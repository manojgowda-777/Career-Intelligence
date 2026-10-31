
"use client";

import { useState } from "react";

const API_URL = "http://127.0.0.1:5001";

export default function GitHubAnalyzerPage() {
  const [username, setUsername] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleAnalyze(event) {
    event.preventDefault();

    if (!username.trim()) {
      setError("Please enter a GitHub username.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/api/github/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username.trim() }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Unable to analyze this GitHub profile.");
      }

      setResult(data);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect. Make sure the GitHub Analyzer backend is running."
      );
    } finally {
      setLoading(false);
    }
  }

  const breakdown = result?.score?.breakdown
    ? Object.entries(result.score.breakdown)
    : [];

  const totalStars = result?.repositories?.reduce(
    (total, repo) => total + (repo.stars || 0),
    0
  ) ?? 0;

  const languages = new Set(
    (result?.repositories || [])
      .map((repo) => repo.language)
      .filter(Boolean)
  ).size;

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900 px-4 py-10 text-white sm:px-6 lg:px-8">
      <div className="mx-auto max-w-6xl">
        <header className="mb-8">
          <p className="mb-3 text-sm font-semibold uppercase tracking-wider text-blue-300">
            Career Intelligence
          </p>

          <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
            GitHub Analyzer
          </h1>

          <p className="mt-3 max-w-2xl leading-7 text-slate-300">
            Analyze a public GitHub profile, explore repositories, and discover
            an explainable profile score out of 100.
          </p>
        </header>

        <section className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur-sm sm:p-7">
          <form
            onSubmit={handleAnalyze}
            className="flex flex-col gap-4 sm:flex-row sm:items-end"
          >
            <div className="flex-1">
              <label
                htmlFor="github-username"
                className="mb-2 block text-sm font-semibold"
              >
                GitHub username
              </label>

              <input
                id="github-username"
                type="text"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                placeholder="e.g. octocat"
                autoComplete="off"
                className="w-full rounded-xl border border-white/15 bg-slate-900/70 px-4 py-3 text-white outline-none placeholder:text-slate-400 transition focus:border-blue-400 focus:ring-2 focus:ring-blue-400/20"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? "Analyzing..." : "Analyze GitHub"}
            </button>
          </form>

          {error && (
            <p
              role="alert"
              className="mt-4 rounded-xl border border-red-400/30 bg-red-500/10 p-3 text-sm text-red-200"
            >
              {error}
            </p>
          )}
        </section>

        {loading && (
          <div className="mt-6 rounded-2xl border border-white/10 bg-white/5 p-6 text-center text-slate-200">
            Fetching GitHub profile and repository information...
          </div>
        )}

        {result && (
          <section className="mt-8 space-y-6">
            <div className="rounded-2xl border border-white/10 bg-white/5 p-6 shadow-lg backdrop-blur-sm">
              <div className="flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between">
                <div>
                  <h2 className="text-2xl font-bold">
                    {result.name || result.username}
                  </h2>

                  <p className="mt-1 text-slate-300">@{result.username}</p>

                  <a
                    href={result.profile_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="mt-3 inline-block font-medium text-blue-300 transition hover:text-blue-200"
                  >
                    View GitHub profile ↗
                  </a>
                </div>

                <div className="flex h-28 w-28 flex-col items-center justify-center rounded-full border-4 border-blue-400/60 bg-blue-500/10">
                  <span className="text-3xl font-bold">
                    {result.score.score}
                  </span>
                  <span className="text-sm text-slate-300">out of 100</span>
                </div>
              </div>
            </div>

            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
              <StatCard
                label="Public repositories"
                value={result.public_repositories}
              />
              <StatCard
                label="Repositories analyzed"
                value={result.repositories_analyzed}
              />
              <StatCard label="Total stars" value={totalStars} />
              <StatCard label="Languages detected" value={languages} />
            </div>

            <div className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur-sm sm:p-7">
              <h2 className="text-xl font-bold">Score breakdown</h2>

              <p className="mt-2 text-sm leading-6 text-slate-300">
                This is our own score based on available public profile signals.
                It is not an official GitHub rating or a direct measurement of
                programming ability.
              </p>

              <div className="mt-6 space-y-5">
                {breakdown.map(([name, metric]) => (
                  <div key={name}>
                    <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
                      <span className="font-medium">{name}</span>
                      <span className="text-sm text-blue-200">
                        {metric.score} / {metric.maximum}
                      </span>
                    </div>

                    <div className="h-2 overflow-hidden rounded-full bg-white/10">
                      <div
                        className="h-full rounded-full bg-blue-400 transition-all"
                        style={{
                          width: `${Math.min(
                            100,
                            (metric.score / metric.maximum) * 100
                          )}%`,
                        }}
                      />
                    </div>

                    <p className="mt-2 text-sm leading-6 text-slate-200">
                      {metric.details}
                    </p>
                  </div>
                ))}
              </div>
            </div>

            <div className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur-sm sm:p-7">
              <div className="mb-5">
                <h2 className="text-xl font-bold">Public repositories</h2>
                <p className="mt-2 text-sm text-slate-300">
                  Review repository details and open projects on GitHub.
                </p>
              </div>

              <div className="space-y-3">
                {result.repositories.map((repo) => (
                  <article
                    key={repo.url}
                    className="rounded-xl border border-white/10 bg-slate-900/40 p-4 transition hover:border-blue-400/40 hover:bg-white/5"
                  >
                    <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                      <div className="min-w-0">
                        <a
                          href={repo.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="break-words font-semibold text-blue-300 hover:text-blue-200"
                        >
                          {repo.name}
                        </a>

                        <p className="mt-2 text-sm leading-6 text-slate-200">
                          {repo.language || "Language not specified"}
                          {" · "}
                          {repo.stars} stars
                          {" · "}
                          {repo.has_readme
                            ? "README available"
                            : "No README detected"}
                        </p>
                      </div>

                      {repo.homepage && (
                        <a
                          href={repo.homepage}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="shrink-0 text-sm font-semibold text-emerald-300 hover:text-emerald-200"
                        >
                          Project website ↗
                        </a>
                      )}
                    </div>
                  </article>
                ))}
              </div>

              <p className="mt-5 rounded-xl border border-amber-300/20 bg-amber-400/10 p-4 text-sm leading-6 text-amber-100">
                {result.deployment_note}
              </p>
            </div>
          </section>
        )}
      </div>
    </main>
  );
}

function StatCard({ label, value }) {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-5 shadow-lg backdrop-blur-sm">
      <p className="text-sm text-slate-300">{label}</p>
      <p className="mt-2 text-3xl font-bold">{value}</p>
    </div>
  );
}
