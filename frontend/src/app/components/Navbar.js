
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="navbar">
      <Link href="/" className="brand">
        <span className="brand-icon">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <circle cx="12" cy="12" r="9" />
            <path d="m15.8 8.2-2.5 5.1-5.1 2.5 2.5-5.1 5.1-2.5Z" />
            <circle cx="12" cy="12" r="1" />
          </svg>
        </span>
        <span>
          Career<span className="brand-highlight"> Intelligence</span>
        </span>
      </Link>

      <div className="flex items-center gap-3">
        <Link href="/" className="nav-home">
          Home
        </Link>

        <Link
          href="/github-analyzer"
          className="nav-home"
        >
          GitHub Analyzer
        </Link>
      </div>
    </nav>
  );
}
