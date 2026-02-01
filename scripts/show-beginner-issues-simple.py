#!/usr/bin/env python3
"""
Simple CLI to display beginner-friendly issues from the pytest GitHub repository.

This is a minimal implementation that can work even without dependencies,
by providing instructions to view issues in the browser.
"""

from __future__ import annotations


def main() -> None:
    """Display instructions to view beginner-friendly issues."""
    print("=" * 80)
    print("初心者向けIssue (Beginner-Friendly Issues)")
    print("=" * 80)
    print()
    print("To view beginner-friendly issues for the pytest project, visit:")
    print()
    print("1. Good First Issues:")
    print("   https://github.com/pytest-dev/pytest/labels/good%20first%20issue")
    print()
    print("2. Easy Issues:")
    print("   https://github.com/pytest-dev/pytest/labels/status%3A%20easy")
    print()
    print("3. All Open Issues (to filter manually):")
    print("   https://github.com/pytest-dev/pytest/issues")
    print()
    print("=" * 80)
    print("Contributing Guide:")
    print("=" * 80)
    print()
    print("Before starting work on an issue:")
    print("1. Read CONTRIBUTING.rst in the repository")
    print("2. Comment on the issue to indicate you're working on it")
    print("3. Fork the repository and create a branch")
    print("4. Make your changes and submit a pull request")
    print()
    print("For more details, see:")
    print("https://docs.pytest.org/en/stable/contributing.html")
    print()


if __name__ == "__main__":
    main()
