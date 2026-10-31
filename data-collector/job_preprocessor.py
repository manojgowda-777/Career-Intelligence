
# Career Intelligence - Clean and prepare collected job data.
# Supports both Flask backend calls and terminal execution.

import json
import re
from pathlib import Path
from html import unescape
from datetime import datetime, timezone


# Locate project folders independently of the terminal directory.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
RAW_FOLDER = PROJECT_FOLDER / "data" / "raw"
PROCESSED_FOLDER = PROJECT_FOLDER / "data" / "processed"


def safe_role_name(role):
    # Convert the role into a safe filename component.
    return re.sub(r"[^a-zA-Z0-9]+", "_", role).strip("_").lower()


def normalize_mode(mode):
    # Accept either menu numbers or readable mode names.
    mode_names = {
        "1": "india",
        "2": "international",
        "3": "both",
        "india": "india",
        "international": "international",
        "remote": "international",
        "both": "both"
    }

    normalized = mode_names.get(str(mode).strip().lower())

    if normalized is None:
        raise ValueError("Choose India, international, or both.")

    return normalized


def first_value(job, *keys):
    # Return the first available non-empty field.
    for key in keys:
        value = job.get(key)

        if value is not None and value != "":
            return value

    return None


def clean_html(text):
    # Remove HTML tags and normalize whitespace.
    if not text:
        return ""

    text = unescape(str(text))
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def convert_timestamp(timestamp):
    # Convert Unix timestamps to readable UTC dates.
    if timestamp is None or timestamp == "":
        return None

    try:
        if isinstance(timestamp, str):
            try:
                timestamp = float(timestamp)
            except ValueError:
                # Preserve dates that are already readable strings.
                return timestamp

        return datetime.fromtimestamp(
            float(timestamp),
            timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S UTC")

    except (ValueError, TypeError, OSError, OverflowError):
        return None


def clean_job(job):
    # Normalize field names from Himalayas and JobSpy.
    source = job.get("source", "Himalayas")

    description = clean_html(
        first_value(job, "description") or ""
    )

    excerpt = clean_html(
        first_value(job, "excerpt", "summary") or ""
    )

    return {
        "title": first_value(job, "title"),
        "company": first_value(job, "companyName", "company"),
        "employment_type": first_value(
            job, "employmentType", "job_type"
        ),
        "seniority": first_value(job, "seniority", "job_level"),

        "categories": first_value(job, "categories") or [],
        "parent_categories": first_value(
            job, "parentCategories"
        ) or [],

        "location": first_value(
            job, "location", "locationRestrictions"
        ),
        "location_restrictions": first_value(
            job, "locationRestrictions"
        ) or [],
        "timezone_restrictions": first_value(
            job, "timezoneRestrictions"
        ) or [],

        "min_salary": first_value(job, "minSalary", "min_amount"),
        "max_salary": first_value(job, "maxSalary", "max_amount"),
        "salary_period": first_value(
            job, "salaryPeriod", "interval"
        ),
        "currency": first_value(job, "currency"),

        "excerpt": excerpt,
        "description": description,

        "published_at": convert_timestamp(
            first_value(job, "pubDate", "date_posted")
        ),
        "expiry_at": convert_timestamp(
            first_value(job, "expiryDate")
        ),

        "source": source,
        "application_link": first_value(
            job, "applicationLink", "job_url"
        ),
        "job_id": first_value(job, "guid", "id"),

        "is_remote": first_value(job, "is_remote"),
        "skills": first_value(job, "skills"),
        "company_url": first_value(
            job, "companyUrl", "company_url"
        )
    }


def preprocess_jobs(role, mode):
    # Clean the raw dataset for the requested role and mode.
    role = role.strip()

    if not role:
        raise ValueError("Please enter a job role.")

    mode = normalize_mode(mode)
    safe_role = safe_role_name(role)

    input_file = RAW_FOLDER / f"jobs_{safe_role}_{mode}.json"
    output_file = (
        PROCESSED_FOLDER / f"clean_jobs_{safe_role}_{mode}.json"
    )

    # Check that collection has already created the raw file.
    if not input_file.exists():
        raise FileNotFoundError(
            f"Raw job data was not found: {input_file}. "
            "Collect jobs for this role and search mode first."
        )

    # Load the collected postings.
    with input_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = data.get("jobs", [])
    clean_jobs = []

    # Clean each posting using the existing cleaning rules.
    for number, job in enumerate(jobs, start=1):
        clean_jobs.append(clean_job(job))
        print(f"Preprocessed {number}/{len(jobs)}")

    # Ensure the output folder exists.
    PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

    # Save the cleaned postings and their metadata.
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "search_role": data.get("search_role", role),
                "search_mode": data.get("search_mode", mode),
                "total_jobs": len(clean_jobs),
                "jobs": clean_jobs
            },
            file,
            indent=4,
            ensure_ascii=False,
            default=str
        )

    print(f"Preprocessed {len(clean_jobs)} jobs.")
    print(f"Saved to: {output_file}")

    # Return information for the Flask backend.
    return {
        "search_role": role,
        "search_mode": mode,
        "total_jobs": len(clean_jobs),
        "output_file": str(output_file)
    }


def main():
    # Preserve the original terminal workflow.
    role = input("Enter the job role: ").strip()

    if not role:
        print("Please enter a job role.")
        return

    print("\nSelect the raw dataset to preprocess:")
    print("1. India")
    print("2. International")
    print("3. Both")

    choice = input("Enter your choice (1-3): ").strip()

    try:
        preprocess_jobs(role, choice)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Preprocessing failed: {error}")


if __name__ == "__main__":
    main()
