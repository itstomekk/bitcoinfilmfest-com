# Cinema Hub — sub-plan (v1 — SUPERSEDED)

**⚠️ SUPERSEDED 2026-08-29 by `PLAN-CINEMA.md`.** After this v1 was written, Tomek expanded scope: a full `/cinema/` ecosystem section (film database with per-title profile pages, a companies/projects directory, global reusable frame, phased checkpoints for other agents) rather than one curated showcase page. Kept here as a dated historical record per the never-delete rule — read `PLAN-CINEMA.md` for the current plan, not this file.

**Status:** proposed, not yet built. Extends `REBUILD-PHASES.md` Phase 4 (film catalogue / private-source pipeline) with a lighter first step.

## Purpose

`about.md` already claims Bitcoin FilmFest runs "a Cinema Hub... extensive network of films and people." This page is the public proof of that claim: a curated showcase that a filmmaker, sponsor, or journalist can land on and immediately see that Bitcoin cinema is an active, real industry — not a hobby archive.

It is **not** the research database. The private working KB (`Claude news/bitcoin-cinema-kb.md`, 157 entries with sourcing caveats, disputed items, internal tags) stays private. This page is a small, hand-picked, always-presentable subset.

## Pages / files

| File | Purpose |
| --- | --- |
| `site/hub.md` | Public page. New top-level nav item (added to `_data/navigation.yml`, alongside Storyboard / Festivals / Reel / Credits / Contribute). |
| `site/_data/cinema-hub.yml` | Curated public dataset: stat strip, "on our radar" titles, "in production" strip, one anchor story, recent news items. Same editing pattern as existing `_data/credits.json` / `_data/navigation.yml` — plain YAML, no code required to update. |

## Content sections (page structure)

1. **Stat strip** — small set of top-line numbers (e.g. titles tracked, features, released, in production). Pulled from the KB's own stats line, refreshed occasionally — not on every KB run.
2. **On our radar** — 6–10 cards for titles with real name recognition and a public production trail (major studio/network, known cast/director, reviewed by a mainstream outlet). This is the credibility section.
3. **In production** — a short strip pulled from the upcoming-films tracker: title, stage, expected window. Signals BFF is watching the pipeline, not just cataloguing the past.
4. **Anchor story** — one title told with real narrative texture (a paragraph or two, not a bullet). Does more for credibility than ten short entries.
5. **Recent news** — 8–12 dated, sourced items, outlet name visible (Variety, Deadline, HBO, Netflix, Hollywood Reporter preferred over niche crypto press).

## Curation rule (hard constraint)

Curation from KB → YAML is a **manual or agent-assisted editorial pass**, never an automated/build-time import from the private KB. This matches Phase 4's explicit review-gate requirement.

Never published to the public repo:
- Internal tags: `[sourcing-pending]`, `[unverifiable]`, `[scope-review]`, `[adjacent]`, `[not-a-film]`, `[duplicate]`
- Anything from `UNCERTAINTY.md` (disputes, unresolved title conflicts, scope calls not yet made)
- BFF-internal notes, contact names, sourcing commentary written for the research team
- Anything outside the Bitcoin-only scope rule — no Ethereum/NFT/generic-crypto entries, even ones tagged `[adjacent]` in the KB

Only entries with a clean, credible public source (mainstream outlet, official studio/streamer announcement) go on the page.

## Update pipeline (for GitHub collaborators)

1. Curator (Tomek or an agent acting for him) reviews `Claude news/bitcoin-cinema-kb.md` and `bitcoin-cinema-news.md` for newsworthy, clean-sourced items.
2. Hand-write/update entries in `site/_data/cinema-hub.yml` — strip all internal tags and private notes per the rule above.
3. Normal repo flow: branch → edit YAML → local Jekyll build (`bundle exec jekyll build --trace`) → review desktop/mobile → PR → merge to `main` → GitHub Actions deploys.
4. A non-technical collaborator can add a single news item by editing the YAML directly — same skill level as editing `navigation.yml` today.

**Cadence:** ad hoc, triggered by a genuinely newsworthy item (studio announcement, festival win, major release) — not tied 1:1 to the biweekly KB research cadence, since most KB churn is internal bookkeeping rather than showcase-worthy.

## Open items (need Tomek's call before/while building)

- First content pass: which 6–10 "on our radar" titles, which 8–12 news items, which single anchor story. Candidates surfaced from the KB scan (2026-08-29): *One Attempt Remaining* (Netflix, Garner/Cena, 21 Laps), *Dutch & Razzlekhan* (Amazon MGM, filmed 2025), *Money Electric: The Bitcoin Mystery* (HBO), *Hotel Bitcoin* (Netflix), *The Satoshi Affair* (David O. Sacks Productions), *Cold Wallet* (SXSW/Variety-reviewed) — for radar cards; *The Six Billion Dollar Man* (Bitcoin-only global release, Dorsey-backed, Snowden panel) as a strong anchor-story candidate.
- Exact page URL/slug (`/hub/` vs `/cinema/` vs other) and nav label wording.
- Visual treatment — reuse existing cinema-frame card patterns from festival edition pages, or a new layout in `design.md`.
- Whether stat-strip numbers get a "last updated" date visible on the page (recommended, for trust) or stay silent.

---
*Created 2026-08-29. Not yet approved for build — review before starting `site/hub.md` / `cinema-hub.yml`.*
