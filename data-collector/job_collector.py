
# Collect job postings from Himalayas and JobSpy.
# Supports both direct API calls and running from the terminal.

import requests
import json
import re
import time
from pathlib import Path

API_URL = "https://himalayas.app/jobs/api/search"
MAX_PAGES = 3
INDIA_RESULTS = 20
JOB_AGE_HOURS = 720  # Approximately the last 30 days.

# Locate the project folders independently of the terminal directory.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
RAW_FOLDER = PROJECT_FOLDER / "data" / "raw"


def safe_role_name(role):
    # Convert a role into a safe filename component.
    return re.sub(r"[^a-zA-Z0-9]+", "_", role).strip("_").lower()


def collect_himalayas(role):
    # Collect remote and international jobs from Himalayas.
    all_jobs = []

    for page in range(1, MAX_PAGES + 1):
        print(f"Fetching Himalayas page {page}...")

        params = {"q": role, "sort": "recent", "page": page}

        try:
            response = requests.get(API_URL, params=params, timeout=30)

            if response.status_code == 429:
                print("Himalayas rate limit reached.")
                break

            response.raise_for_status()
            jobs = response.json().get("jobs", [])

            for job in jobs:
                job["source"] = "Himalayas"

            all_jobs.extend(jobs)
            print(f"  Jobs received: {len(jobs)}")

            if not jobs:
                break

            if page < MAX_PAGES:
                time.sleep(1)

        except (requests.RequestException, ValueError) as error:
            print("Himalayas collection error:", error)
            break

    return all_jobs


def collect_india_jobs(role):
    # Collect India-focused jobs using JobSpy and Indeed.
    try:
        from jobspy import scrape_jobs

        print("Searching Indeed for jobs in India...")

        jobs_df = scrape_jobs(
            site_name=["indeed"],
            search_term=role,
            location="India",
            results_wanted=INDIA_RESULTS,
            hours_old=JOB_AGE_HOURS,
            country_indeed="India"
        )

        if jobs_df is None or jobs_df.empty:
            print("No India jobs returned.")
            return []

        # Replace missing DataFrame values with None for JSON.
        jobs_df = jobs_df.astype(object).where(jobs_df.notna(), None)
        jobs = jobs_df.to_dict(orient="records")

        for job in jobs:
            job["source"] = "Indeed (JobSpy)"

        print(f"  India jobs received: {len(jobs)}")
        return jobs

    except Exception as error:
        print("JobSpy collection error:", error)
        return []


def remove_duplicates(jobs):
    # Remove duplicate postings using URLs or source-specific IDs.
    unique_jobs = []
    seen = set()

    for job in jobs:
        source = job.get("source", "Unknown")
        link = (
            job.get("job_url")
            or job.get("applicationLink")
            or job.get("application_url")
        )
        job_id = job.get("guid") or job.get("id")

        if link:
            key = ("url", str(link).strip().lower())
        elif job_id:
            key = ("id", source, str(job_id))
        else:
            # Keep records when there is no reliable duplicate key.
            unique_jobs.append(job)
            continue

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs


def collect_and_save_jobs(role, mode):
    # Collect and save jobs for a role and selected search scope.
    role = role.strip()

    mode_names = {
        "1": "india",
        "2": "international",
        "3": "both",
        "india": "india",
        "international": "international",
        "remote": "international",
        "both": "both"
    }

    mode = mode_names.get(str(mode).strip().lower())

    if not role:
        raise ValueError("Please enter a job role.")

    if mode is None:
        raise ValueError("Choose India, international, or both.")

    all_jobs = []

    if mode in {"india", "both"}:
        all_jobs.extend(collect_india_jobs(role))

    if mode in {"international", "both"}:
        all_jobs.extend(collect_himalayas(role))

    # Remove duplicate records across the selected sources.
    all_jobs = remove_duplicates(all_jobs)

    # Build a role-specific raw-data filename.
    RAW_FOLDER.mkdir(parents=True, exist_ok=True)
    output_file = RAW_FOLDER / f"jobs_{safe_role_name(role)}_{mode}.json"

    # Save the collected data for the next pipeline stage.
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "search_role": role,
                "search_mode": mode,
                "total_jobs_collected": len(all_jobs),
                "jobs": all_jobs
            },
            file,
            indent=4,
            ensure_ascii=False,
            default=str,
            allow_nan=False
        )

    print(f"Collected {len(all_jobs)} unique jobs.")
    print(f"Saved to: {output_file}")

    return {
        "search_role": role,
        "search_mode": mode,
        "total_jobs_collected": len(all_jobs),
        "output_file": str(output_file)
    }


def main():
    # Preserve the existing terminal-based workflow.
    role = input("Enter the job role: ").strip()

    if not role:
        print("Please enter a job role.")
        return

    print("\nSelect search scope:")
    print("1. India")
    print("2. International / remote")
    print("3. Both")

    choice = input("Enter your choice (1-3): ").strip()

    if choice not in {"1", "2", "3"}:
        print("Invalid choice. Please run the program again.")
        return

    collect_and_save_jobs(role, choice)


if __name__ == "__main__":
    main()
