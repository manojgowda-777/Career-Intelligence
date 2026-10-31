
from mcq_engine import get_quiz_questions

# Test with the Python question bank
result = get_quiz_questions(["Python"], question_count=10)

if result["success"]:
    print("Quiz generated successfully!")
    print("Number of questions:", len(result["questions"]))

    for number, question in enumerate(result["questions"], start=1):
        print(f"\n{number}. {question['question']}")
        for option in question["options"]:
            print("-", option)

    # Verify that correct answers are hidden
    assert all(
        "correct_answer" not in question
        for question in result["questions"]
    )

    print("\nTest passed: answers are hidden.")
else:
    print("Quiz could not be generated:", result["message"])
