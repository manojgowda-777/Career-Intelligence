
# Career Intelligence - Resume PDF Analyzer.
# Extracts PDF text and identifies skills from the reusable skill library.

from io import BytesIO
import re

from pypdf import PdfReader
from skill_library import get_skill_aliases


# Load the reusable skill library.
SKILL_ALIASES = get_skill_aliases()


def extract_resume_text(pdf_bytes):
    # Open the uploaded PDF from its bytes.
    reader = PdfReader(BytesIO(pdf_bytes))

    # Reject password-protected PDFs.
    if reader.is_encrypted:
        raise ValueError(
            "Password-protected PDFs are not supported yet."
        )

    # Extract text from every page.
    pages_text = []

    for page in reader.pages:
        text = page.extract_text() or ""

        if text.strip():
            pages_text.append(text.strip())

    # Combine all extracted text.
    resume_text = "\n\n".join(pages_text).strip()

    # Check whether readable text was found.
    if not resume_text:
        raise ValueError(
            "No readable text was found in the PDF. "
            "The resume may be scanned or image-based."
        )

    return resume_text


def extract_resume_skills(resume_text):
    # Convert text to lowercase for matching.
    text = resume_text.lower()
    found_skills = []

    # Check every skill and its alternative names.
    for skill, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            # Match complete terms to reduce false matches.
            pattern = (
                r"(?<!\w)" + re.escape(alias.lower()) + r"(?!\w)"
            )

            if re.search(pattern, text):
                found_skills.append(skill)
                break

    # Return each skill once, using its standard name.
    return found_skills

def compare_resume_with_job_skills(resume_skills, required_skills):
    # Convert skill names to lowercase for fair comparison.
    resume_set = {skill.strip().lower() for skill in resume_skills}
    required_set = {skill.strip().lower() for skill in required_skills}

    # Find skills that appear in both the resume and job requirements.
    matching_skills = sorted(resume_set & required_set)

    # Find required skills that were not detected in the resume.
    missing_skills = sorted(required_set - resume_set)

    # Calculate the score based on the required skills matched.
    if required_set:
        readiness_score = round(
            len(matching_skills) / len(required_set) * 100, 2
        )
    else:
        readiness_score = 0

    # Return all comparison results.
    return {
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "matched_count": len(matching_skills),
        "required_count": len(required_set),
        "readiness_score": readiness_score
    }
