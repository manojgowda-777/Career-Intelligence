
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function RolesPage() {
  const router = useRouter();
  const [role, setRole] = useState("");
  const [searchedRole, setSearchedRole] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [skills, setSkills] = useState([]);

  async function handleSearch(event) {
    event.preventDefault();

    const selectedRole = role.trim();
    if (!selectedRole) {
      setError("Please enter a job role first.");
      return;
    }

    setLoading(true);
    setError("");
    setSkills([]);
    setSearchedRole(selectedRole);

    try {
      const response = await fetch("http://127.0.0.1:5000/api/role/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
        role: selectedRole,
        mode: "both",
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
            data.error || data.message || "Unable to search this role."
        );
        }

        const results = Array.isArray(data.skills) ? data.skills : [];

      if (!results.length) {
        setError("No skills were returned for this role. Try another role.");
      } else {
        setSkills(results);
      }
    
    } catch (err) {
      setError(err.message || "Unable to complete the role search.");
    } finally {
      setLoading(false);
    }

  }

  return (
    <main className="roles-page">
      <section className="roles-heading">
        <div className="roles-eyebrow">
          <span className="roles-eyebrow-dot" />
          CAREER SKILL ASSESSMENT
        </div>

        <h1>
          Discover the skills
          <br />
          <span>your next role demands.</span>
        </h1>

        <p>
          Enter a job role to discover the most demanded skills in the job
          market and understand what employers are looking for.
        </p>
      </section>

      <section className="roles-search-card">
        <form onSubmit={handleSearch}>
          <label htmlFor="role">Which role are you targeting?</label>

          <div className="roles-input-row">
            <input
              id="role"
              type="text"
              value={role}
              onChange={(event) => setRole(event.target.value)}
              placeholder="e.g. Full Stack Developer, Data Analyst..."
            />

            <button type="submit" disabled={loading}>
              {loading ? "Searching..." : "Search Role"}
              {!loading && <span aria-hidden="true"> →</span>}
            </button>
          </div>

          <div className="roles-hint">
            <span>✦</span> Skills are based on job-market data.
          </div>
        </form>

        <div className="roles-suggestions">
          <span>Popular searches</span>
          {["Full Stack Developer", "Data Analyst", "Python Developer"].map(
            (item) => (
              <button
                key={item}
                type="button"
                onClick={() => setRole(item)}
              >
                {item}
              </button>
            )
          )}
        </div>
      </section>

      {error && <p className="roles-error">{error}</p>}

      {skills.length > 0 && (
        <section className="roles-results">
          <div className="roles-results-heading">
            <div>
              <span className="roles-section-label">ROLE ANALYSIS</span>
              <h2>Skills for {searchedRole}</h2>
              <p>Here are the top skills identified for this role.</p>
            </div>
            <span className="roles-result-count">
              {skills.length} skills
            </span>
          </div>

          <div className="roles-skills-grid">
            {skills.map((item, index) => {
              const name = typeof item === "string" ? item : item.skill || item.name;
              const demand = typeof item === "string" ? null : item.demand_percentage;

              return (
                <article className="roles-skill-card" key={name || index}>
                  <div className="roles-skill-top">
                    <span className="roles-skill-number">
                      {String(index + 1).padStart(2, "0")}
                    </span>
                    <span className="roles-skill-symbol">✦</span>
                  </div>
                  <h3>{name}</h3>
                  <div className="roles-skill-bottom">
                    <span>Market demand</span>
                    <strong>
                      {demand !== undefined && demand !== null
                        ? `${Math.round(Number(demand))}%`
                        : "Identified"}
                    </strong>
                  </div>
                  {demand !== undefined && demand !== null && (
                    <div className="roles-demand-track">
                      <div
                        className="roles-demand-fill"
                        style={{
                          width: `${Math.max(0, Math.min(100, Number(demand)))}%`,
                        }}
                      />
                    </div>
                  )}
                </article>
              );
            })}
          </div>

          <div className="roles-next-step">
            <div>
              <span className="roles-section-label">YOUR NEXT STEP</span>
              <h2>Ready to check your skills?</h2>
              <p>Test your knowledge or find skill gaps in your resume.</p>
            </div>

            <div className="roles-actions">
              <button
                type="button"
                onClick={() => {
                    const skillNames = skills
                    .map((item) =>
                        typeof item === "string" ? item : item.skill || item.name
                    )
                    .filter(Boolean);

                    const params = new URLSearchParams({
                    role: searchedRole,
                    skills: skillNames.join(","),
                    });

                    router.replace(`/mcq?${params.toString()}`);
                    router.refresh();
                }}
              >
                Take MCQ Test <span>→</span>
              </button>
              <button
                type="button"
                className="roles-secondary-button"
                onClick={() =>
                  router.push(
                    `/resume?role=${encodeURIComponent(searchedRole)}`
                  )
                  }
              >
                Analyze Resume <span>↗</span>
              </button>
            </div>
          </div>
        </section>
      )}
    </main>
  );
}
