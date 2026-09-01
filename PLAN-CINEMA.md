# /cinema/ — Bitcoin Cinema Ecosystem — phased build plan

**Status:** Phase 0 foundations, Phase 1 seed content, the essential-ten curation, the industry-footprint strip, the private database map, and the first Minis/Roadshows structure are implemented and deployed on `main` at commit `517c87f`. The current direction is a single public Cinema page: overview, browsable films, companies, industry context, and historical festival stories. Detail routes remain available behind the rows. A real Windows Jekyll build and HTTP deployment checks have passed; visual review remains optional and was intentionally skipped in the last release. Supersedes `PLAN-CINEMA-HUB.md` (2026-08-29 v1, single-page scope) — kept in the repo as a dated record, not deleted. Extends `REBUILD-PHASES.md` Phase 4.

**Slug:** `/cinema/` for the whole section. Sub-routes TBD per phase (`/cinema/films/`, `/cinema/films/:slug/`, `/cinema/companies/`, `/cinema/companies/:slug/`, `/cinema/news/`).

## Why this exists

`about.md` already claims BFF runs a "Cinema Hub... extensive network of films and people." `/cinema/` is the public proof: an IMDb-style destination showing that Bitcoin cinema is a real, active industry — films with real studios attached, real production companies, real ongoing news — built from the private research KB (`Claude news/bitcoin-cinema-kb.md`, 157 entries) without exposing its private sourcing plumbing.

The public experience is now explicitly **one Cinema page**, with optional detail routes behind individual entries:

1. **`/cinema/`** — the single public destination: ecosystem overview, essential titles, searchable/filterable film catalogue, and companies/platforms.
2. **Detail routes** — individual film/company profiles remain available from catalogue rows for people who want the full record.
3. **News** — folded into `/cinema/` and/or a `/cinema/news/` feed, sourced from `bitcoin-cinema-news.md`.

This plan explicitly **uses the whole KB** over time rather than hand-picking ~10 titles once — the 157 entries, 73 news items, and 48-entry upcoming-films tracker are the actual content reservoir, released in curated batches per phase.

## Data source boundary (unchanged principle, now applies to more data)

Private and never published as-is:
- `Claude news/bitcoin-cinema-kb.md`, `bitcoin-cinema-news.md`, `BFF27-ai-upcomingfilms.md`, `UNCERTAINTY.md`, `BFF27-CONTACTS.md`, `BFF-PEOPLE-DATABASE.md`, `BFF-PARTNERS-DATABASE.md`
- Internal tags: `[sourcing-pending]`, `[unverifiable]`, `[scope-review]`, `[adjacent]`, `[not-a-film]`, `[duplicate]`, `[stalled]`
- Contact names/emails, BFF-internal notes, sourcing commentary written for the research team, anything from the Decisions Log disputes

Public, once curated:
- Title/company name, year/est. date, type, director/founder, cast, country, runtime, one-paragraph Bitcoin angle (rewritten in public voice, not copy-pasted researcher notes), platform/where-to-watch, trailer link, 1-3 credible public sources, BFF screening history if any.

`[adjacent]`-tagged entries are a judgment call per phase, not a blanket rule — see Phase 2 open item.

**BFF-PARTNERS-DATABASE.md (89 sponsors/vendors) is explicitly OUT of `/cinema/companies/`.** That's a different thing — event sponsors, not Bitcoin-cinema production/distribution companies. Do not merge the two lists. `/cinema/companies/` draws only from the KB's own Studios/Production Companies and Distribution/Platforms/Funding sections.

## Global component: the shared frame

Per `design.md`, every page already shares the room/bezel/frame chrome (`assets/css/cinema-frame.css`, `_includes/nav.html`, `_includes/footer.html`) — this is the "cinema-frame" that must stay global and does not need reinventing.

What's new is a **list/detail component pair** for this section:
- A row/list pattern for the film and company indexes, built as an extension of the existing `.showtime` row language (design.md explicitly prefers "programme/showtime rows... not generic rounded cards") rather than introducing a new "card" visual idiom.
- A profile-page pattern (`_layouts/film.html`, `_layouts/company.html`) reusing the paper/reading-page screen surface already defined for content pages.

Both get built once in Phase 1 and reused for every subsequent entry — one Liquid include/layout per type, driven by data, not one hand-written page per film.

## Phased build (each phase = a checkpoint; small, mergeable, independently useful)

