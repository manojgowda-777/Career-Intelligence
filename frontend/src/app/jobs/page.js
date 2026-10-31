
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const API_URL = "http://127.0.0.1:5000";

export default function JobsPage() {
  const [role, setRole] = useState("");
  const [mode, setMode] = useState("both");
  const [jobs, setJobs] = useState([]);
  const [searchedRole, setSearchedRole] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [hasSearched, setHasSearched] = useState(false);
  const [totalJobs, setTotalJobs] = useState(0);
  const router = useRouter();
  async function handleSearch(event) {
    event.preventDefault();

    if (!role.trim()) {
      setError("Please enter a job role.");
      return;
    }

    setLoading(true);
    setError("");
    setJobs([]);
    setTotalJobs(0);
    setHasSearched(false);
    setSearchedRole(role.trim());

    try {
      const response = await fetch(`${API_URL}/api/jobs/search`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          role: role.trim(),
          mode,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Unable to search for jobs.");
      }

      const results = Array.isArray(data.jobs) ? data.jobs : [];

      setJobs(results);
      setTotalJobs(
        typeof data.total_jobs === "number"
          ? data.total_jobs
          : results.length
      );
      setSearchedRole(data.role || role.trim());
      setHasSearched(true);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect to the backend. Make sure Flask is running."
      );
    } finally {
      setLoading(false);
    }
  }

  function getJobTitle(job) {
    return job.title || job.job_title || job.position || "Untitled position";
  }

  function getCompany(job) {
    return job.company || job.company_name || job.employer || "";
  }

  function getLocation(job) {
    const location =
      job.location ||
      job.locations ||
      job.location_restrictions ||
      "";

    if (Array.isArray(location)) {
      return location.join(", ");
    }

    if (typeof location === "object" && location !== null) {
      return Object.values(location).filter(Boolean).join(", ");
    }

    return String(location);
  }

  function getDescription(job) {
    const description =
      job.description ||
      job.summary ||
      job.excerpt ||
      "No description is available for this listing.";

    return String(description)
      .replace(/<[^>]*>/g, " ")
      .replace(/&nbsp;/gi, " ")
      .replace(/&amp;/gi, "&")
      .replace(/&lt;/gi, "<")
      .replace(/&gt;/gi, ">")
      .replace(/&#39;/gi, "'")
      .replace(/&quot;/gi, '"')
      .replace(/\s+/g, " ")
      .trim();
  }

  function getApplicationLink(job) {
    const link =
      job.application_link ||
      job.apply_url ||
      job.application_url ||
      job.url ||
      job.link ||
      "";

    if (typeof link !== "string") return "";

    try {
      const parsed = new URL(link);
      return ["http:", "https:"].includes(parsed.protocol) ? link : "";
    } catch {
      return "";
    }
  }

  function getJobSkills(job) {
    const skills = job.extracted_skills || job.skills || [];

    if (!Array.isArray(skills)) return [];

    return skills.filter((skill) => typeof skill === "string");
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900 px-4 py-10 text-white sm:px-6 lg:px-8">
      <div className="mx-auto max-w-6xl">
        <section className="mb-8">
          <p className="mb-3 text-sm font-semibold uppercase tracking-wider text-blue-300">
            Career Intelligence
          </p>

          <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Search for Jobs
          </h1>

          <p className="mt-3 max-w-2xl text-slate-300">
            Find job opportunities that match your target role. Explore
            available listings and follow their application links.
          </p>
        </section>

        <section className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur-sm sm:p-7">
          <form onSubmit={handleSearch} className="space-y-5">
            <div>
              <label
                htmlFor="job-role"
                className="mb-2 block text-sm font-semibold"
              >
                Target job role
              </label>

              <input
                id="job-role"
                type="text"
                value={role}
                onChange={(event) => setRole(event.target.value)}
                placeholder="e.g. Python Developer"
                className="w-full rounded-xl border border-white/15 bg-slate-900/70 px-4 py-3 text-white outline-none placeholder:text-slate-400 transition focus:border-blue-400 focus:ring-2 focus:ring-blue-400/20"
              />
            </div>

            <div>
              <label className="mb-3 block text-sm font-semibold">
                Search region
              </label>

              <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
                {[
                  { value: "india", label: "India" },
                  { value: "international", label: "International" },
                  { value: "both", label: "Both" },
                ].map((option) => (
                  <label
                    key={option.value}
                    className={`flex cursor-pointer items-center gap-3 rounded-xl border p-4 transition ${
                      mode === option.value
                        ? "border-blue-400 bg-blue-500/30 text-white"
                        : "border-white/20 text-slate-200 hover:border-blue-400/60"
                    }`}
                  >
                    <input
                      type="radio"
                      name="search-region"
                      value={option.value}
                      checked={mode === option.value}
                      onChange={() => setMode(option.value)}
                      className="accent-blue-600"
                    />
                    <span className="text-sm font-medium">
                      {option.label}
                    </span>
                  </label>
                ))}
              </div>
            </div>

            <div className="flex flex-col gap-3 sm:flex-row">
                <button
                    type="submit"
                    disabled={loading}
                    className="flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-5 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
                >
                    {loading ? (
                    <>
                        <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent" />
                        Searching jobs...
                    </>
                    ) : (
                    <>
                        <span aria-hidden="true">⌕</span>
                        Search Jobs
                    </>
                    )}
                </button>

                <button
                    type="button"
                    onClick={() =>
                    router.push(
                        `/resume?role=${encodeURIComponent(searchedRole || role.trim())}`
                    )
                    }
                    className="flex items-center justify-center gap-2 rounded-xl border border-purple-300/30 bg-purple-500/20 px-5 py-3 font-semibold text-white transition hover:bg-purple-500/30"
                >
                    Analyze Resume
                </button>
            </div>
          </form>
        </section>

        {error && (
          <div
            role="alert"
            className="mt-6 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-700"
          >
            {error}
          </div>
        )}

        {loading && (
          <div className="mt-8 rounded-xl border border-slate-200 bg-white p-8 text-center">
            <p className="font-medium">Finding job opportunities...</p>
            <p className="mt-2 text-sm text-slate-500">
              This may take a little time while current listings are collected.
            </p>
          </div>
        )}

        {!loading && hasSearched && (
          <section className="mt-8">
            <div className="mb-5 flex flex-col justify-between gap-2 sm:flex-row sm:items-center">
              <div>
                <h2 className="text-xl font-bold">
                  Results for {searchedRole}
                </h2>
                <p className="mt-1 text-sm text-slate-600">
                  Region:{" "}
                  {mode === "both"
                    ? "India and international"
                    : mode === "india"
                      ? "India"
                      : "International"}
                </p>
              </div>

              <span className="text-sm font-medium text-slate-600">
                {totalJobs} {totalJobs === 1 ? "job" : "jobs"} found
              </span>
            </div>

            {jobs.length === 0 ? (
              <div className="rounded-2xl border border-slate-200 bg-white p-8 text-center">
                <h3 className="font-semibold">No jobs found</h3>
                <p className="mt-2 text-sm text-slate-600">
                  Try another job role or change the search region.
                </p>
              </div>
            ) : (
              <div className="space-y-4">
                {jobs.map((job, index) => {
                  const title = getJobTitle(job);
                  const company = getCompany(job);
                  const location = getLocation(job);
                  const description = getDescription(job);
                  const applicationLink = getApplicationLink(job);
                  const skills = getJobSkills(job);

                  return (
                    <article
                      key={
                        job.id ||
                        job.application_link ||
                        job.url ||
                        `${title}-${company}-${index}`
                      }
                      className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg transition hover:border-blue-400/40 hover:bg-white/10 sm:p-6"
                    >
                      <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                        <div className="min-w-0 flex-1">
                          <h3 className="text-lg font-bold">{title}</h3>

                          {company && (
                            <p className="mt-1 text-sm font-medium text-slate-200">
                              {company}
                            </p>
                          )}

                          {location && (
                            <p className="mt-2 text-sm text-slate-400">
                              <span aria-hidden="true">⌖ </span>
                              {location}
                            </p>
                          )}

                          {job.employment_type && (
                            <span className="mt-3 inline-block rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-700">
                              {job.employment_type}
                            </span>
                          )}
                        </div>

                        {applicationLink ? (
                          <a
                            href={applicationLink}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="inline-flex shrink-0 items-center justify-center rounded-lg bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700"
                          >
                            Apply Now ↗
                          </a>
                        ) : (
                          <span className="shrink-0 text-sm text-slate-500">
                            Application link unavailable
                          </span>
                        )}
                      </div>

                      <p className="mt-4 whitespace-pre-line break-words text-sm leading-6 text-slate-200">
                        {description.length > 500
                          ? `${description.slice(0, 500)}...`
                          : description}
                      </p>

                      {skills.length > 0 && (
                        <div className="mt-4">
                          <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">
                            Skills
                          </p>

                          <div className="flex flex-wrap gap-2">
                            {skills.slice(0, 12).map((skill) => (
                              <span
                                key={skill}
                                className="rounded-full border border-blue-300/20 bg-blue-400/15 px-3 py-1 text-xs font-medium text-blue-200"
                              >
                                {skill}
                              </span>
                            ))}
                          </div>
                        </div>
                      )}

                      {job.source && (
                        <p className="mt-4 text-xs text-slate-400">
                          Source: {job.source}
                        </p>
                      )}
                    </article>
                  );
                })}
              </div>
            )}
          </section>
        )}
      </div>
    </main>
  );
}
