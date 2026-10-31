
# Career Intelligence - Main Flask Backend
# Connects job collection, preprocessing, and skill extraction.
from flask import Flask, jsonify, request
from flask_cors import CORS
from mcq_engine import get_quiz_questions, submit_quiz_answers
from resume_analyzer import (
    extract_resume_text,
    extract_resume_skills,
    compare_resume_with_job_skills
)
from pathlib import Path
from collections import Counter
import sys
import json

# Create the Flask application.
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Locate the project and its folders.
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "data" / "processed"
COLLECTOR_FOLDER = PROJECT_FOLDER / "data-collector"

# Allow Python to import modules from data-collector.
sys.path.insert(0, str(COLLECTOR_FOLDER))

# Import the reusable functions from our existing scripts.
from job_collector import collect_and_save_jobs
from job_preprocessor import preprocess_jobs
from skill_extractor import extract_skills_from_jobs


# Home page: check whether the backend is running.
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "project": "Career Intelligence",
        "status": "Backend is running",
        "message": "Welcome to Career Intelligence API"
    })


# Health check: verify that the backend is healthy.
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


# Run the complete job pipeline for a newly searched role.
@app.route("/api/role/search", methods=["POST"])
def search_role_pipeline():

    # Read the role and search region from the JSON request.
    payload = request.get_json(silent=True) or {}
    role = str(payload.get("role", "")).strip()
    mode = str(payload.get("mode", "")).strip().lower()

    # Check the user's input.
    if not role:
        return jsonify({
            "error": "Please enter a job role."
        }), 400

    # Accept the three supported search regions.
    valid_modes = {
        "1": "india",
        "2": "international",
        "3": "both",
        "india": "india",
        "international": "international",
        "remote": "international",
        "both": "both"
    }

    mode = valid_modes.get(mode)

    if mode is None:
        return jsonify({
            "error": "Choose India, international, or both.",
            "valid_modes": ["india", "international", "both"]
        }), 400

    try:
        # Stage 1: collect job postings for this role.
        collection_result = collect_and_save_jobs(role, mode)

        # Stage 2: clean the collected postings.
        preprocessing_result = preprocess_jobs(role, mode)

        # Stage 3: extract skills from the cleaned postings.
        extraction_result = extract_skills_from_jobs(role, mode)

        # Open the processed file containing extracted skills.
        skills_file = Path(extraction_result["output_file"])

        with skills_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Exclude postings identified as advertisements for multiple roles.
        jobs = data.get("jobs", [])
        analysis_jobs = [
            job for job in jobs
            if not job.get("is_multi_role", False)
        ]

        # Count each skill at most once per suitable job.
        skill_counts = Counter()

        for job in analysis_jobs:
            skill_counts.update(
                set(job.get("extracted_skills", []))
            )

        # Calculate demand percentages using suitable jobs as the denominator.
        total_analysis_jobs = len(analysis_jobs)
        skill_results = []

        for skill, count in skill_counts.most_common():
            demand_percentage = round(
                (count / total_analysis_jobs) * 100,
                2
            ) if total_analysis_jobs > 0 else 0

            skill_results.append({
                "skill": skill,
                "job_count": count,
                "demand_percentage": demand_percentage
            })

        # Return the results from the complete pipeline.
        return jsonify({
            "message": "Role analysis completed successfully",
            "role": role,
            "search_mode": mode,
            "total_jobs_collected": collection_result[
                "total_jobs_collected"
            ],
            "total_jobs_processed": preprocessing_result["total_jobs"],
            "total_jobs_analyzed": total_analysis_jobs,
            "excluded_multi_role_jobs": extraction_result[
                "excluded_multi_role_jobs"
            ],
            "total_skills_found": len(skill_results),
            "skills": skill_results
        })

    except (ValueError, FileNotFoundError, json.JSONDecodeError) as error:
        # Report expected pipeline and data errors.
        return jsonify({
            "error": str(error)
        }), 400

    except Exception:
        # Avoid exposing internal paths or technical details to users.
        app.logger.exception("Role analysis pipeline failed.")

        return jsonify({
            "error": (
                "The role analysis could not be completed. "
                "Check the backend terminal for details."
            )
        }), 500


