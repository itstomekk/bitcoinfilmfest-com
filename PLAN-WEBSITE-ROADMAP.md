# Bitcoin FilmFest website roadmap

**Written:** 2026-08-31
**Status:** agreed direction, Phase 0/1 foundation and the first Cinema ecosystem release verified on `main` at `517c87f`; Phase 2 content work is now active. The next iteration starts with historical festival extraction from the curated Notion material and then expands the film catalogue in small, source-backed batches. Owner brain-dump questions are part of every iteration.
**Website:** `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\`
**Private source:** `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\`

## 1. Product boundary

The website is a public projection of Bitcoin FilmFest, not the complete project database.

The private BFF knowledge base may contain contacts, sponsor history, outreach status, permissions, research uncertainty, internal notes and operational tasks. The website may contain only deliberately selected and publication-safe material: verified public facts, approved editorial framing, selected films and companies, public links, approved media and current public event information.

There must be no build-time import from `Claude news` into Jekyll. A curator translates approved records into website files and keeps the private provenance in the private knowledge base.

## 2. First gate - reconcile before building more

The next website agent must first check:

- current `git status`, branch and recent commits;
- whether `HANDOFF-CURRENT.md` still describes the checkout accurately;
- the actual status of the `/cinema/` foundation;
- whether `docs/context/` contains public-safe files only;
- whether the real Jekyll build command works on the current machine or must be run through the documented Windows/Ruby environment or GitHub Actions;
- whether unrelated local modifications must be kept out of the next commit.

A stale handoff must be corrected before new feature work begins.

## 3. Roadmap

### Phase 0 - Stabilize the current foundation

Goal: prove that the current website checkout builds and the existing cinema foundation renders correctly.

Tasks:

- reconcile the current Git state with `HANDOFF-CURRENT.md`;
- run the documented Jekyll build from `site/`;
- smoke-test `/cinema/`, the film detail page and the company detail page;
- check desktop, mobile, keyboard focus and reduced-motion behavior;
- verify there are no private emails, CRM fields or internal research tags in public source files;
- commit only the intended coherent change through the repository's normal branch/PR workflow.

Acceptance criteria:

- build passes, or the external build limitation is documented with a successful alternative check;
- the overview, index rows, detail pages and back-links work;
- no unrelated local changes are included;
- the handoff reflects reality.

### Phase 1 - Make the public information architecture coherent

Goal: make the public site explain BFF clearly before expanding the database.

Core public areas:

- Home
- About / what Bitcoin FilmFest is
- Editions / festival history
- Cinema ecosystem overview
- Films directory
- Companies and projects directory
- Reel / Chronicle / news
- Credits and contact/call-to-action pages

Tasks:

- reconcile navigation labels and hierarchy;
- make the distinction between the Warsaw festival, BFF Minis and travelling cinema clear;
- link historical video material where it is public and verified;
- keep the shared cinema frame and existing visual system intact;
- avoid introducing generic card grids when the design system calls for programme/showtime rows.

Acceptance criteria:

- a first-time visitor can understand what BFF is, what Bitcoin Cinema means and where the festival operates;
- every primary navigation item has a real destination;
- historical claims have a private provenance note or public source.

### Phase 2 - Curated cinema database

Goal: grow the `/cinema/` section in small, reviewable batches.

Tasks:

- add the strongest films with clean public sourcing first;
- add companies only when they are genuinely part of film production, distribution or funding;
- keep one entry per entity and use stable slugs;
- cross-link films and companies only after both records exist;
- process approximately 10-20 records per review batch;
- keep unsourced, disputed and unverifiable entries out of the public website until cleared;
- decide once how Bitcoin-adjacent films should appear, then apply that decision consistently.

Acceptance criteria:

- each entry has a working profile page;
- each entry uses the schema in `site/_cinema-schema.md`;
- each entry has public sources and no private research notes;
- a reviewer can trace the public entry back to a private source record without exposing the private record publicly.

### Phase 3 - Event history and roadshow stories

Goal: turn the project history into useful public storytelling, not only database rows.

Priority stories:

- BFF Warsaw editions;
- Lugano Cinema Room and compact programme;
- Lisbon Mini;
- Madeira / Funchal Mini;
- South Africa / Cape Town Mini;
- other verified conference collaborations and roadshow appearances.

For each story, verify:

- place and date;
- what actually happened versus what was only planned;
- programme format;
- confirmed films and guests;
- public photos, videos or announcements;
- why the event mattered to the development of Bitcoin Cinema.

Do not publish draft Notion running orders as final attendance or screening records.

### Phase 4 - Current activity

Goal: show that Bitcoin Cinema is an active ecosystem.

Tasks:

- add a curated cinema news feed from the private news log;
- add an in-production/upcoming strip with explicit status labels;
- distinguish released, upcoming, in production, development and historical material;
- include public media links and source dates;
- prefer useful editorial selection over dumping every research record.

Acceptance criteria:

- a visitor can see both the history and current movement of the ecosystem;
- dates and statuses are not presented as current unless they have been checked;
- news items do not expose private research commentary.

### Phase 5 - Discovery and trust

Goal: improve usefulness after there is enough public content to justify it.

Tasks:

- add simple filtering and sorting;
- add site search if the collection volume warrants it;
- add `Movie` and `Organization` schema.org markup where facts are verified;
- add visible last-updated dates;
- add Open Graph/social preview images;
- add lazy trailer embeds with accessibility and reduced-motion care;
- test routes, links, mobile layout and keyboard navigation.

Do not build complicated search infrastructure before the content model and public curation workflow are stable.

## 4. Public entry review gate

Before a private record becomes a website entry, the curator must answer:

1. Is the entity in scope for Bitcoin FilmFest and Bitcoin Cinema?
2. Is the claim supported by a public source or a clearly publishable BFF record?
3. Is the date/status confirmed, or is it explicitly labelled as historical or planned?
4. Are the names, roles, titles and URLs correct?
5. Does the entry contain private contact data, internal tags, outreach status, permissions or unresolved research notes?
6. Is there a reason this belongs on the website now?
7. Does the entry link to existing public records instead of creating a duplicate?

If any answer is unclear, keep the record private and put the question in `UNCERTAINTY.md`.

## 5. What is deliberately deferred

- merging the many CRM databases into one CRM;
- automatic synchronization from Notion;
- build-time importing from the private knowledge base;
- publishing every person, sponsor, partner or contact;
- adding a public sponsor database without an explicit editorial decision;
- complicated filtering/search before the collection has enough content;
- custom domain changes until Tomek asks for them.

## 6. Working rhythm

Use small, independently reviewable batches:

1. choose one content batch;
2. verify source records and public eligibility;
3. add the website files;
4. run structural checks and a real build;
5. visually review the affected routes;
6. open one coherent PR or commit;
7. update the website handoff and private organization log.

The objective is not to transfer the entire private project into the website. The objective is to make the website the clearest, safest and most useful public expression of the project.
