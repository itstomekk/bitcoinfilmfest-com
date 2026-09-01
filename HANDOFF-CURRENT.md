# Handoff — Bitcoin FilmFest Jekyll rebuild
Updated: 2026-08-31

## Cross-project architecture

The website is a curated public projection of the wider private project knowledge base in `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\`. The CRM remains split across its existing local files and spreadsheets for now. Do not import the private KB or CRM into the Jekyll build. Read `PLAN-WEBSITE-ROADMAP.md` and `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\HANDOFF-TO-VERIFIER-2026-08-31.md` before reorganizing or adding broad content.

The Git state and cinema status below must be reconciled against the live checkout before execution because this handoff predates the latest local changes.

## Where this stands

The Jekyll rebuild is live at the temporary GitHub Pages URL. On top of the existing site (homepage, festival editions, Reel, Credits), the `/cinema/` section now contains the film database and company directory foundations, the essential-ten curation, the industry-footprint strip, and the first roadshow structure. The coherent Cinema ecosystem update is committed and deployed on `main` and `origin/main` at `517c87f`. Build and HTTP deployment verification passed.

### Current implementation after 2026-08-31 owner steer

- `/cinema/` is the single public Cinema destination: overview, essential films, searchable/filterable film catalogue, and companies/platforms on one page.
- The Cinema page now follows the `design-taste-frontend` redesign pass while preserving BFF's existing system: asymmetric hero with the real rabbit asset, horizontal featured shelf, sparse editorial hierarchy, sharp controls, and explicit mobile fallback.
- The primary menu has one direct `Cinema` link; `Films` and `Companies` are no longer separate Cinema menu items. Existing index/detail routes remain as useful deep links.
- `Festivals` now includes `Minis & roadshows`, a cautious archive page covering the verified historical pattern around Lugano, Lisbon, Funchal/Madeira, Cape Town/South Africa and El Salvador. It avoids claiming exact dates, venues or final running orders where the private archive is not conclusive.
- BFF’24 and BFF’25 already have public edition pages and remain linked under `Festivals`.
- “Bitfest” was not added as a named event because the verified local source material did not identify one unambiguously; add it only after a source/title/date is confirmed.

**Repository:** https://github.com/itstomekk/bitcoinfilmfest-com
**Temporary live site:** https://itstomekk.github.io/bitcoinfilmfest-com/
**Local checkout:** `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll`
**Deployment:** GitHub Actions builds and deploys `main` to GitHub Pages.

## Done this session (and the one before it)

- [verified] `/cinema/`, `/cinema/films/`, `/cinema/companies/` pages are present with real content (confirmed by reading each file, not just listing them).
- [verified] Two new Jekyll collections registered in `site/_config.yml`: `films` and `companies`, with permalinks `/cinema/films/:name/` and `/cinema/companies/:name/`, plus `defaults:` blocks that auto-assign the right layout.
- [verified] `site/_layouts/film.html` and `site/_layouts/company.html` built — real field rendering (director, cast, studio, sources, etc.), not placeholder content.
- [verified] `site/_includes/cinema-row.html` — shared list-row component, extends the site's existing `.showtime` row style rather than introducing generic cards (per `site/design.md`'s explicit rule against that).
- [verified] The current checkout contains 14 film entries and 7 company entries. The first curated cinema batch is committed in `0e98c97` and `866f4b8`, including BFF-linked titles and the essential-ten curation.
- [verified] `site/_cinema-schema.md` written — the field-by-field reference for adding new entries, plus a restated "never publish" list (banned internal research tags, no partner-sponsor entries here).
- [verified] `site/_data/navigation.yml` has a new "Cinema" dropdown (Overview / Films / Companies).
- [verified] `PLAN-CINEMA.md` (repo root) — the full phased plan (Phase 0 foundation and Phase 1 content implemented; Phase 2-4 remain scoped).
- [verified] `HANDOFF-CINEMA-TASKS.md` (repo root) — ready-to-assign task cards for delegating Phase 1 content work to smaller/lower-tier agents, one film or company per task, with exact KB source line numbers.
- [verified] `site/_chronicle/` collection — 10 short dated news items feeding a new Chronicle block on `/reel/`, modeled on thebitcoindistrict.com/press. `site/reel.md` rewritten to include it.
- [verified] Earlier UI fixes from a prior session (seats clipping, nav logo, heart icon, hover color, footer brightness) all confirmed intact — they were separately committed and pushed already (commits through `2d0dcef`), and one regression found in that batch (nav logo icon shrunk to near-invisible) was already fixed and is part of that separate, already-pushed history.
- [verified] A real local `jekyll build --trace` now passes on Windows with `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`. The only output is the known non-blocking `faraday-retry` notice.
- [verified] Local browser smoke test covered `/cinema/` and `/festivals/roadshows/`: the Cinema page renders 14 film items and 7 company entries, the filters/search controls are present, the direct Cinema nav link is active, and the roadshow page renders five researched places. Private/internal tags are absent from the generated public pages.

## Open — next up: Phase 2 content programme

1. **Festival-history extraction (first priority):** turn the historical Notion material into public-safe edition and roadshow stories. Start with BFF23 Warsaw, BFF24 Warsaw, BFF25 Warsaw, Lugano, Lisbon 2023, Madeira/Funchal 2024, Cape Town/South Africa, El Salvador, and the BFF26 recap. Separate confirmed facts, draft programme notes, and owner questions.
2. **Film expansion:** add the next 10–20 strongest public film records from the private cinema KB. Prioritize BFF-screened titles, award winners, films with complete public sourcing, and films that explain different parts of Bitcoin Cinema. Do not bulk-dump the KB.
3. **Owner brain-dump checkpoint:** every iteration must end with a short question set for Tomek about unknown attendance, winners, guests, programme changes, photos, videos, permissions, and the story behind the event. Do not invent missing facts.
4. **Build the private extraction ledger:** record source, confidence, publication candidate, missing owner facts, media leads, and whether a fact is safe for the public site.
5. **Only then:** implement the next coherent website batch, run build and route checks, visually review if available, and update this handoff again.

## Explicit next-phase boundaries

- Do not repeat Phase 0 foundation work.
- Do not treat raw Notion draft running orders as final attendance or screening records.
- Do not expose private contact data, CRM status, permissions, internal tags, or research disputes.
- Do not add more films merely to increase the count; each record must earn its place editorially.
- Ask the owner when a fact is missing or materially changes the story; use the answer in the next iteration.

## Decisions and why

- **Jekyll collections, not a YAML array**, for films/companies. Each entry is one Markdown file with front matter. Chosen because it mirrors the existing `_newsletters/` pattern already in this repo, gives free per-entry URLs, and is far easier for a small delegated agent (or a non-technical collaborator) to add one file correctly than to hand-edit a growing array without breaking YAML syntax elsewhere in the file.
- **Row list, not cards**, for film/company indexes. `site/design.md` explicitly rules out generic rounded cards for this site's visual language ("look like programme/showtime rows"). `cinema-row.html` extends the existing `.showtime` pattern instead of inventing a new component.
- **Private KB stays private.** Every entry is hand-curated from `Claude news/bitcoin-cinema-kb.md` (157 entries, sourcing caveats, internal tags) into clean public Markdown — never a build-time import. `_cinema-schema.md` has the exact list of tags/notes that must never reach a public file. Revisit only if Tomek explicitly wants a faster, less-curated pipeline.
- **BFF-PARTNERS-DATABASE.md (89 event sponsors) is explicitly excluded from `/cinema/companies/`.** Sponsors are not the same thing as Bitcoin-cinema production/distribution companies — don't merge the two lists later.

## Gotchas

- **This cloud sandbox cannot run `jekyll build`.** `gem install jekyll` fails on the `json` gem's native extension (no ruby-dev headers, no sudo). This has been true across multiple sessions — don't waste time retrying it here. Build and visually verify from Tomek's machine or via the GitHub Actions run itself.
- **The "perforation pattern was removed" note from the previous handoff is now stale.** An `effect-lab` commit (already pushed, before this session) added a full `.cinema-atmosphere` texture layer to `_layouts/default.html` — grain, scratches, dust, flicker, vignette, and `.cinema-sprocket` holes — active site-wide on every paper-screen page via `.stage--paper .cinema-sprocket`. This is intentional and already live; do not remove it thinking it's leftover cruft.
- **OneDrive sync in this environment sometimes locks empty folders** (`rmdir` can fail with "Operation not permitted" on an empty dir you just created) — harmless, doesn't affect the Jekyll build, just don't be alarmed by it.
- Large private files (`bitcoin-cinema-kb.md`, `QUERIES-KNOWLEDGE.md`, `BFF27-CONTACTS.md`) exceed normal read windows — use grep/line-number jumps, not full reads. `HANDOFF-CINEMA-TASKS.md` already has the line numbers for the next batch of KB entries, so this shouldn't come up again soon.

## Git state note

At the latest verification, `main` and `origin/main` both point to `517c87f` (`Add cinema inventory and industry footprint`). The published Cinema ecosystem update is deployed. The working tree currently contains unrelated documentation/context changes; inspect `git status --short` before staging anything and do not include unrelated files in a content commit.

The private source material remains outside the Jekyll build:
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\bitcoin-cinema-kb.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\BFF-NOTION-KNOWLEDGE.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\docs\context\NOTION-EXTRACTION-LEDGER.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF26-guest-page\press\BFF26-POST-FESTIVAL-SOURCE.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF26-guest-page\BFF26-AGENDA-confirmed.md`

