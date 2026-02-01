#!/usr/bin/env python3
"""
Script to display beginner-friendly issues from the pytest GitHub repository.

This script fetches and displays issues tagged with labels that indicate they are
suitable for beginners, such as "status: easy" or "good first issue".

Usage:
    python scripts/show-beginner-issues.py
    python scripts/show-beginner-issues.py --max 20 --verbose
    python scripts/show-beginner-issues.py --state all

Optional: Set GITHUB_TOKEN environment variable to increase API rate limits.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Any


try:
    import requests
except ImportError:
    print("Error: 'requests' library is required. Install it with: pip install requests")
    sys.exit(1)


GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "pytest-dev"
REPO_NAME = "pytest"
BEGINNER_LABELS = ["status: easy", "good first issue"]


def fetch_beginner_issues(
    state: str = "open", max_results: int = 10
) -> list[dict[str, Any]]:
    """
    Fetch beginner-friendly issues from the GitHub repository.

    Args:
        state: Issue state filter ('open', 'closed', or 'all')
        max_results: Maximum number of issues to retrieve

    Returns:
        List of issue dictionaries
    """
    all_issues = []

    # Get GitHub token from environment if available
    headers = {}
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    for label in BEGINNER_LABELS:
        url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
        params: dict[str, str | int] = {
            "labels": label,
            "state": state,
            "per_page": max_results,
            "sort": "created",
            "direction": "desc",
        }

        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            issues = response.json()

            # Filter out pull requests (GitHub API returns PRs as issues)
            issues = [issue for issue in issues if "pull_request" not in issue]

            all_issues.extend(issues)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print(
                    "Warning: GitHub API rate limit reached. "
                    "Set GITHUB_TOKEN environment variable to increase limits.",
                    file=sys.stderr,
                )
                # Continue trying other labels
                continue
            else:
                print(f"Error fetching issues with label '{label}': {e}", file=sys.stderr)
                continue
        except requests.exceptions.RequestException as e:
            print(f"Error fetching issues with label '{label}': {e}", file=sys.stderr)
            continue

    # Remove duplicates (issues with multiple beginner labels)
    seen = set()
    unique_issues = []
    for issue in all_issues:
        if issue["number"] not in seen:
            seen.add(issue["number"])
            unique_issues.append(issue)

    # Sort by creation date (newest first) and limit to max_results
    unique_issues.sort(key=lambda x: x["created_at"], reverse=True)
    return unique_issues[:max_results]


def display_issues(issues: list[dict[str, Any]], verbose: bool = False) -> None:
    """
    Display issues in a formatted way.

    Args:
        issues: List of issue dictionaries
        verbose: Whether to show detailed information
    """
    if not issues:
        print("No beginner-friendly issues found.")
        return

    print(f"\n{'=' * 80}")
    print(f"初心者向けIssue (Beginner-Friendly Issues): {len(issues)} found")
    print(f"{'=' * 80}\n")

    for i, issue in enumerate(issues, 1):
        title = issue["title"]
        number = issue["number"]
        url = issue["html_url"]
        labels = [label["name"] for label in issue["labels"]]
        created_at = issue["created_at"].split("T")[0]

        print(f"{i}. #{number}: {title}")
        print(f"   URL: {url}")
        print(f"   Created: {created_at}")
        print(f"   Labels: {', '.join(labels)}")

        if verbose and issue.get("body"):
            body = issue["body"][:200]
            if len(issue["body"]) > 200:
                body += "..."
            print(f"   Description: {body}")

        print()


def main() -> None:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Display beginner-friendly issues from the pytest GitHub repository"
    )
    parser.add_argument(
        "--state",
        choices=["open", "closed", "all"],
        default="open",
        help="Filter issues by state (default: open)",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="Maximum number of issues to display (default: 10)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed information including issue descriptions",
    )

    args = parser.parse_args()

    print("Fetching beginner-friendly issues...")
    issues = fetch_beginner_issues(state=args.state, max_results=args.max)
    display_issues(issues, verbose=args.verbose)


if __name__ == "__main__":
    main()
