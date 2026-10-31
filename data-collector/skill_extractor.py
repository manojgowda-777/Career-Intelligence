
# Career Intelligence - Extract skills from cleaned job postings.
# Supports Flask backend calls and terminal execution.

import json
import re
import sys
from pathlib import Path
from html import unescape

# Locate project folders independently of the terminal directory.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
PROCESSED_FOLDER = PROJECT_FOLDER / "data" / "processed"

# Import the shared skill library from the backend folder.
BACKEND_FOLDER = PROJECT_FOLDER / "backend"
sys.path.insert(0, str(BACKEND_FOLDER))

from skill_library import get_skill_aliases

# Use the same skills for job postings and resume analysis.
SKILL_ALIASES = get_skill_aliases()

def safe_role_name(role):
    # Convert a role into a safe filename component.
    return re.sub(r"[^a-zA-Z0-9]+", "_", role).strip("_").lower()


def normalize_mode(mode):
    # Accept menu numbers or readable search-mode names.
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

# Headings that commonly introduce unrelated promotional content.
STOP_HEADINGS = [
    "not your tech stack",
    "other technologies",
    "other tech stacks",
    "other roles",
    "other positions",
    "related jobs",
]


def remove_irrelevant_sections(text):
    # Remove promotional sections after the earliest known heading.
    text_lower = text.lower()
    cut_positions = []

    for heading in STOP_HEADINGS:
        position = text_lower.find(heading)

        if position != -1:
            cut_positions.append(position)

    if cut_positions:
        text = text[:min(cut_positions)]

    # Ignore alternative-language examples that are not requirements.
    text = re.sub(
        r"\ba server[- ]side language such as\b[^.]*\.",
        " ",
        text,
        flags=re.IGNORECASE
    )

    return text


def is_multi_role_job(title, description):
    # Flag postings that advertise several different job roles.
    text = f"{title or ''} {description or ''}".lower()

    multi_role_phrases = [
        "we are looking for the following roles",
        "we have the following openings",
        "multiple positions available",
        "various positions available",
        "open positions include",
    ]

    return any(phrase in text for phrase in multi_role_phrases)


def extract_skills(text):
    # Decode HTML entities and remove known irrelevant sections.
    text = unescape(text or "")
    text = remove_irrelevant_sections(text)
    text_lower = text.lower()

    found_skills = []

    for standard_name, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            # Match complete terms instead of partial words.
            pattern = (
                r"(?<!\w)"
                + re.escape(alias.lower())
                + r"(?!\w)"
            )

            if re.search(pattern, text_lower):
                found_skills.append(standard_name)
                break

    # Return each standard skill only once per job.
    return found_skills


def extract_skills_from_jobs(role, mode):
    # Extract skills from the cleaned dataset for a selected role.
    role = role.strip()

    if not role:
        raise ValueError("Please enter a job role.")

    mode = normalize_mode(mode)
    safe_role = safe_role_name(role)

    input_file = (
        PROCESSED_FOLDER / f"clean_jobs_{safe_role}_{mode}.json"
    )
    output_file = (
        PROCESSED_FOLDER / f"jobs_with_skills_{safe_role}_{mode}.json"
    )

    # Ensure the cleaned dataset exists before processing.
    if not input_file.exists():
        raise FileNotFoundError(
            f"Cleaned job data was not found: {input_file}. "
            "Run the collection and preprocessing stages first."
        )

    # Load cleaned job postings.
    with input_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = data.get("jobs", [])

    print(f"Extracting skills from {len(jobs)} jobs...")

    # Extract skills and identify potentially multi-role postings.
    for number, job in enumerate(jobs, start=1):
        text = " ".join([
            job.get("title") or "",
            job.get("excerpt") or "",
            job.get("description") or ""
        ])

        job["extracted_skills"] = extract_skills(text)
        job["is_multi_role"] = is_multi_role_job(
            job.get("title"),
            job.get("description")
        )

        print(
            f"Processed {number}/{len(jobs)} - "
            f"{len(job['extracted_skills'])} skills found"
        )

    # Exclude multi-role postings from demand calculations.
    analysis_jobs = [
        job for job in jobs
        if not job.get("is_multi_role", False)
    ]

    # Count each skill at most once per suitable job.
    skill_counts = {}

    for job in analysis_jobs:
        for skill in set(job.get("extracted_skills", [])):
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    # Save all extracted records and metadata for later analysis.
    data["search_role"] = data.get("search_role", role)
    data["search_mode"] = data.get("search_mode", mode)
    data["total_jobs"] = len(jobs)
    data["analysis_jobs_count"] = len(analysis_jobs)
    data["excluded_multi_role_jobs"] = len(jobs) - len(analysis_jobs)
    data["jobs"] = jobs

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
            default=str
        )

    print(f"Total jobs collected: {len(jobs)}")
    print(f"Jobs suitable for analysis: {len(analysis_jobs)}")
    print(f"Multi-role jobs excluded: {len(jobs) - len(analysis_jobs)}")

    # Show demand percentages for the suitable postings.
    total_analysis_jobs = len(analysis_jobs)

    print("\nSkill demand percentages:")

    if total_analysis_jobs > 0:
        for skill, count in sorted(
            skill_counts.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            percentage = (count / total_analysis_jobs) * 100
            print(f"{skill}: {percentage:.1f}% ({count} jobs)")
    else:
        print("No suitable jobs available for analysis.")

    print(f"Saved to: {output_file}")

    # Return a summary that Flask can use.
    return {
        "search_role": role,
        "search_mode": mode,
        "total_jobs": len(jobs),
        "analysis_jobs_count": total_analysis_jobs,
        "excluded_multi_role_jobs": len(jobs) - total_analysis_jobs,
        "output_file": str(output_file)
    }


def main():
    # Preserve terminal-based execution.
    role = input("Enter the job role: ").strip()

    if not role:
        print("Please enter a job role.")
        return

    print("\nSelect the cleaned dataset:")
    print("1. India")
    print("2. International")
    print("3. Both")

    choice = input("Enter your choice (1-3): ").strip()

    try:
        extract_skills_from_jobs(role, choice)
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Skill extraction failed: {error}")


if __name__ == "__main__":
    main()