# Existing role-analysis endpoint: keep the current test working.
@app.route("/api/role", methods=["GET"])
def search_existing_role():

    # Read the requested role.
    role = request.args.get("role", "").strip()

    if not role:
        return jsonify({
            "error": "Please enter a job role."
        }), 400

    # The legacy test dataset uses a filename without a search-mode suffix.
    data_file = (
        DATA_FOLDER / "jobs_with_skills_full_stack_developer.json"
    )

    if not data_file.exists():
        return jsonify({
            "error": "The existing test dataset was not found."
        }), 404

    # Read the existing test dataset.
    with data_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    saved_role = data.get("search_role", "").strip()

    if role.casefold() != saved_role.casefold():
        return jsonify({
            "message": "Use POST /api/role/search to collect and analyze a role.",
            "requested_role": role,
            "available_role": saved_role
        }), 404

    # Count skills from the saved dataset.
    jobs = data.get("jobs", [])
    analysis_jobs = [
        job for job in jobs
        if not job.get("is_multi_role", False)
    ]

    skill_counts = Counter()

    for job in analysis_jobs:
        skill_counts.update(set(job.get("extracted_skills", [])))

    total_jobs = len(analysis_jobs)

    skills = [
        {
            "skill": skill,
            "job_count": count,
            "demand_percentage": round(
                (count / total_jobs) * 100, 2
            ) if total_jobs > 0 else 0
        }
        for skill, count in skill_counts.most_common()
    ]

    return jsonify({
        "message": "Skills retrieved successfully",
        "role": saved_role,
        "total_jobs_analyzed": total_jobs,
        "total_skills_found": len(skills),
        "skills": skills
    })


# Search for actual job postings for a selected role and region.
@app.route("/api/jobs/search", methods=["POST"])
def search_jobs():

    # Read the role and search region from the request.
    payload = request.get_json(silent=True) or {}
    role = str(payload.get("role", "")).strip()
    mode = str(payload.get("mode", "")).strip().lower()

    # Validate the user's input.
    if not role:
        return jsonify({
            "error": "Please enter a job role."
        }), 400

    valid_modes = {
        "1": "india",
        "2": "international",
        "3": "both",
        "india": "india",
        "international": "international",
        "remote": "international",
        "both": "both"
    }

    mode = valid_modes.get(mode)

    if mode is None:
        return jsonify({
            "error": "Choose India, international, or both."
        }), 400

    try:
        # Collect and clean jobs using the existing functions.
        collect_and_save_jobs(role, mode)
        preprocessing_result = preprocess_jobs(role, mode)

        # Load the cleaned job postings.
        jobs_file = Path(preprocessing_result["output_file"])

        with jobs_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Return job listings, not skill statistics.
        jobs = data.get("jobs", [])

        return jsonify({
            "message": "Job search completed successfully",
            "role": role,
            "search_mode": mode,
            "total_jobs": len(jobs),
            "jobs": jobs
        })

    except (ValueError, FileNotFoundError, json.JSONDecodeError) as error:
        return jsonify({
            "error": str(error)
        }), 400

    except Exception:
        app.logger.exception("Job search failed.")

        return jsonify({
            "error": (
                "The job search could not be completed. "
                "Check the backend terminal for details."
            )
        }), 500

# Upload a PDF resume and extract its text.
@app.route("/api/resume/extract", methods=["POST"])
def extract_resume():

    # Check that the request contains a PDF file.
    if "resume" not in request.files:
        return jsonify({
            "error": "Please upload a PDF resume using the 'resume' field."
        }), 400

    uploaded_file = request.files["resume"]

    if not uploaded_file.filename:
        return jsonify({
            "error": "Please select a PDF file."
        }), 400

    # Accept PDF files only.
    if not uploaded_file.filename.lower().endswith(".pdf"):
        return jsonify({
            "error": "Only PDF files are supported."
        }), 400

    try:
        # Read the uploaded file into memory.
        pdf_bytes = uploaded_file.read()

        if not pdf_bytes:
            return jsonify({
                "error": "The uploaded file is empty."
            }), 400

        # Extract readable text from the PDF.
        resume_text = extract_resume_text(pdf_bytes)

        return jsonify({
            "message": "Resume text extracted successfully",
            "filename": uploaded_file.filename,
            "characters_extracted": len(resume_text),
            "resume_text": resume_text
        })

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

    except Exception:
        app.logger.exception("Resume extraction failed.")

        return jsonify({
            "error": (
                "Could not read the PDF. "
                "Check the backend terminal for details."
            )
        }), 500


