# Organisation log — Bitcoin FilmFest website

Running, dated record of what is happening on the website work: who did what, which PR, what is open, who acts next. Newest entry first.

This file is **public**. Write no private contacts, CRM notes, credentials, private links, or unverified claims. The private organisation log on the team's own drive stays the place for private detail.

Entry template:

```text
## YYYY-MM-DD — Short title
- Who: person or agent
- Done: what changed
- PR: link
- Open / next: what is left and who acts next
```

---

## 2026-09-30 — Fork work redone on top of current upstream

- Who: Claude (agent), asked by Nomishka.
- Done: Nomishka reset the fork's `main` to match upstream because the earlier fork commits (PRs 5 and 6) conflicted with it. The same changes were reapplied on a fresh branch from current upstream `main`: Pages base-path fix, Cloudflare preview config (`wrangler.jsonc`, `scripts/cloudflare-build.sh`, `.ruby-version`), `CLAUDE.md`, this log, the GitHub guide, and handoff/build-log notes. `CHANGELOG.md` got a new top entry; upstream entries are untouched.
- PR: new PR into the fork's `main` (see the fork's pull requests).
- Open / next: Nomishka reviews and merges. After merge, the Cloudflare `main` build and branch previews should work again with the existing dashboard settings.

## 2026-09-26 — PR 5 merged; GitHub Pages and Cloudflare both live

- Who: Claude (agent) merged PR 5 at Nomishka's request; Nomishka fixed the Cloudflare dashboard settings.
- Done: https://github.com/Nomishka/bitcoinfilmfest-com-fork/pull/5 merged into the fork's `main`. The GitHub Pages deploy passed (the fork site is styled again). The Cloudflare Workers build of `main` passed: Jekyll build, 1,162 files uploaded, deployed to the fork's `workers.dev` address. Final Cloudflare settings: build command `bash scripts/cloudflare-build.sh`, deploy command `npx wrangler deploy`, root directory `/` (it was `site`, which broke the build).
- PR: this log entry only.
- Preview links: WORKING. The first preview build on PR 6 failed because Worker Previews (`npx wrangler preview`) require a `previews` block in `wrangler.jsonc`. After adding an empty `"previews": {}`, the PR 6 preview build and deployment passed, and the Cloudflare bot posted a stable per-branch Preview URL (`<branch>-bitcoinfilmfest-com-fork.<account>.workers.dev`) plus a per-commit URL. Every non-`main` branch now gets one automatically (about 7 minutes per build).
- Open / next: (1) Nomishka decides what to send upstream to Tomek: the fork-subpath fix in `deploy-pages.yml` is safe for upstream; the Cloudflare files are fork-specific.

## 2026-09-26 — Cloudflare preview links for pull requests

- Who: Claude (agent), asked by Nomishka (chose option B: preview links).
- Done: The Cloudflare Worker `bitcoinfilmfest-com-fork` was only a "Hello world" placeholder, and the repo had no build instructions for it, so every `Workers Builds` check failed at once. Added `wrangler.jsonc` (serves the built Jekyll site as static files), `scripts/cloudflare-build.sh` (the build command) and `.ruby-version` (Ruby 3.3, same as GitHub Actions). Verified locally: the Jekyll build passes, `wrangler deploy --dry-run` accepts the config (about 1,300 files), and `wrangler dev` serves `/`, `/cinema/`, CSS and the 404 page correctly. GitHub Pages stays the production site.
- PR: https://github.com/Nomishka/bitcoinfilmfest-com-fork/pull/5
- Open / next: Nomishka sets 2 things in the Cloudflare dashboard (build command, and turning on builds for non-production branches), then checks that the bot posts a working preview link. Before this goes upstream, the `name` in `wrangler.jsonc` must match Tomek's own Worker, or leave these files out.

## 2026-09-26 — Fork website showed without styles

- Who: Claude (agent), asked by Nomishka.
- Done: The fork's GitHub Pages site (served under `/bitcoinfilmfest-com-fork/`) loaded as plain unstyled text. After the custom-domain cutover, `main` builds with an empty base path, so on the fork every CSS/JS/image link pointed to the wrong place. `.github/workflows/deploy-pages.yml` now reads the real base path from GitHub (`actions/configure-pages`). Verified by a local Jekyll build and a browser screenshot of the fork path: page fully styled, 0 missing files. The upstream build output is unchanged (empty base path).
- PR: https://github.com/Nomishka/bitcoinfilmfest-com-fork/pull/5 (added to the open PR).
- Open / next: Nomishka merges PR 5 and checks the fork site. The fix is also worth sending upstream to Tomek, so any fork of the repo renders correctly.

## 2026-09-26 — Cloudflare check failing on PR 5

- Who: Claude (agent), asked by Nomishka.
- Done: Looked into the red check on https://github.com/Nomishka/bitcoinfilmfest-com-fork/pull/5. The failing check is `Workers Builds` (Cloudflare Workers Git integration). It fails right away, before building anything. The repo's own `Public-safe Pages preview build` check passes. No code change fixes it; the problem is a setting in the Cloudflare dashboard.
- PR: https://github.com/Nomishka/bitcoinfilmfest-com-fork/pull/5 (explanation posted as a PR comment).
- Open / next: Nomishka either disconnects the repo in Cloudflare, or sets it up as Cloudflare Pages (root `site`, build `bundle exec jekyll build`, output `_site`). PR 5 can be merged either way.

## 2026-09-23 — Agent working rules and GitHub guide

- Who: Claude (agent), requested by Nomishka.
- Done: Read the knowledge base (README, BUILDER-GUIDE, HANDOFF-CURRENT, COLLABORATION, CHANGELOG, BUILD-LOG, roadmap, PR checks). Added `CLAUDE.md` (rules every agent follows: read the KB, work via PRs, log and hand off, guide Nomishka), this organisation log, and `docs/GITHUB-GUIDE-NOMISHKA.md` (step-by-step GitHub process). No website pages changed.
- PR: into `Nomishka/bitcoinfilmfest-com-fork` `main` from `claude/adoring-hawking-54yiw3`.
- Open / next: Nomishka reviews and merges the PR in the fork, then decides whether to send these process files upstream to Tomek. Website state is unchanged from `HANDOFF-CURRENT.md` (next up: Phase 2 content programme).