### Phase 0 — Foundations (blocking everything else) — ✅ built 2026-08-30, pending a real local build check
- [x] Decide data shape: **Jekyll collections**, per the recommendation — `_films/*.md`, `_companies/*.md` with front matter, mirroring `_newsletters/`.
- [x] Front-matter schema written down in `site/_cinema-schema.md` (excluded from the Jekyll build, builder-facing doc only).
- [x] `films` and `companies` registered in `_config.yml` `collections:` with permalinks `/cinema/films/:name/` and `/cinema/companies/:name/`, plus `defaults:` blocks so entries get `layout: film`/`layout: company` automatically.
- [x] Shared list-row include (`_includes/cinema-row.html`) and both profile layouts (`_layouts/film.html`, `_layouts/company.html`) built — real field rendering, not lorem ipsum.
- [x] `/cinema/` added to `_data/navigation.yml` as a top-level item with Overview/Films/Companies children, added only once real seed entries existed in both collections.
- [x] Hub page (`cinema.md`) built with an auto-counted stat strip (`site.films.size` etc. — not hand-typed) and featured-highlights sections, plus the two index pages (`cinema-films.md`, `cinema-companies.md`).
- [x] One real seed entry per collection: *The Gimp and the Hitman* (film — BFF'26 Official Selection, ties the database back to the festival) and Angel Studios (company — NYSE-listed, Bitcoin treasury, clean sourcing).

**Checkpoint 0 done when:** one real film and one real company render correctly end-to-end (index row → profile page → back), using the shared frame, on desktop and mobile, via a real local Jekyll build. **Structurally verified** (Liquid tag balance, YAML front-matter parse, schema field/enum validation, banned-internal-tag scan, permalink-collision check, cross-check of every `page.*` field referenced in the layouts against what the seed files actually provide — all clean). **Not yet verified via a real `jekyll build`** — this sandbox has no ruby-dev headers/sudo (same documented gap as prior sessions) and cannot install the `jekyll` gem. First real visual check needs Tomek's machine or a GitHub Actions run.

-### Phase 1 — Seed content (prove the pattern with real, strong entries) — ✅ content implemented, verification pending
- [x] Migrate the first strong public batch: the current checkout contains 14 `_films/` entries, including the essential-ten curation and BFF-linked titles.
- [x] Migrate the first company/platform batch: the current checkout contains 7 `_companies/` entries.
- [x] Write the `/cinema/` hub page with auto-counted stats, curated highlights, and links into `/cinema/films/` and `/cinema/companies/`.
- [ ] Anchor story block on the hub page — one title told in full prose (*The Six Billion Dollar Man* is the standing candidate: Bitcoin-only global release, Dorsey-backed, Snowden panel).

**Checkpoint 1 content and release bar:** met. The public Cinema update is deployed at `517c87f`; Windows Jekyll build, generated routes, HTTP smoke tests, and GitHub Actions deployment verification passed. Visual review was intentionally skipped by owner decision and remains optional.

### Phase 2 — Historical festival intelligence + film expansion (active)

This phase has two parallel tracks, with the historical festival track first because it gives the film catalogue meaning.

#### Phase 2A — Extract and write the festival history

- [ ] Build a private fact ledger from the Notion extraction and post-festival source files.
- [ ] Cover BFF23 Warsaw, BFF24 Warsaw, BFF25 Warsaw, BFF26 Warsaw, Lugano, Lisbon 2023, Madeira/Funchal 2024, Cape Town/South Africa, El Salvador, and other verified conference appearances.
- [ ] For every event, separate: confirmed fact, draft/uncertain fact, owner question, public media lead, and publication status.
- [ ] Turn the best material into stories rather than schedule dumps: the travelling Cinema Room model, the evolution from Warsaw festival to international roadshow, the African/community strand, the creator and audience stories, the Golden Rabbits, and the BFF/MoneroKon cultural intersection.
- [ ] Use photos, video, quotes, award artefacts, posters, programmes and attendee anecdotes only after checking ownership/permission and identifying the edition.
- [ ] Ask Tomek a concise brain-dump question set at the end of every iteration; do not silently fill missing attendance, winners, dates or names.

#### Phase 2B — Grow the film database

- [ ] Add the next 10–20 strongest public film records from the private KB in small batches.
- [ ] Prioritize BFF-screened titles, Golden Rabbit winners/nominees, films with complete public sourcing, and titles that represent distinct Bitcoin Cinema modes: documentary, fiction, short, animation, art, adoption stories, monetary history, sovereignty and community.
- [ ] Prefer a smaller number of rich, accurate records over a bulk import. Keep unsourced, disputed and internal-only records private.
- [ ] Record each candidate in `CINEMA-DATABASE-MAP.md` before publication and link its private provenance in the local map only.
- [ ] Keep stable slugs and add one entry per entity; cross-link companies only when the matching public record exists.
- [ ] Apply a consistent policy to Bitcoin-adjacent titles; until Tomek decides otherwise, do not feature them as core Bitcoin Cinema.

- [ ] Add simple filtering/sorting to `/cinema/films/` once the expanded catalogue needs it (by type, status, year, BFF appearance and essential/editorial tier).

**Checkpoint 2 done when:** the historical archive has a reliable event ledger and at least one strong public story, the next film batch is live with complete profile pages and sources, owner questions are resolved or clearly labelled, and the handoff explains exactly what a new agent should do next.

### Phase 3 — Fill out companies + add live "in production" + news feed
- [ ] Migrate the rest of Studios/Production Companies and Distribution/Platforms/Funding sections.
- [ ] Add an "In Production" strip/section pulling from `BFF27-ai-upcomingfilms.md` (48 entries) — title, stage, expected window, linked to a profile page once/if the title graduates to `released`.
- [ ] Build `/cinema/news/` (or fold into the hub) from `bitcoin-cinema-news.md` — dated, sourced, outlet-name-visible items; curated selection favoring mainstream outlets over niche crypto press, per the original screening rule.
- [ ] Cross-link: a film's profile page links to its production company's profile page and vice versa (front-matter reference field, e.g. `company: angel-studios`).

**Checkpoint 3 done when:** companies/platforms/venues all have pages, in-production titles are visible and distinct from released ones, news feed is live and linked from the hub, cross-linking works both directions.

### Phase 4 — Polish, discovery, trust (folds into REBUILD-PHASES.md Phase 5)
- [ ] Per-entry Open Graph / social preview images.
- [ ] `Movie` / `Organization` schema.org markup on profile pages where facts are verified.
- [ ] "Last updated" dates visible per entry (trust signal, cheap to add since collections already carry dates).
- [ ] Trailer embeds (YouTube) on film profile pages, lazy-loaded, respecting the site's reduced-motion rules.
- [ ] Search/filter maturity pass once volume is high enough to need it.

## Update pipeline for GitHub collaborators (this is the point of using collections)

Adding one film = adding one Markdown file, e.g. `site/_films/one-attempt-remaining.md`:

```yaml
---
title: "One Attempt Remaining"
year: 2027
type: Feature
status: in-production
director: null
studio: Netflix / 21 Laps Entertainment
company: null   # future cross-link once a matching _companies/ entry exists
country: USA
runtime: null
synopsis: >
  A locked hardware wallet, two guesses left, and a fortune in Bitcoin on the line.
bitcoin_angle: >
  Inspired by the real Stefan Thomas IronKey story...
platform: null
trailer: https://www.youtube.com/watch?v=lc7D58V7yFo
sources:
  - label: Variety
    url: https://variety.com/2025/film/news/netflix-jennifer-garner-cryptocurrency-one-attempt-remaining-1236606649/
featured: true
---
Optional longer-form body content (prose) renders below the front-matter fields.
```

This is deliberately close to editing `_data/credits.json` or adding a `_newsletters/` post — no code, no build-time importer, no automation pulling from the private KB directly. A curator (Tomek, or an agent acting for him) does the KB → Markdown translation by hand or with assistance, one batch at a time, per phase above.

**Cadence:** Phase 0-1 is one push to get the pattern proven. Phases 2-3 are explicitly meant to be picked up slowly, batch by batch, by whoever (human or agent) has time — that's why each phase is broken into small checkpointed batches rather than one big migration. Phase 4 waits until there's real content volume to justify it.

## Open items needing Tomek's call

- `[adjacent]` visibility policy (Phase 2) — show with a tag, or hold back entirely.
- Exact nav labels ("Films" / "Titles" / "Catalogue"? "Companies" / "Industry" / "Ecosystem"?).
- Whether `/cinema/companies/` should also surface un-tiered mentions like physical Bitcoin-accepting cinemas (Cine Multi) as their own type, or a "Venues" sub-filter within Companies.
- Whether the Six Billion Dollar Man should be the first long-form anchor story on the Cinema hub.

---
*Created 2026-08-29 (v2 — supersedes the single-page v1 plan after Tomek's steer: ecosystem section, film + company profile pages, global reusable frame, phased/checkpointed for other agents to pick up incrementally). Phase 0 and the Phase 1 content batch were implemented afterward; the real-build/release gate remains open.*
