# Bitcoin FilmFest route reconciliation

This is the builder-safe route inventory for the current Jekyll source. It replaces the older 64/66-route migration estimate, which mixed legacy source URLs with pages that now belong inside the Cinema and Reel hubs.

## Current build counts

- Generated routes: 101
- Public/indexable routes: 89
- Shared core pages: 16
- Compatibility redirect outputs: 11
- Film profiles: 20
- Company profiles: 7
- Newsletter detail pages: 1
- Reel detail pages: 10
- Press room pages: 34 (`/26/press/`, EN/PL hub, info-base and article pages)
- Press kit page: 1 (`/presskit/`)
- Builder-only/private route: 1 (`/effect-lab/`, `noindex, nofollow`)
- Legacy-only routes still requiring a decision: 48 planned rows plus 2 redirect candidates

The generated-route count includes the root route. The public/indexable count excludes `/bff25/` and `/effect-lab/`. The 10 `_chronicle/` files are source notes with `output: false` and produce no routes. The 34 static press-room pages and `/presskit/` are now public outputs copied from the verified local press/branding sources. Private source material is not part of this inventory.

## Current public routes

### Shared core and compatibility output (16 + 11 redirects)

| Route | Source | State |
|---|---|---|
| `/` | `site/index.md` | implemented |
| `/about/` | `site/about.md` | implemented |
| `/23/` | `site/23.md` | implemented |
| `/24/` | `site/24.md` | implemented |
| `/25/` | `site/bff25.md` | implemented, canonical BFF'25 |
| `/26/` | `site/26.md` | implemented |
| `/27/` | `site/27.md` | implemented |
| `/awards/` | `site/awards.md` | implemented |
| `/cinema/` | `site/cinema.md` | implemented, Cinema hub |
| `/cinema/films/` | `site/cinema-films.md` | implemented, film hub |
| `/cinema/companies/` | `site/cinema-companies.md` | implemented, company hub |
| `/credits/` | `site/credits.md` | implemented |
| `/festivals/roadshows/` | `site/festivals-roadshows.md` | implemented |
| `/join/` | `site/join.md` | implemented |
| `/reel/` | `site/reel.md` | implemented, unified Reel archive |
| `/presskit/` | `site/presskit/index.html` | implemented, branding book and downloadable logo/laurel assets |
| `/26/press/` | `site/26/press/index.html` | implemented, restored BFF’26 press room hub |
| `/thanks/` | `site/thanks.md` | implemented |
| `/bff25/` | `site/bff25-legacy.md` | compatibility redirect to `/25/`, not a page |

`/bff25/` and the 10 migrated legacy article routes are listed for link compatibility but are not counted as additional public pages. The canonical public page count is now 89, while the generated build has 101 route outputs including 11 redirects, 34 BFF’26 press-room pages, the `/presskit/` branding book, and the private effect lab.

### Collection routes

- 20 film details under `/cinema/films/<slug>/`, from `site/_films/`.
- 7 company details under `/cinema/companies/<slug>/`, from `site/_companies/`.
- 1 newsletter detail under `/newsletters/2024-06-19-summer-2024/`, from `site/_newsletters/`.
- 10 Reel details under `/reel/<slug>/`, from `site/_reel/`; interviews, guest posts, and the BFF24 event report share this collection.
- 34 BFF’26 press-room pages under `/26/press/`, including the EN/PL hub, info-base, press articles and article stylesheet.
- 1 standalone `/presskit/` branding book with 14 copied public download assets from the verified local `logos-page` source.
- 10 legacy article routes redirect to their corresponding Reel detail; these are `noindex, follow` compatibility outputs, not duplicate content pages.

### Builder-only route

- `/effect-lab/` is a local effect comparison tool. It is deliberately `noindex, nofollow`, should not be promoted in navigation, and must not be treated as public content or a migration target.

## Legacy reconciliation

The legacy map's 48 planned rows are not 48 new top-level pages. Use these destinations when migrating public-safe material:

### Fold into existing hubs or edition pages

| Legacy routes | Destination |
|---|---|
| `/bff24-event-coverage-bitesize-media-may-2024/`, `/bff24-official-selection-freedom-themed-films/` | `/24/` or a Reel entry linked from `/24/` |
| `/26/laurels/` | `/presskit/` |
| `/festival-flashbacks/` | `/reel/` archive, with edition links where relevant |
| `/bff-rabits/`, `/press-and-media/` | `/26/press/` for the restored BFF’26 press room; `/presskit/` for logos and brand downloads |
| `/cinema-digest-monthly-content/`, `/cinematic-hub/`, `/blog/`, `/cinema-digest/`, `/bff-interviews/` | `/cinema/` and/or `/reel/` |
| `/part-one-official-selection-feature-films-at-bff25/`, `/part-two-official-selection-experimental-shorts-at-bff25/` | `/25/` |
| `/wall/`, `/qr/`, `/linktree/`, `/bitcoin-filmfest-2024-european-halving-party-🐇/`, `/european-halving-party-thankyou/`, `/europeanhalvingparty/` | `/24/` |
| `/pow/` | `/awards/` |
| `/26/wintrezor/` | `/26/` |
| `/unique-bitcoin-video-ads/` | `/reel/` |

These are folds, not permission to copy private notes or recreate campaign microsites.

### Separate public pages worth migrating

- Newsletter entries: preserve the original legacy URL as redirect metadata, but publish the content as ordinary Reel entries under `/reel/<slug>/` unless it is explicitly retained as a newsletter detail.
- Individual interviews and features: the first 10 are now ordinary Reel entries under `/reel/<slug>/`; `/bff-interviews/` remains a hub concept, not a second collection.
- `/privacy-policy/`: keep as a separate legal page when verified and public-safe.
- `/authors/tomek-k/`: only create if an author archive is needed after Reel content exists; otherwise fold author links into Reel metadata.

### Redirects

- `/bff25/` -> `/25/` (implemented compatibility redirect; never duplicate the BFF'25 page).
- `/bff26/` -> `/26/` (legacy alias; use a redirect if the old URL is retained).
- `/bff2024/` -> `/24/` (legacy alias; use a redirect if the old URL is retained).
- Legacy individual article, interview, and newsletter URLs should redirect to their Reel entry after migration. Do not create duplicate top-level pages for them.

## Source boundaries and next step

Only reviewed Markdown under `site/` is public source. `_chronicle/` is non-output working material, and private KB/Drive material must stay outside the public repository. The first 10 public-safe Reel entries are now built under `site/_reel/`, with 10 `noindex, follow` compatibility routes preserving their original public URLs.