# Compare resume skills with current job requirements.
@app.route("/api/resume/compare", methods=["POST"])
def compare_resume():
    import re
    from skill_library import get_skill_aliases

    # Read the uploaded resume and selected job role.
    resume_file = request.files.get("resume")
    role = request.form.get("role", "").strip()
    mode = request.form.get("mode", "international").strip().lower()

    # Validate the input.
    if not resume_file or not resume_file.filename:
        return jsonify({"error": "Please upload a resume PDF."}), 400

    if not resume_file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Please upload a PDF file."}), 400

    if not role:
        return jsonify({"error": "Please enter a job role."}), 400

    if mode not in ["india", "international", "both"]:
        return jsonify({"error": "Invalid search mode."}), 400

    try:
        # Step 1: Extract skills from the resume.
        resume_text = extract_resume_text(resume_file.read())
        resume_skills = extract_resume_skills(resume_text)

        # Step 2: Collect and preprocess current job postings.
        collect_and_save_jobs(role, mode)
        preprocessing_result = preprocess_jobs(role, mode)

        # Step 3: Open the processed job data.
        data_path = Path(preprocessing_result["output_file"])

        with data_path.open("r", encoding="utf-8") as file:
            job_data = json.load(file)

        # Get the list of job records.
        if isinstance(job_data, dict):
            jobs = job_data.get("jobs", [])
        elif isinstance(job_data, list):
            jobs = job_data
        else:
            jobs = []

        # Step 4: Identify required skills using the skill library.
        skill_aliases = get_skill_aliases()
        required_skills = set()

        for job in jobs:
            if not isinstance(job, dict):
                continue

            # Add skills already provided in the job data.
            saved_skills = job.get("skills") or []

            if isinstance(saved_skills, list):
                for skill in saved_skills:
                    if isinstance(skill, str) and skill.strip():
                        required_skills.add(skill.strip())

            # Search the job title and description for known skills.
            title = job.get("title") or ""
            description = job.get("description") or ""
            job_text = f"{title} {description}".lower()

            for skill, aliases in skill_aliases.items():
                for alias in aliases:
                    pattern = (
                        r"(?<!\w)"
                        + re.escape(alias.lower())
                        + r"(?!\w)"
                    )

                    if re.search(pattern, job_text):
                        required_skills.add(skill)
                        break

        # Remove duplicates and sort the skills.
        required_skills = sorted(required_skills)

        # Stop if no skills could be detected.
        if not required_skills:
            return jsonify({
                "error": "No required skills were found in the job data."
            }), 422

        # Step 5: Compare resume skills with job requirements.
        result = compare_resume_with_job_skills(
            resume_skills,
            required_skills
        )

        # Step 6: Return the comparison results.
        return jsonify({
            "message": "Resume comparison completed successfully.",
            "role": role,
            "search_mode": mode,
            "resume_skills": resume_skills,
            "required_skills": required_skills,
            "total_jobs_analyzed": len(jobs),
            **result
        }), 200

    except Exception:
        # Print technical details in the Flask terminal.
        app.logger.exception("Resume comparison failed")

        return jsonify({
            "error": (
                "Resume comparison failed. "
                "Check the backend terminal for details."
            )
        }), 500

@app.route("/api/mcq/generate", methods=["POST"])
def generate_mcq():
    data = request.get_json(silent=True) or {}

    required_skills = data.get("skills", [])

    if not isinstance(required_skills, list) or not required_skills:
        return jsonify({
            "success": False,
            "message": "Please provide a non-empty list of skills."
        }), 400

    if not all(
        isinstance(skill, str) and skill.strip()
        for skill in required_skills
    ):
        return jsonify({
            "success": False,
            "message": "Every skill must be a non-empty string."
        }), 400

    result = get_quiz_questions(required_skills, question_count=10)

    if not result["success"]:
        return jsonify(result), 400

    return jsonify(result), 200


@app.route("/api/mcq/submit", methods=["POST"])
def submit_mcq():
    data = request.get_json(silent=True) or {}

    quiz_id = data.get("quiz_id")
    answers = data.get("answers")

    result = submit_quiz_answers(quiz_id, answers)

    if not result["success"]:
        return jsonify(result), 400

    return jsonify(result), 200


# Start the backend server.
if __name__ == "__main__":
    app.run(debug=True, port=5000)
