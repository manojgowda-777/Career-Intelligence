
"use client";

import { Suspense, useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";

const API_URL = "http://127.0.0.1:5000";

function MCQContent() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const role = searchParams.get("role") || "";
  const skillsParam = searchParams.get("skills") || "";
  const quizKey = `${role}|${skillsParam}`;
  const [questions, setQuestions] = useState([]);
  const [quizId, setQuizId] = useState("");
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");
  useEffect(() => {
  setQuestions([]);
  setQuizId("");
  setAnswers({});
  setResult(null);
  setError("");
  setLoading(true);
  }, [quizKey]);

  useEffect(() => {
    let cancelled = false;

    async function generateQuiz() {
      try {
        const skills = skillsParam
          .split(",")
          .map((skill) => skill.trim())
          .filter(Boolean);

        if (!role || skills.length === 0) {
          throw new Error(
            "No role or skills were provided. Return to Search for Roles and search again."
          );
        }

        const response = await fetch(`${API_URL}/api/mcq/generate`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ skills }),
        });

        const data = await response.json();

        if (!response.ok || !data.success) {
          throw new Error(
            data.message || "Unable to generate the MCQ assessment."
          );
        }

        if (
          !Array.isArray(data.questions) ||
          data.questions.length !== 10 ||
          !data.quiz_id
        ) {
          throw new Error(
            "The backend did not return a complete 10-question quiz."
          );
        }

        if (!cancelled) {
          setQuestions(data.questions);
          setQuizId(data.quiz_id);
        }
      } catch (err) {
        if (!cancelled) {
          setError(
            err.message ||
              "Unable to connect to the backend. Check that Flask is running."
          );
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    generateQuiz();

    return () => {
      cancelled = true;
    };
  }, [role, skillsParam]);

  function selectAnswer(questionId, option) {
    if (result) return;

    setAnswers((previous) => ({
      ...previous,
      [questionId]: option,
    }));
  }

  async function submitQuiz() {
    if (Object.keys(answers).length !== questions.length) {
      setError("Please answer all 10 questions before submitting.");
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const response = await fetch(`${API_URL}/api/mcq/submit`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          quiz_id: quizId,
          answers: questions.map((question) => ({
            id: question.id,
            answer: answers[question.id],
          })),
        }),
      });

      const data = await response.json();

      if (!response.ok || !data.success) {
        throw new Error(data.message || "Unable to submit your answers.");
      }

      setResult(data);
    } catch (err) {
      setError(err.message || "Unable to submit the quiz.");
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) {
    return (
      <main className="mcq-page">
        <div className="mcq-message">
          <div className="mcq-spinner" />
          <h1>Preparing your assessment...</h1>
          <p>Generating questions from the available skill banks.</p>
        </div>
      </main>
    );
  }

  if (error && questions.length === 0) {
    return (
      <main className="mcq-page">
        <div className="mcq-message">
          <h1>Unable to start the assessment</h1>
          <p className="mcq-error">{error}</p>
          <button className="mcq-primary-button" onClick={() => router.push("/roles")}>
            Back to Search for Roles
          </button>
        </div>
      </main>
    );
  }

  return (
    <main className="mcq-page">
      <header className="mcq-heading">
        <span className="roles-section-label">SKILL ASSESSMENT</span>
        <h1>Test your knowledge</h1>
        <p>
          Role: <strong>{role}</strong>
        </p>
        <div className="mcq-progress-info">
          <span>
            {result
              ? "Assessment completed"
              : `${Object.keys(answers).length} of ${questions.length} answered`}
          </span>
          <span>{questions.length} questions</span>
        </div>
        <div className="mcq-progress-track">
          <div
            className="mcq-progress-fill"
            style={{
              width: `${
                result ? 100 : (Object.keys(answers).length / questions.length) * 100
              }%`,
            }}
          />
        </div>
      </header>

      {error && <p className="mcq-error">{error}</p>}

      {result && (
        <section className="mcq-result-card">
          <span className="roles-section-label">YOUR RESULTS</span>
          <h2>
            {result.score} / {questions.length}
          </h2>
          <p>{result.percentage}% score</p>
          <p>Your assessment has been submitted successfully.</p>
        </section>
      )}

      <section className="mcq-questions">
        {questions.map((question, index) => {
          const questionId = question.id;
          const selected = answers[questionId];
          const explanation = result?.results?.find(
            (item) => item.id === questionId
          );
          return (
            <article className="mcq-question-card" key={questionId}>
              <div className="mcq-question-meta">
                <span>QUESTION {index + 1} OF {questions.length}</span>
                {question.skill && <span>{question.skill}</span>}
              </div>

              <h2>{question.question}</h2>

              <div className="mcq-options">
                {question.options.map((option, optionIndex) => {
                  const letter = ["A", "B", "C", "D"][optionIndex] || "";
                  const isSelected = selected === option;
                  const isCorrect =
                    Boolean(result) && option === explanation?.correct_answer;
                  const isWrongSelected =
                    Boolean(result) && isSelected && !isCorrect;
                  return (
                    <button
                      type="button"
                      key={`${questionId}-${optionIndex}`}
                      className={[
                        "mcq-option",
                        isSelected ? "selected" : "",
                        isCorrect ? "correct" : "",
                        isWrongSelected ? "incorrect" : "",
                      ].filter(Boolean).join(" ")}
                      onClick={() => selectAnswer(questionId, option)}
                      disabled={Boolean(result)}
                    >
                      <span className="mcq-option-letter">{letter}</span>
                      <span>{option}</span>
                    </button>
                  );
                })}
              </div>

              {result && explanation && (
                <div className="mcq-explanation">
                  <strong>
                    {selected === explanation.correct_answer
                      ? "Correct answer"
                      : "Correct answer: " + explanation.correct_answer}
                  </strong>
                  {explanation.explanation && <p>{explanation.explanation}</p>}
                </div>
              )}
            </article>
          );
        })}
      </section>

      {!result ? (
        <div className="mcq-submit-area">
          <p>Review your answers before submitting.</p>
          <button
            className="mcq-primary-button"
            onClick={submitQuiz}
            disabled={submitting}
          >
            {submitting ? "Submitting..." : "Submit Assessment"}
          </button>
        </div>
      ) : (
        <div className="mcq-submit-area">
          <button
            className="mcq-primary-button"
            onClick={() => router.push("/roles")}
          >
            Back to Search for Roles
          </button>
        </div>
      )}
    </main>
  );
}
export default function MCQPage() {
  return (
    <Suspense
      fallback={
        <main className="mcq-page">
          <div className="mcq-message">
            <div className="mcq-spinner" />
            <h1>Loading assessment...</h1>
          </div>
        </main>
      }
    >
      <MCQContent />
    </Suspense>
  );
}