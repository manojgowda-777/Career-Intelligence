
"use client";

import { useState } from "react";

const API_URL = "http://127.0.0.1:5000";

export default function ResumeAnalyzerPage() {
  const [resume, setResume] = useState(null);
  const [role, setRole] = useState("");
  const [mode, setMode] = useState("both");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  function handleFileChange(event) {
    const file = event.target.files?.[0];

    setResume(null);
    setResult(null);
    setError("");

    if (!file) return;

    if (!file.name.toLowerCase().endsWith(".pdf")) {
      setError("Please select a PDF resume.");
      event.target.value = "";
      return;
    }

    setResume(file);
  }

  async function handleAnalyze(event) {
    event.preventDefault();
    setError("");
    setResult(null);

    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!role.trim()) {
      setError("Please enter your target job role.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("resume", resume);
      formData.append("role", role.trim());
      formData.append("mode", mode);

      const response = await fetch(`${API_URL}/api/resume/compare`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Resume analysis failed.");
      }

      setResult(data);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the backend. Check that Flask is running."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="resume-page">
      <section className="resume-hero">
        <p className="resume-eyebrow">CAREER INTELLIGENCE</p>
        <h1>Resume Analyzer</h1>
        <p>
          Discover your matching skills, missing skills, and readiness for
          your target role.
        </p>
      </section>

      <form className="resume-form" onSubmit={handleAnalyze}>
        <label htmlFor="resume-file">Upload your resume (PDF)</label>
        <input
          id="resume-file"
          type="file"
          accept=".pdf,application/pdf"
          onChange={handleFileChange}
        />

        {resume && <p className="resume-file-name">{resume.name}</p>}

        <label htmlFor="target-role">Target job role</label>
        <input
          id="target-role"
          type="text"
          placeholder="e.g. Python Developer"
          value={role}
          onChange={(event) => setRole(event.target.value)}
        />

        <label htmlFor="search-mode">Job market</label>
        <select
          id="search-mode"
          value={mode}
          onChange={(event) => setMode(event.target.value)}
        >
          <option value="india">India</option>
          <option value="international">International</option>
          <option value="both">India and International</option>
        </select>

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing resume..." : "Analyze Resume"}
        </button>

        {loading && (
          <p className="resume-status">
            Fetching job postings and comparing skills. This may take a little
            time.
          </p>
        )}

        {error && <p className="resume-error">{error}</p>}
      </form>

      {result && (
        <section className="resume-results">
          <h2>Your Analysis Results</h2>
          <p>
            Target role: <strong>{result.role}</strong>
          </p>
          <p>
            Jobs analyzed: <strong>{result.total_jobs_analyzed}</strong>
          </p>

          <div className="resume-score">
            <span>Role readiness</span>
            <strong>{result.readiness_score}%</strong>
          </div>

          <div className="resume-result-grid">
            <article>
              <h3>Matching Skills ({result.matched_count})</h3>
              {result.matching_skills?.length ? (
                <ul>
                  {result.matching_skills.map((skill) => (
                    <li key={skill}>{skill}</li>
                  ))}
                </ul>
              ) : (
                <p>No matching skills detected.</p>
              )}
            </article>

            <article>
              <h3>Skills to Improve ({result.missing_skills?.length})</h3>
              {result.missing_skills?.length ? (
                <ul>
                  {result.missing_skills.map((skill) => (
                    <li key={skill}>{skill}</li>
                  ))}
                </ul>
              ) : (
                <p>No missing skills detected.</p>
              )}
            </article>
          </div>

          <details>
            <summary>View skills detected in your resume</summary>
            {result.resume_skills?.length ? (
              <ul>
                {result.resume_skills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>No skills were detected.</p>
            )}
          </details>
        </section>
      )}
    </main>
  );
}

