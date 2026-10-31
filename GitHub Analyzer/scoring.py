
def calculate_github_score(profile, repositories):
    """
    Calculate a transparent GitHub profile score out of 100.
    This is our own score, not an official GitHub rating.
    """

    # 1. Project portfolio: 25 points
    repo_count = len(repositories)
    portfolio_points = min(repo_count / 10, 1) * 25

    # 2. Documentation: 20 points
    readme_count = sum(
        1 for repo in repositories
        if repo.get("has_readme", False)
    )
    documentation_points = (
        readme_count / repo_count * 20 if repo_count else 0
    )

    # 3. Community recognition: 15 points
    total_stars = sum(
        repo.get("stargazers_count", 0) for repo in repositories
    )
    community_points = min(total_stars / 50, 1) * 15

    # 4. Development activity: 20 points
    # Use public repository update dates as a simple activity indicator.
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc)
    recent_repositories = 0

    for repo in repositories:
        updated_at = repo.get("pushed_at")

        if updated_at:
            try:
                updated = datetime.fromisoformat(
                    updated_at.replace("Z", "+00:00")
                )
                if (now - updated).days <= 180:
                    recent_repositories += 1
            except (ValueError, TypeError):
                pass

    activity_points = (
        min(recent_repositories / 5, 1) * 20
    )

    # 5. Language diversity: 10 points
    languages = {
        repo.get("language")
        for repo in repositories
        if repo.get("language")
    }
    language_points = min(len(languages) / 5, 1) * 10

    # 6. Profile completeness: 10 points
    profile_fields = [
        profile.get("bio"),
        profile.get("blog"),
        profile.get("location"),
        profile.get("name"),
    ]
    completed_fields = sum(bool(value) for value in profile_fields)
    profile_points = completed_fields / len(profile_fields) * 10

    breakdown = {
        "Project portfolio": {
            "score": round(portfolio_points, 1),
            "maximum": 25,
            "details": f"{repo_count} public repositories",
        },
        "Documentation": {
            "score": round(documentation_points, 1),
            "maximum": 20,
            "details": f"{readme_count} repositories marked with README",
        },
        "Community recognition": {
            "score": round(community_points, 1),
            "maximum": 15,
            "details": f"{total_stars} total stars",
        },
        "Development activity": {
            "score": round(activity_points, 1),
            "maximum": 20,
            "details": f"{recent_repositories} repositories updated in the last 180 days",
        },
        "Language diversity": {
            "score": round(language_points, 1),
            "maximum": 10,
            "details": f"{len(languages)} programming languages detected",
        },
        "Profile completeness": {
            "score": round(profile_points, 1),
            "maximum": 10,
            "details": f"{completed_fields} of 4 profile fields completed",
        },
    }

    total_score = round(
        sum(item["score"] for item in breakdown.values())
    )

    return {
        "score": total_score,
        "maximum_score": 100,
        "breakdown": breakdown,
    }
