
import requests

GITHUB_API = "https://api.github.com"


def get_github_profile(username):
    """Fetch a public GitHub profile and its public repositories."""

    username = username.strip()

    if not username:
        raise ValueError("Please enter a GitHub username.")

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Career-Intelligence-GitHub-Analyzer",
    }

    profile_url = f"{GITHUB_API}/users/{username}"
    profile_response = requests.get(
        profile_url, headers=headers, timeout=15
    )

    if profile_response.status_code == 404:
        raise ValueError("GitHub username not found.")

    if profile_response.status_code == 403:
        raise RuntimeError(
            "GitHub API rate limit reached. Please try again later."
        )

    profile_response.raise_for_status()
    profile = profile_response.json()

    repositories = []
    page = 1

    while page <= 10:
        repo_response = requests.get(
            f"{GITHUB_API}/users/{username}/repos",
            headers=headers,
            params={
                "per_page": 100,
                "page": page,
                "type": "owner",
                "sort": "updated",
            },
            timeout=15,
        )

        if repo_response.status_code == 403:
            raise RuntimeError(
                "GitHub API rate limit reached. Please try again later."
            )

        repo_response.raise_for_status()
        batch = repo_response.json()

        if not batch:
            break

        repositories.extend(batch)

        if len(batch) < 100:
            break

        page += 1

    return {
        "profile": profile,
        "repositories": repositories,
    }
