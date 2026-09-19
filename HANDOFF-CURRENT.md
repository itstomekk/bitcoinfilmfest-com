# Handoff — Bitcoin FilmFest Jekyll rebuild
Updated: 2026-09-19

## Cross-project architecture

The website is a curated public projection of the wider private project knowledge base in `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\`. The CRM remains split across its existing local files and spreadsheets for now. Do not import the private KB or CRM into the Jekyll build. Read `PLAN-WEBSITE-ROADMAP.md` and `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\HANDOFF-TO-VERIFIER-2026-08-31.md` before reorganizing or adding broad content.

The Git state and cinema status below were reconciled against the live checkout after the 2026-09-19 dead-route integration. The four focused repair branches were merged into `main` at `e35e159`, and GitHub Actions run `35417053924` completed its build and Pages deploy successfully.

## Where this stands

The Jekyll rebuild is live through GitHub Pages and the configured custom domain. On top of the existing site (homepage, festival editions, Reel, Credits), the `/cinema/` section now contains the film database and company directory foundations, the essential-ten curation, the industry-footprint strip, and the first roadshow structure. The coherent Cinema ecosystem update was originally committed at `517c87f` and is included in the current `main`; the archive/current-edition visual pass landed in merge commit `4635bce`. The latest build and Pages deployment passed.

### 2026-09-19 dead-route repair integration

- Merged `fix/sponsor-page-stub`, `fix/press-and-media-page`, `fix/gallery-page`, and `fix/small-dead-links` into `main` at `e35e159` using a clean worktree; unrelated local changes in the primary checkout were left untouched.
- Added working `/sponsor/`, `/press-and-media/`, and `/gallery/` routes. The gallery renders all 51 existing photos with non-empty content alt text; no primary navigation or homepage link was added.
- Repaired the six small dead internal links without inventing replacement destinations where no real target existed.
- Local safety scan, Jekyll build, generated-route checks, gallery asset checks, and `git diff --check` passed. The Actions build and Pages deploy passed in run `35417053924`.
- The deployed route content is reachable, but normal HTTPS verification for `bitcoinfilmfest.com` is still pending: GitHub Pages reports `https_enforced: false` and the current certificate fails hostname verification. Do not call the custom domain TLS-ready until the certificate is corrected and HTTPS enforcement is enabled.

### 2026-09-18 Reel/newsletter migration integration

- The Reel archive is now the single editorial collection for interviews, articles, and newsletters. The former `_newsletters` collection is gone; all entries live under `site/_reel/` with `category: interviews`, `category: articles`, or `category: newsletters`.
- The collection contains 23 public entries: 10 prior interviews/articles plus 13 Bitcoin Cinema Digest issues, including the previously migrated Summer 2024 issue. Every migrated entry carries `archived: true`; future writing can use the Posts view without entering the archive.
- `/reel/` now renders Chronicle, Posts, then Archive. Posts has a deliberate empty state, while Archive is a single newest-first list with visible category labels. All 23 detail routes render real body content.
- The migration build passed with the Windows Ruby toolchain. Source and generated Reel output contain no WordPress `/wp-content/uploads/` or raw `bitcoinfilmfest.com/media` references; `/25/` remains the canonical BFF’25 route.
- The entries contain text and verified external source links only. No private contact, CRM, KB, Notion, Drive, licensing, or internal review material was copied into the public entries.
- The FormSubmit AJAX success path reads the footer form’s configured `_next` value, preserving the shared `/thanks/` destination without hardcoding it in JavaScript.

### 2026-09-18 press kit and BFF’26 press room

- `/presskit/` now preserves the local branding book: BFF logos, rabbit mark, posters, laurels, SVG/PDF vectors, colours and Syne Mono/Courier Prime specimens. The source was `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\logos-page\`; only its public HTML and 14 prepared assets were copied.
- Storyboard links to `/presskit/`, and the BFF’26 Press Kit section links to `/26/press/`, `/presskit/`, and the existing `/25/#gallery` archive.
- `/26/press/` restores 34 local static EN/PL pages from `BFF26-guest-page\press\`: hub, info-base, recaps, previews, interviews, evergreen articles and shared CSS. Private source notes, FTP scripts and archive backups were excluded.
- Restored press pages use the current `/presskit/` and local project-relative paths rather than the old `/26/laurels/`, `/logos`, and `/gallery/` destinations.
- Route inventory is now 101 generated / 89 public-indexable outputs.

### Current implementation after 2026-08-31 owner steer

- `/cinema/` is the single public Cinema destination: overview, essential films, searchable/filterable film catalogue, and companies/platforms on one page.
- The Cinema page now follows the `design-taste-frontend` redesign pass while preserving BFF's existing system: asymmetric hero with the real rabbit asset, horizontal featured shelf, sparse editorial hierarchy, sharp controls, and explicit mobile fallback.
- The primary menu has one direct `Cinema` link; `Films` and `Companies` are no longer separate Cinema menu items. Existing index/detail routes remain as useful deep links.
- `Festivals` now includes `Minis & roadshows`, a cautious archive page covering the verified historical pattern around Lugano, Lisbon, Funchal/Madeira, Cape Town/South Africa and El Salvador. It avoids claiming exact dates, venues or final running orders where the private archive is not conclusive.
- BFF’24 and BFF’25 already have public edition pages and remain linked under `Festivals`.
- “Bitfest” was not added as a named event because the verified local source material did not identify one unambiguously; add it only after a source/title/date is confirmed.

### 2026-09-16 visual and performance pass

- BFF’23 and BFF’25 keep their complete public albums, now behind native disclosure controls: 554 and 152 lazy-loaded derivatives respectively. The albums are still available in full when opened; originals remain outside Git.
- BFF’27’s hero art no longer reads as a generic bordered card, and the page now defines the archive accent token used by its index/fact treatments.
- BFF’24’s first selection feature is given an asymmetric lead layout on wide screens; BFF’23/BFF’24 archive indexes have visible hover movement.
- The shared BFF’26 shell and its scoped styles were not changed.
- PR #12 was merged into `main` at `4635bce`; its GitHub Pages workflow build and deploy both passed. HTTPS verification confirmed the updated `/23/`, `/24/`, `/25/`, `/26/`, and `/27/` routes live.

**Repository:** https://github.com/itstomekk/bitcoinfilmfest-com
**GitHub Pages preview:** https://itstomekk.github.io/bitcoinfilmfest-com/
**Configured custom domain:** https://bitcoinfilmfest.com (content deployed; TLS/enforcement pending verification above)
**Local checkout:** `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll-bff26`
**Deployment:** GitHub Actions builds and deploys `main` to GitHub Pages.

## Done this session (and the one before it)

- [verified] `/cinema/`, `/cinema/films/`, `/cinema/companies/` pages are present with real content (confirmed by reading each file, not just listing them).
- [verified] Two new Jekyll collections registered in `site/_config.yml`: `films` and `companies`, with permalinks `/cinema/films/:name/` and `/cinema/companies/:name/`, plus `defaults:` blocks that auto-assign the right layout.
- [verified] `site/_layouts/film.html` and `site/_layouts/company.html` built — real field rendering (director, cast, studio, sources, etc.), not placeholder content.
- [verified] `site/_includes/cinema-row.html` — shared list-row component, extends the site's existing `.showtime` row style rather than introducing generic cards (per `site/design.md`'s explicit rule against that).
- [verified] The current checkout contains 20 film entries and 7 company entries. The first curated cinema batch is committed in `0e98c97` and `866f4b8`, the ecosystem update in `517c87f`, and the first festival-history handoff in `8c1d3ee`, with this film batch following it.
- [verified] `site/_cinema-schema.md` written — the field-by-field reference for adding new entries, plus a restated "never publish" list (banned internal research tags, no partner-sponsor entries here).
- [verified] `site/_data/navigation.yml` has a new "Cinema" dropdown (Overview / Films / Companies).
- [verified] `PLAN-CINEMA.md` (repo root) — the full phased plan (Phase 0 foundation and Phase 1 content implemented; Phase 2-4 remain scoped).
- [verified] `HANDOFF-CINEMA-TASKS.md` (repo root) — ready-to-assign task cards for delegating Phase 1 content work to smaller/lower-tier agents, one film or company per task, with exact KB source line numbers.
- [verified] `site/_chronicle/` collection — 10 short dated news items feeding a new Chronicle block on `/reel/`, modeled on thebitcoindistrict.com/press. `site/reel.md` rewritten to include it.
- [verified] Earlier UI fixes from a prior session (seats clipping, nav logo, heart icon, hover color, footer brightness) all confirmed intact — they were separately committed and pushed already (commits through `2d0dcef`), and one regression found in that batch (nav logo icon shrunk to near-invisible) was already fixed and is part of that separate, already-pushed history.
- [verified] A real local `jekyll build --trace` now passes on Windows with `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`. The only output is the known non-blocking `faraday-retry` notice.
- [verified] Local browser smoke test covered `/cinema/` and `/festivals/roadshows/`: the Cinema page renders 20 film items and 7 company entries, the filters/search controls are present, the direct Cinema nav link is active, and the roadshow page renders five researched places. Private/internal tags are absent from the generated public pages.

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

- **Jekyll collections, not a YAML array**, for films/companies and Reel editorial entries. Each entry is one Markdown file with front matter, gives free per-entry URLs, and is far easier for a small delegated agent (or a non-technical collaborator) to add one file correctly than to hand-edit a growing array without breaking YAML syntax elsewhere in the file.
- **One Reel collection for editorial writing.** Interviews, newsletters, guest posts, features, and event reports all render under `/reel/<slug>/`; `category` is metadata with only `interviews`, `newsletters`, or `articles` allowed. `archived: true` marks the 23 explicitly migrated legacy entries and is reserved for archived content.
- **Row list, not cards**, for film/company indexes. `site/design.md` explicitly rules out generic rounded cards for this site's visual language ("look like programme/showtime rows"). `cinema-row.html` extends the existing `.showtime` pattern instead of inventing a new component.
- **Private KB stays private.** Every entry is hand-curated from `Claude news/bitcoin-cinema-kb.md` (157 entries, sourcing caveats, internal tags) into clean public Markdown — never a build-time import. `_cinema-schema.md` has the exact list of tags/notes that must never reach a public file. Revisit only if Tomek explicitly wants a faster, less-curated pipeline.
- **BFF-PARTNERS-DATABASE.md (89 event sponsors) is explicitly excluded from `/cinema/companies/`.** Sponsors are not the same thing as Bitcoin-cinema production/distribution companies — don't merge the two lists later.

## Gotchas

- **This cloud sandbox cannot run `jekyll build`.** `gem install jekyll` fails on the `json` gem's native extension (no ruby-dev headers, no sudo). This has been true across multiple sessions — don't waste time retrying it here. Build and visually verify from Tomek's machine or via the GitHub Actions run itself.
- **The "perforation pattern was removed" note from the previous handoff is now stale.** An `effect-lab` commit (already pushed, before this session) added a full `.cinema-atmosphere` texture layer to `_layouts/default.html` — grain, scratches, dust, flicker, vignette, and `.cinema-sprocket` holes — active site-wide on every paper-screen page via `.stage--paper .cinema-sprocket`. This is intentional and already live; do not remove it thinking it's leftover cruft.
- **OneDrive sync in this environment sometimes locks empty folders** (`rmdir` can fail with "Operation not permitted" on an empty dir you just created) — harmless, doesn't affect the Jekyll build, just don't be alarmed by it.
- Large private files (`bitcoin-cinema-kb.md`, `QUERIES-KNOWLEDGE.md`, `BFF27-CONTACTS.md`) exceed normal read windows — use grep/line-number jumps, not full reads. `HANDOFF-CINEMA-TASKS.md` already has the line numbers for the next batch of KB entries, so this shouldn't come up again soon.

## Git state note

The four dead-route repair branches have been merged; `main` includes the integration result at `e35e159`. Inspect `git status --short` before staging anything else.

The private source material remains outside the Jekyll build:
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\bitcoin-cinema-kb.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\BFF-NOTION-KNOWLEDGE.md`
- `C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/website/rebuild-jekyll-bff26/docs/context/NOTION-EXTRACTION-LEDGER.md`
- `C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/website/rebuild-jekyll-bff26/docs/context/FESTIVAL-HISTORY-RESEARCH.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF26-guest-page\press\BFF26-POST-FESTIVAL-SOURCE.md`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF26-guest-page\BFF26-AGENDA-confirmed.md`

The private-to-public map is:
`C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\CINEMA-DATABASE-MAP.md`

Current public collection counts: 20 films and 7 companies. The next content work must be staged separately from unrelated local modifications and must update the handoff after verification.

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

> Read `HANDOFF-CURRENT.md`, `PLAN-WEBSITE-ROADMAP.md`, `PLAN-CINEMA.md`, `docs/context/NOTION-EXTRACTION-LEDGER.md`, and `docs/context/FESTIVAL-HISTORY-RESEARCH.md` first. Confirm `git status --short --branch` and the current public routes. Do not repeat Phase 0. Start Phase 2 with a private source scan of the historical Notion material and BFF post-festival records. Build a fact ledger for BFF23/BFF24/BFF25 Warsaw, Lugano, Lisbon, Madeira/Funchal, Cape Town/South Africa, El Salvador, and BFF26. Separate confirmed facts from draft programme material and owner questions. Then propose a public story batch and a film batch of 10–20 strongest records from the private cinema KB. End the iteration with concise questions for Tomek about missing attendance, winners, guests, photos, videos, dates, permissions, and anecdotes. Never invent facts or expose private CRM/research notes. Implement only after the source and owner questions are clear; run build/routes checks and update this handoff when finished.