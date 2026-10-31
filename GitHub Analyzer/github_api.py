
from flask import Flask, jsonify, request
from flask_cors import CORS
from github_client import get_github_profile
from scoring import calculate_github_score
import requests
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route("/api/github/analyze", methods=["POST"])
def analyze_github():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")

    try:
        result = get_github_profile(username)
        profile = result["profile"]
        repositories = result["repositories"]

        # GitHub's repository list doesn't include a has_readme field.
        # Check README availability for each repository.
        # Limit checks to avoid excessive API requests.
        for repo in repositories[:100]:
            repo["has_readme"] = False
            repo_name = repo.get("name")
            owner = (repo.get("owner") or {}).get("login", username)

            if repo_name:
                import requests

                response = requests.get(
                    f"https://api.github.com/repos/{owner}/{repo_name}/readme",
                    headers={
                        "Accept": "application/vnd.github+json",
                        "User-Agent": "Career-Intelligence-GitHub-Analyzer",
                    },
                    timeout=10,
                )
                if response.status_code == 200:
                    repo["has_readme"] = True

        score_result = calculate_github_score(profile, repositories)

        # Deployment cannot be reliably determined for every repository.
        deployment_note = (
            "GitHub does not reliably expose a deployed/undeployed status "
            "for every project. Deployment status is not verified in this version."
        )

        return jsonify({
            "username": profile.get("login"),
            "name": profile.get("name"),
            "profile_url": profile.get("html_url"),
            "public_repositories": profile.get("public_repos", 0),
            "repositories_analyzed": len(repositories),
            "repositories": [
                {
                    "name": repo.get("name"),
                    "url": repo.get("html_url"),
                    "stars": repo.get("stargazers_count", 0),
                    "language": repo.get("language"),
                    "has_readme": repo.get("has_readme", False),
                    "homepage": repo.get("homepage"),
                }
                for repo in repositories
            ],
            "deployment_note": deployment_note,
            "score": score_result,
        })

    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except requests.RequestException:
        return jsonify({
            "error": "Unable to reach GitHub. Please try again later."
        }), 502
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 429


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
