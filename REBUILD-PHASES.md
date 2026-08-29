# Bitcoin FilmFest rebuild phases

This is the working migration roadmap. It replaces the public route-inventory page that previously exposed implementation status. The underlying route inventory remains private-to-builders in `site/_data/sitemap.json` and `site/SITEMAP-PLAN.md`; neither should be linked or rendered for visitors.

## Principles

- Preserve established public URLs wherever practical. Add a redirect before retiring an old URL.
- Migrate real historic content and assets. Do not invent programme, award, film, or partner details.
- Each phase ends with a local build, route checks, desktop/mobile review, and a focused pull request.
- The public repository is not the home for raw private data. Keep private sources in a private repository or service.

## Phase 0 - Foundation and visual shell - complete

- Jekyll source, shared cinema frame, data-driven menu, reusable footer, visual tokens, GitHub Actions deployment.
- GitHub Pages temporary URL is live.
- Historic Credits data, key BFF editions, and a first newsletter have been migrated.

## Phase 1 - Archive triage and URL decisions

**Goal:** turn the historic route inventory into an editorially approved migration queue.

1. Review every historical route with the owner.
2. Mark each route as one of: migrate, redirect, archive externally, or retire.
3. Record the desired URL and source location in the private builder plan.
4. Add redirects only after the destination exists.

**Output:** a prioritised list, not a public page.

## Phase 2 - Festival edition pages

**Goal:** complete BFF 2024, 2025, 2026, and 2027 pages using authenticated historic material.

1. Recover programme, guests, jury, venues, awards, press, partners, and approved photography.
2. Build one reusable edition-page content pattern rather than copying page markup.
3. Add source/provenance comments beside imported data.
4. Verify every image has accurate alt text and a local rights-approved source.

**Output:** useful edition hubs that link to the most valuable historic material.

## Phase 3 - Reel and publication archive

**Goal:** make Reel a single calm destination with real content, not a menu tree.

1. Migrate newsletters in chronological order.
2. Add verified press coverage and selected interviews/blog posts.
3. Create a readable archive/index within the Reel page or a future collection page when there is enough content.
4. Preserve original dates and bylines.

**Output:** an editorial record people can browse and search.

## Phase 4 - Film catalogue and private-source pipeline

**Goal:** publish an approved public film catalogue without exposing the private working database.

1. Define the public fields: title, year, country, director, still, short synopsis, edition/screening status, and public links.
2. Keep the upstream data in a separate private repo or database.
3. Add a build-time importer using GitHub Actions Secrets only after a source is approved.
4. Generate public static JSON/pages during the build. Do not commit secrets, raw exports, contracts, internal notes, or private contacts.
5. Add a review gate so imported data is checked before publication.

**Output:** structured movie pages that remain safe for a static GitHub Pages website.

## Phase 5 - Discovery, trust, and machine-readable files

**Goal:** improve search, sharing, and future agent onboarding after public content is substantial.

- Add per-page social preview images and review Open Graph metadata.
- Add Organization, Event, FilmFestival, and Movie schema where facts are verified.
- Add a reviewed public XML sitemap configuration when the route set is stable.
- Add `AGENTS.md` with concise repository instructions once the content/build conventions settle.
- Add link checking, HTML validation, and redirect verification to CI.

**Output:** technically discoverable pages without publishing private project planning.

## Phase 6 - Launch and domain

**Goal:** move from the temporary GitHub Pages project URL to `bitcoinfilmfest.com` deliberately.

1. Confirm DNS access and target records.
2. Update Jekyll production URL/base URL configuration.
3. Add the `CNAME` file only when DNS is ready.
4. Verify HTTPS, canonical tags, social previews, redirects, and analytics after deployment.

**Output:** verified custom-domain launch.
