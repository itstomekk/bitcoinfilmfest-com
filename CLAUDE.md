# Agent operating rules — Bitcoin FilmFest website

Every AI agent working in this repository follows these rules. They apply on top of `BUILDER-GUIDE.md`.

## 1. Read the knowledge base first

Before changing anything, read in this order:

1. `BUILDER-GUIDE.md` — ownership map and rules that must not regress.
2. `HANDOFF-CURRENT.md` — current state and "Pick up here".
3. `ORGANISATION-LOG.md` — the latest entries (what happened recently, who is doing what).
4. `site/README.md` and `site/design.md` — editing and design rules.
5. `PLAN-WEBSITE-ROADMAP.md` and `BUILD-LOG.md` — roadmap and verified milestones.
6. `docs/PUBLIC-REPO-SAFETY.md` — what must never be committed.

When documents disagree: `BUILDER-GUIDE.md`, `site/README.md`, the actual source files, and `BUILD-LOG.md` win. `HANDOFF.md`, `HANDOFF-SESSION-2.md`, and `HANDOFF-SESSION-3.md` are history only.

## 2. Changes go through pull requests

- Never push to `main`. Work on a branch, then open a pull request.
- One branch = one focused change.
- Any change under `site/` needs a dated entry in `CHANGELOG.md` (`## YYYY-MM-DD — Title`), or the PR check fails.
- This repo (`Nomishka/bitcoinfilmfest-com-fork`) is a fork of `itstomekk/bitcoinfilmfest-com`. Open the PR into the fork's `main` first; Nomishka then sends it upstream to Tomek (see `docs/GITHUB-GUIDE-NOMISHKA.md`).
- Run `python3 scripts/check-public-repo.py` and `git diff --check` before every commit.
- Build and check the site before pushing: see the sandbox build steps under "Gotchas" in `HANDOFF-CURRENT.md`. If the build cannot run, say so in the PR and rely on the PR check.

## 3. Always log and hand off

At the end of every session, before the final push:

1. Add a dated entry at the top of `ORGANISATION-LOG.md`: what was done, the PR link, what is open, who needs to act next.
2. Update `HANDOFF-CURRENT.md` if the project state changed (and its "Pick up here" prompt).
3. Add a `BUILD-LOG.md` entry for any verified website milestone.

Logs are public. Never write private contacts, CRM notes, credentials, private links, or unverified claims into them.

## 4. Guide Nomishka through GitHub

Nomishka is a team member, not a developer. After opening a PR, always explain in plain words:

- the PR link and what it changes (2–3 bullets);
- exactly what to click next (review → merge into the fork → open the upstream PR to Tomek), pointing to the matching step in `docs/GITHUB-GUIDE-NOMISHKA.md`;
- what to check on the page before approving.

Keep instructions short and step-by-step. Never ask Nomishka to use the command line.
