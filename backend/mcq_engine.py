import random
import secrets

from mcq_questions import MCQ_QUESTION_BANK


ACTIVE_QUIZZES = {}
def get_quiz_questions(required_skills, question_count=10):
    """
    Select random questions from the banks matching the required skills.
    Correct answers are not included in the returned questions.
    """

    available_questions = []
    seen_ids = set()

    for skill in required_skills:
        skill_key = skill.strip().lower()

        for question in MCQ_QUESTION_BANK.get(skill_key, []):
            if question["id"] not in seen_ids:
                available_questions.append(question)
                seen_ids.add(question["id"])

    if len(available_questions) < question_count:
        return {
            "success": False,
            "message": (
                f"Only {len(available_questions)} matching questions are "
                f"available. At least {question_count} are needed."
            ),
            "available_count": len(available_questions),
        }

    selected_questions = random.sample(
        available_questions, question_count
    )

    # Do not send correct answers to the frontend before submission.
    public_questions = []

    for question in selected_questions:
        public_questions.append({
            "id": question["id"],
            "skill": question["skill"],
            "topic": question["topic"],
            "question": question["question"],
            "options": question["options"],
        })

    quiz_id = secrets.token_urlsafe(24)

    ACTIVE_QUIZZES[quiz_id] = {
        "question_ids": [question["id"] for question in selected_questions],
        "submitted": False,
    }

    return {
        "success": True,
        "quiz_id": quiz_id,
        "questions": public_questions,
    }

def submit_quiz_answers(quiz_id, answers):
    """
    Check submitted answers against the server-side question bank.
    Return the score and explanations after submission.

    answers format:
    [
        {"id": "python_001", "answer": "def"},
        ...
    ]
    """
    if not isinstance(quiz_id, str) or quiz_id not in ACTIVE_QUIZZES:
        return {
            "success": False,
            "message": "Invalid or expired quiz ID."
        }

    quiz = ACTIVE_QUIZZES[quiz_id]

    if quiz["submitted"]:
        return {
            "success": False,
            "message": "This quiz has already been submitted."
        }

    expected_ids = set(quiz["question_ids"])
    if not isinstance(answers, list) or len(answers) != 10:
        return {
            "success": False,
            "message": "Please submit answers for exactly 10 questions."
        }

    question_lookup = {
        question["id"]: question
        for skill_questions in MCQ_QUESTION_BANK.values()
        for question in skill_questions
    }

    submitted_ids = []

    for item in answers:
        if not isinstance(item, dict):
            return {
                "success": False,
                "message": "Each answer must include a question ID and answer."
            }

        question_id = item.get("id")
        selected_answer = item.get("answer")

        if not isinstance(question_id, str) or not isinstance(selected_answer, str):
            return {
                "success": False,
                "message": "Question IDs and answers must be strings."
            }
        if question_id not in expected_ids:
            return {
                "success": False,
                "message": "This question does not belong to the selected quiz."
            }
        if question_id not in question_lookup:
            return {
                "success": False,
                "message": f"Unknown question ID: {question_id}"
            }

        
        if question_id in submitted_ids:
            return {
                "success": False,
                "message": "Duplicate question IDs are not allowed."
            }

        submitted_ids.append(question_id)

        question = question_lookup[question_id]

        if selected_answer not in question["options"]:
            return {
                "success": False,
                "message": f"Invalid option for question {question_id}."
            }

    if len(submitted_ids) != len(expected_ids) or set(submitted_ids) != expected_ids:
        return {
            "success": False,
            "message": "Please submit all questions from this quiz."
        }
    score = 0
    results = []
    topic_scores = {}

    for item in answers:
        question = question_lookup[item["id"]]
        selected_answer = item["answer"]
        is_correct = selected_answer == question["correct_answer"]

        if is_correct:
            score += 1

        topic = question.get("topic", question["skill"])
        if topic not in topic_scores:
            topic_scores[topic] = {"correct": 0, "total": 0}

        topic_scores[topic]["total"] += 1
        if is_correct:
            topic_scores[topic]["correct"] += 1

        results.append({
            "id": question["id"],
            "question": question["question"],
            "selected_answer": selected_answer,
            "correct_answer": question["correct_answer"],
            "is_correct": is_correct,
            "explanation": question["explanation"],
            "topic": topic
        })

    if score >= 8:
        feedback = "Excellent work! You have a strong understanding of these topics."
        celebration = True
    else:
        feedback = "Good effort! Review the explanations and practise the weaker topics."
        celebration = False

    weaker_topics = [
        topic
        for topic, values in topic_scores.items()
        if values["correct"] < values["total"]
    ]
    ACTIVE_QUIZZES[quiz_id]["submitted"] = True
    return {
        "success": True,
        "score": score,
        "total": 10,
        "percentage": score * 10,
        "feedback": feedback,
        "celebration": celebration,
        "weaker_topics": weaker_topics,
        "topic_scores": topic_scores,
        "results": results
    }
