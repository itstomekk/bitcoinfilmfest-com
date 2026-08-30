# Collaborating safely through GitHub

This public repository is the shared website source. Your friend can propose and review changes without receiving access to your computer, OneDrive folders, Git credentials, or any production deployment secret.

## Recommended workflow

1. Invite your friend as a **Write** collaborator in the GitHub repository settings, or have them fork the repository if you prefer no direct write access.
2. They create a branch with a clear name, for example `friend/homepage-copy`.
3. They make their changes and open a Pull Request (PR) into `main`.
4. GitHub automatically runs **Pull request safety and preview build**.
5. Review the Files changed tab together. The check must be green before merge.
6. Download the `bff-preview-pr-...` artifact from the PR Checks tab if you need the exact built static files before merge.
7. Merge only after review. `main` is the only branch that deploys to the public GitHub Pages site.

## What GitHub checks before review

The PR workflow runs with read-only permissions and no secrets. It:

- scans tracked repository files for common credential formats and forbidden local/build paths;
- builds the site with the same temporary GitHub Pages URL settings as production;
- checks the generated crawler files, favicon, manifest, sitemap, and default social image;
- uploads a downloadable, seven-day preview artifact; and
- cannot deploy or change the live site.

A GitHub Pages project site has one public deployment target. It cannot safely provide separate hosted URLs for each PR without replacing the production site. If you want a clickable hosted preview link for every PR, connect the repository to **Netlify** or **Cloudflare Pages** later. Both support pull-request preview deployments while GitHub Pages remains the production site.

## Local file and credential boundaries

- Never place a password, API key, private movie database, contact export, private licensing document, or credential in this repository.
- Keep sensitive values in GitHub Actions secrets only when a future build integration genuinely needs them. The current site requires no deployment secrets.
- `.gitignore` prevents accidental new commits, but it cannot hide a file already committed in Git history.
- The PR safety check reads only files Git tracks. It does not read your OneDrive, home directory, browser profile, Git credential manager, or ignored files.
- Before committing locally, run:

  ```bash
  python scripts/check-public-repo.py
  git status --short
  ```

## Before merging a PR

- Confirm the PR contains only the intended files.
- Confirm the green safety/build check.
- Open the generated preview artifact or run the local Jekyll build.
- Merge to `main` only when the page copy, images, links, and SEO metadata look right.

## Suggested GitHub repository settings

Enable these in **Settings -> Branches** for `main` once collaborators start using PRs:

- Require a pull request before merging.
- Require one approving review.
- Require the `Public-safe Pages preview build` status check to pass.
- Require conversation resolution before merging.
- Do not allow force pushes.

GitHub may restrict some branch-protection options by account plan. If so, keep the human rule: no direct pushes to `main`; use a PR and wait for the check.
