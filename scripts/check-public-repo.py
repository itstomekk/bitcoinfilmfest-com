#!/usr/bin/env python3
"""Fast, dependency-free safety gate for PRs and release builds.

Only tracked repository files are checked. It never reads a developer's home
folder, Git credentials, environment variables, or ignored local files. On a
match it prints the path and rule name, never the suspected secret value.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import PurePosixPath

tracked = subprocess.check_output(["git", "ls-files", "-z"], text=False).decode("utf-8").split("\0")
tracked = [path for path in tracked if path]

forbidden_paths = (
    "site/_site/",
    "site/vendor/",
    "site/.bundle/",
    ".env",
    "private/",
    "local/",
    ".secrets/",
)
secret_patterns = {
    "GitHub personal access token": re.compile(r"github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic assigned secret": re.compile(r"(?i)(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{12,}"),
}

failures: list[str] = []
for filename in tracked:
    path = PurePosixPath(filename)
    if any(filename == denied or filename.startswith(denied) for denied in forbidden_paths):
        failures.append(f"forbidden tracked path: {filename}")
        continue
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".woff", ".woff2"}:
        continue
    try:
        content = open(filename, "r", encoding="utf-8", errors="ignore").read()
    except OSError:
        failures.append(f"unreadable tracked file: {filename}")
        continue
    for label, pattern in secret_patterns.items():
        if pattern.search(content):
            failures.append(f"possible {label}: {filename}")

if failures:
    print("Safety check failed. Remove private material before opening or merging this PR:")
    print("\n".join(f"- {item}" for item in failures))
    sys.exit(1)

print(f"Safety check passed: {len(tracked)} tracked files scanned; no forbidden paths or common credentials found.")
