# Bitcoin FilmFest website roadmap

**Written:** 2026-08-31
**Status:** agreed direction, Phase 0/1 foundation and the first Cinema ecosystem release verified on `main`; the historical edition set `/23/`–`/26/` and canonical `/25/` route are now deployed at version `0.6.0`. Phase 2 cinema work and Phase 3 historical enrichment are active. The next iteration mines the private knowledge base and edition photo folders for public-safe additions, then builds out the BFF’27 current-event page in small, source-backed batches. Owner brain-dump questions are part of every iteration.
**Website:** `C:/Users/Lenovo/OneDrive/Bitcoin FilmFest/website/rebuild-jekyll-bff26/`

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

### Phase 3A - Enrich the deployed BFF’23–’25 archive pages

**Status:** next implementation batch. The archive pages are live, but the research pass found additional verified public facts that should be added without changing the shared design language.

Goal: make `/23/`, `/24/` and `/25/` useful historical records rather than minimal festival summaries, while keeping uncertain material explicitly labelled or private.

Workstreams:

- **BFF’25 results and recap:** add the Golden Rabbits winners (No More Inflation, Satoshi: The Creation of Bitcoin, Hotel Bitcoin and Revolución Bitcoin), PoWies winners (Mempool: Grand Prix/Visual; StreetCyber: Identity), Pitching Rabbits winner Jenna Reid / *Network Effect*, and the public Bitcoin News recap metrics (200+ attendees, 20+ countries) with source links and reported-metric wording.
- **BFF’25 voices and press:** add a compact press/voices section linking the published Bitcoin News, Lightning News, The Crypto Radio, Bitvocation, Philip Charter, Bitpopart and Aaron Koenig coverage. Add the public Furious BTC recap only after verifying its title/date and keeping it as an external link.
- **BFF’24 programme detail:** add full director credits where confirmed, public trailer links, *Peru* to the ShortFest context, and the CartoonFest titles *Adventures of Jonathan*, *The Maxis Club Show* and *Bitcoin & Friends*. Add one short Sean McNamara pull quote only if the citation and wording are preserved.
- **BFF’23 credit and source recovery:** add Rémi Forte and Aaron Mucke / Eva Mühlenbäumer to the award records, extract the Polish brochure for possible programme facts, and publish only claims supported by the brochure or first-party evidence.

Rules:

- Do not reconstruct exact historical timetables from campaign drafts.
- Do not turn reported attendance figures into a single total when categories overlap.
- Keep expired ticketing, submission, signup, sponsor-referral and VOD CTAs archive-only or omitted.
- Every addition gets a public source URL or a private provenance note in the edition content map.

Acceptance criteria:

- Each edition page has a tested results/recap section where evidence exists.
- New external links are checked, labelled as historical where appropriate, and open in a new tab with `rel="noopener"`.
- Existing `/23/`, `/24/`, `/25/`, `/26/` routes and shared shell remain regression-safe.
- No private contacts, internal statuses or unresolved research notes enter `site/`.

### Phase 3B - Build the BFF photo and media curation pipeline

**Status:** source discovery active; implementation follows Phase 3A content review.

Goal: use the substantial local BFF photo archive without dumping private, uncredited or unnecessarily large source folders into the public repository.

Source roots to inventory:

- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF23\WK23 zdjęcia od fotografa\`
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF24\` and its EHP / film / partner subfolders
- `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF25\BFF 25 fotki\BFF25\` and `Photos for website\`
- existing public BFF26 photo bundles and any explicitly public BFF27 material

Tasks:

- Create a private inventory for every candidate image: edition, source path, filename, dimensions, checksum, photographer/credit if known, publication permission status, intended crop and alt text.
- Separate public/owner-approved images from private event folders, photographer delivery archives, PSD/source files, screenshots, chat captures and ZIPs.
- Produce resized derivatives for the website, normally 1600–2400 px on the long edge, while preserving the original source outside Git.
- Curate a representative gallery and at least one full-bleed/viewport-width band per edition where the image rights are clear.
- Record uncertain rights and photographer credits in the private review queue; do not publish them merely because they are stored locally.
- Add a validator that checks asset existence, local-only references, image dimensions, byte totals and the source-to-destination manifest.

Acceptance criteria:

- Every published image has a known source path, safe-to-publish status, useful alt text and a documented crop/derivative.
- No full photographer ZIP or unreviewed source archive is copied into the site.
- Desktop and mobile screenshots confirm that photo bands stay full-width inside the cinema viewport without horizontal overflow.
- The asset manifest is small enough for GitHub Pages and reproducible from the source inventory.

### Phase 3C - Build the BFF’27 current-event page

**Status:** `/27/` exists as a skeleton; the public content build is not complete.

Goal: turn `/27/` into the current festival landing page using the shared cinema shell, while keeping private candidate research and operational data out of the public site.

Confirmed public anchor:

- BFF’27 runs **24–27 June 2027 in Warsaw**. Kinoteka / exact companion venues, ticketing, submission window and programme are not to be inferred until confirmed by the owner or a public first-party page.
- `Claude news/BFF27-opis-kinoteka-format.md` is a stale/misnamed BFF’26 description and is not a BFF’27 source. Treat it as historical BFF’26 research until explicitly replaced.

Tasks:

- Replace the current 28-line skeleton in `site/27.md` with a proper current-edition structure: save-the-date hero, what the festival is, participation paths, current status, film call/programme status, and a clearly labelled updates/press area.
- Create `docs/context/BFF27-CONTENT-MAP.md` and an asset manifest before adding claims or images.
- Keep `Claude news/BFF27-ai-upcomingfilms.md` and the BFF27 crosswalk review private. Promote only films with a public source and an explicit editorial reason to appear on the page.
- Start with the confirmed BFF27 candidate pipeline: *Network Effect*, *This Time Is Different*, *What the F*ck Is My Password?!*, *The Buried Bitcoin*, *The Satoshi Affair*, *The Invisible Hand*, *Build on Bitcoin* and other candidates only after status/source review. Candidate status must be labelled as watchlist/editorial context, not selection or commitment.
- Reuse the photo/rights pipeline from Phase 3B and establish a born-in-`BFF27/` asset convention so future campaign images do not become loose root files.
- Add `scripts/check_bff27_page.py` and route/asset tests before any deployment.

Acceptance criteria:

- `/27/` is a useful current page with no stale ticket or submission mechanics presented as live.
- Every public date, venue, film, partner and programme claim has a source and status label.
- No private contacts, warm-lead details, internal candidate scores or campaign operations are published.
- The page passes the shared navigation/footer, asset, mobile overflow, accessibility and Jekyll build checks.

### Phase 3D - Knowledge-base discovery backlog

Run this short scan before each archive or BFF27 batch. The database contains more than the current pages, but it is not a public source by default.

- Search the canonical/evidence registers, Notion exports, legacy page captures, edition folders and public press links for new facts, quotes, trailers and photographs.
- Compare every candidate against the current content map before adding it, so repeated research does not create duplicated or conflicting copy.
- Classify each candidate as `publish`, `publish-with-source`, `owner-review`, `private-only` or `discarded/unsupported`.
- Keep a concise list of unresolved questions in the edition content map or private uncertainty log rather than burying them in page copy.

This backlog is deliberately separate from automatic Notion import. The curator remains the publication gate.

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
