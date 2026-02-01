# Scripts Directory

This directory contains various utility scripts for the pytest project.

## Show Beginner Issues Scripts

Two scripts are available to help newcomers find beginner-friendly issues:

### show-beginner-issues-simple.py

A simple, dependency-free script that displays links to beginner-friendly issues.

**Usage:**
```bash
python scripts/show-beginner-issues-simple.py
```

This script doesn't require any additional dependencies and simply displays helpful links to:
- Good first issues
- Easy issues
- Contributing guidelines

### show-beginner-issues.py

An advanced script that fetches and displays beginner-friendly issues directly from the GitHub API.

**Requirements:**
- Python 3.10+
- `requests` library (install with: `pip install requests`)

**Usage:**
```bash
# Show 10 most recent open beginner-friendly issues
python scripts/show-beginner-issues.py

# Show 20 issues
python scripts/show-beginner-issues.py --max 20

# Show closed issues
python scripts/show-beginner-issues.py --state closed

# Show all issues (open and closed)
python scripts/show-beginner-issues.py --state all

# Show verbose output with issue descriptions
python scripts/show-beginner-issues.py --verbose
```

**Note:** To avoid GitHub API rate limits, you can set the `GITHUB_TOKEN` environment variable:
```bash
export GITHUB_TOKEN=your_github_token_here
python scripts/show-beginner-issues.py
```

## Other Scripts

- `update-plugin-list.py` - Updates the plugin list in documentation
- `generate-gh-release-notes.py` - Generates GitHub release notes
- `prepare-release-pr.py` - Prepares release pull requests
- `release.py` - Handles release processes
