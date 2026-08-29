# Current handoff - Bitcoin FilmFest Jekyll rebuild

**Updated:** 2026-08-29  
**Repository:** https://github.com/itstomekk/bitcoinfilmfest-com  
**Temporary live site:** https://itstomekk.github.io/bitcoinfilmfest-com/  
**Deployment:** GitHub Actions deploys `main` to GitHub Pages.

This is the current practical handoff for future humans and agents. Start with this file, then read `README.md`, `BUILDER-GUIDE.md`, `site/README.md`, and `site/design.md`. Older `HANDOFF*.md` files are dated historical snapshots, not current instructions.

## What is deployed

- The Jekyll source is `site/`; the Git repository root also holds documentation and the Pages workflow.
- `.github/workflows/deploy-pages.yml` builds `site/` with Ruby 3.3 and deploys generated `site/_site/`.
- The repository is public. Never commit private data, passwords, API keys, mailing exports, contracts, or raw private film database exports.
- The custom domain is intentionally deferred. Do not add `CNAME` or change DNS until the owner explicitly asks.

## Current product decisions

- The cinema shell is shared across every route: top navigation, soft shadow bezel, framed canvas, fixed seats, and footer.
- The top perforation pattern was removed by design; retain the bezel shadow.
- Desktop Festivals opens on hover. Reel is intentionally a direct link, not a submenu. Only one disclosure may be open at a time.
- The current-page marker has an orange dot. Inactive menu items are deliberately dim; Contribute brightens only on hover or when it is the current page.
- Footer is a lifted charcoal canvas inside the outer dark cinema frame. It has subscription and compact accessible social icons only; it must not repeat primary navigation.
- Public human-readable sitemap route was removed. The migration inventory stays builder-only in `site/_data/sitemap.json` and `site/SITEMAP-PLAN.md`.

## Files people will edit most

| Need | Edit |
| --- | --- |
| Page text | Matching Markdown file in `site/` |
| Menu structure | `site/_data/navigation.yml` |
| Credits roster | `site/_data/credits.json` |
| Social destinations | `site/_config.yml` |
| Shared visual tokens | `site/tokens.css` |
| Shared components | `site/assets/css/cinema-frame.css` |
| Menu and soft-navigation behavior | `site/assets/js/main.js` |
| Credits motion | `site/assets/js/credits-roll.js` |

## Local/offline copy and Git workflow

The maintained offline copy is the Git clone at:

`C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll`

It contains the full source and full Git history. GitHub is the shared remote backup and collaboration point; it is not the only copy.

1. Before work: `git switch main` then `git pull --ff-only origin main`.
2. Make a branch for one coherent change: `git switch -c content/add-bff26-press`.
3. Edit only the needed files. Avoid simultaneous edits to the same data/template file without agreeing first.
4. Build locally from `site/`:
   `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`
5. Review desktop and mobile pages affected by the change.
6. Inspect exactly what will be published: `git diff --check`, `git status --short`.
7. Commit a clear focused message, for example: `Add BFF 2026 press coverage`.
8. Push the branch, open a pull request, review it, then merge to `main`.
9. GitHub Actions deploys only `main`; check the Actions run and the live page afterward.

For tiny, urgent spelling corrections, a trusted maintainer may push directly to `main` after a build. Branches and pull requests remain the default because they create a reviewable record and reduce accidental conflict.

## Backup practice

- Git history plus GitHub provides rollback for committed work.
- Before a major phase or visual redesign, tag a stable commit, for example `git tag -a phase-2-ready -m "Festival editions baseline"`, then push the tag.
- Keep original private source materials and large unreleased assets in separate backed-up storage or a private repository. Do not assume a public GitHub repo is a private archive.
- `.gitignore` stops new local files from being committed; it does not hide data already pushed.

## Rebuild roadmap

Follow `REBUILD-PHASES.md`. The next practical phase is archive triage: decide every old route's fate before bulk conversion. Then prioritise festival editions, Reel/archive material, and only later a private-source movie catalogue pipeline.

## Required verification before saying work is done

1. Normal Jekyll build passes.
2. GitHub Pages-equivalent build passes when deployment configuration changes.
3. Affected routes load locally at desktop and mobile widths.
4. Navigation, active state, and keyboard access still work.
5. No generated `_site/`, cache, dependency directories, secrets, or local-only files are staged.
6. After a production push, Actions is green and the exact live URL has been read back.