The private-to-public map is:
`C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\CINEMA-DATABASE-MAP.md`

Current public collection counts: 14 films and 7 companies. The next content work must be staged separately from unrelated local modifications and must update the handoff after verification.

## Standing Git/build workflow (unchanged from before)

1. Before work: `git switch main` then `git pull --ff-only origin main`.
2. Branch for one coherent change: `git switch -c content/cinema-phase-0`.
3. Build locally from `site/`: `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`.
4. Review desktop and mobile for affected pages.
5. Check exactly what's staged: `git status --short`.
6. Commit with a clear message, push the branch, open a PR, review, merge to `main`.
7. GitHub Actions deploys only `main` — check the Actions run and the live URL after merge.

For tiny urgent fixes a trusted maintainer may push straight to `main`, but a change this size (a whole new site section) should go through a branch and PR.

## Pick up here

Paste this to start the next session:

> Read `HANDOFF-CURRENT.md`, `PLAN-WEBSITE-ROADMAP.md`, `PLAN-CINEMA.md`, and `docs/context/NOTION-EXTRACTION-LEDGER.md` first. Confirm `git status --short --branch` and the current public routes. Do not repeat Phase 0. Start Phase 2 with a private source scan of the historical Notion material and BFF post-festival records. Build a fact ledger for BFF23/BFF24/BFF25 Warsaw, Lugano, Lisbon, Madeira/Funchal, Cape Town/South Africa, El Salvador, and BFF26. Separate confirmed facts from draft programme material and owner questions. Then propose a public story batch and a film batch of 10–20 strongest records from the private cinema KB. End the iteration with concise questions for Tomek about missing attendance, winners, guests, photos, videos, dates, permissions, and anecdotes. Never invent facts or expose private CRM/research notes. Implement only after the source and owner questions are clear; run build/routes checks and update this handoff when finished.