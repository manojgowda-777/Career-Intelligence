
import Link from "next/link";

function TargetIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <circle cx="12" cy="12" r="9" />
      <circle cx="12" cy="12" r="5" />
      <circle cx="12" cy="12" r="1" />
      <path d="M16.5 7.5 21 3m-4 0h4v4" />
    </svg>
  );
}

function BriefcaseIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <rect x="3" y="7" width="18" height="14" rx="2" />
      <path d="M8 7V4h8v3M3 12h18M10 12v2h4v-2" />
    </svg>
  );
}

function ArrowIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M5 12h14m-6-6 6 6-6 6" />
    </svg>
  );
}
function SparkIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M12 3 14.5 9.5 21 12l-6.5 2.5L12 21l-2.5-6.5L3 12l6.5-2.5L12 3Z" />
      <path d="m19 2 .8 2.2L22 5l-2.2.8L19 8l-.8-2.2L16 5l2.2-.8L19 2Z" />
    </svg>
  );
}

function CareerIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <circle cx="12" cy="12" r="9" />
      <path d="m15.8 8.2-2.5 5.1-5.1 2.5 2.5-5.1 5.1-2.5Z" />
      <circle cx="12" cy="12" r="1" />
    </svg>
  );
}


function CareerCard({ icon, number, title, description, features, href }) {
  return (
    <article className="career-card">
      <div className="card-top">
        <div className="card-icon">{icon}</div>
        <span className="card-number">{number}</span>
      </div>

      <h2>{title}</h2>
      <p className="card-description">{description}</p>

      <ul className="feature-list">
        {features.map((feature) => (
          <li key={feature}>
            <span className="check-mark">✓</span>
            {feature}
          </li>
        ))}
      </ul>

      <Link className="card-link" href={href}>
        <span>Get started</span>
        <span className="arrow-icon">
          <ArrowIcon />
        </span>
      </Link>
    </article>
  );
}

export default function Home() {
  return (
    <main className="home-page">
      <section className="hero">
        <div className="eyebrow">
          CAREER DEVELOPMENT PLATFORM
        </div>

        <h1>
          Turn your career goals
          <br />
          into <span className="heading-highlight">real opportunities.</span>
        </h1>

        <p className="hero-description">
          Discover your skills, explore careers, and find your next opportunity.
        </p>
        
        <div className="hero-note">
          <span className="note-icon"><SparkIcon /></span>
          <span>Know your skills. Find your direction. Move forward.</span>
        </div>
      </section>

      <section className="choice-section">
        <div className="section-heading">
          <div>
            <p className="section-label">GET STARTED</p>
            <h2>What would you like to explore?</h2>
          </div>
          <p className="section-hint">Choose a path to begin</p>
        </div>

        <div className="career-grid">
          <CareerCard
            icon={<TargetIcon />}
            number="01"
            title="Search for Roles"
            description="Discover the skills your dream role requires."
            features={[
              "Explore required skills",
              "Take skill-based MCQs",
              "Analyze your resume",
            ]}

            href="/roles"
          />

          <CareerCard
            icon={<BriefcaseIcon />}
            number="02"
            title="Search for Jobs"
            description="Find opportunities that match your career goals."
            features={[
              "Search jobs worldwide",
              "Explore job openings",
              "Check your resume match",
            ]}
            href="/jobs"
          />
        </div>
      </section>

      <footer className="page-footer">
        <span className="footer-brand">Career Intelligence</span>
        <span>Make your next career move with confidence.</span>
      </footer>
    </main>
  );
}
