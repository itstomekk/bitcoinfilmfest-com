# HANDOFF — Bitcoin FilmFest Jekyll Rebuild (session 3, round 3 nav/credits pass)

Date: 2026-08-28
Project: Hermes desktop project "Bitcoin FilmFest" (slug `bitcoin-filmfest`, id `p_5da04a06`), anchored at
`C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll`
Supersedes: `HANDOFF.md` (original scaffold brief), `HANDOFF-SESSION-2.md` (round-2 redesign handoff).
Site root: `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\site`

## Where things stand — short version

The Jekyll scaffold builds and serves cleanly. Three rounds of work are complete and machine-verified:

- **Round 1** (basic shared shell: footer, black ending, logo-home, responsive) — accepted by user.
- **Round 2** (real brand assets, blue hero, cinema-screen depth/pattern, credits page, hover-unfolding edition menu, active-nav highlighting, soft page transitions, sitemap page, modularity) — **user reviewed screenshots and said "much better!"** — accepted with follow-up notes.
- **Round 3** (this session — user's follow-up notes from round 2): thinner/dimmer nav bar with left-side current-page indicator, rabbit repositioned bottom-right, sitemap removed from primary menu, new menu structure (Storyboard / Festivals / Reel / Credits / Contribute), end-credits auto-scroll on the Credits page — **implemented and CDP-verified this session, NOT yet shown to or approved by the user.**

## What was just done (round 3, this session)

1. **Nav bar made thinner and dimmer** (`tokens.css`, `assets/css/cinema-frame.css`):
   - `--nav-height` reduced from `clamp(3.75rem, 7vh, 4.5rem)` to `clamp(2.75rem, 5.5vh, 3.375rem)`.
   - Logo wordmark/mark shrunk to match (1.5rem instead of 2.35rem).
   - Menu items now render at `color-mix(... 46%, transparent)` by default (dim) and light up to full brightness on `:hover`/`:focus`/`.active` — was 70% opacity before, now properly dim-by-default per the user's request.

2. **New left-of-menu "current page" indicator** (`_includes/nav.html`, CSS `.nav-current`):
   - Sits directly right of the logo, desktop only (`min-width: 52rem`).
   - Shows the current page's label (small dot + text, e.g. "Home", "Storyboard", "BFF'26"), driven by a new `nav_label` front-matter field (falls back to `page.title`).
   - It is itself a link: `href="#main-content"` — clicking it jumps to the top of the page, per the user's request ("anchor link to the top").
   - Updates automatically on soft page navigation: `main.js` now dispatches a `bff:pagechange` custom event after every DOM swap, and the nav-current label re-syncs from the fetched document's own `[data-nav-current-label]` text.

3. **Rabbit repositioned to bottom-right of the hero** (`cinema-frame.css` `.home-hero` / `.home-rabbit`):
   - Was centered/left-ish before; now `position: absolute; inset-inline-end: 0; inset-block-end: 0;` inside the (now `position: relative`) `.home-hero`, matching the user's memory ("rabbit was sitting in bottom right").
   - Verified via CDP: rabbit's right/bottom edges sit within 40px/60px of the hero's own right/bottom edges at 1440px.
   - **Known minor issue**: the rabbit's camcorder/popcorn slightly overlaps the "Rewind" showtime-row text on desktop. Low-risk visual polish item, not fixed yet — flagged for the user or next session.

4. **Menu restructured to the user's exact spec** (`_data/navigation.yml`, `_includes/nav.html`):
   - **Storyboard** → `/about/` (was "About"; the About page's `title`/`nav_label` and `screen` were updated to match — now uses the paper screen instead of default).
   - **Festivals** → dropdown containing BFF'27, BFF'26, BFF'25, and a **new BFF'24 page** (`24.md`, `/24/`) built from real BFF'24 dates (19–21 April 2024, European Halving Party at Kinoteka — sourced via web search since no local BFF'24 page existed yet).
   - **Reel** → dropdown containing Newsletter / Press / Blog, all pointing at anchors on a **new consolidated `/reel/` page** (`reel.md`). The Newsletter section pulls real entries from the `site.newsletters` collection (currently just Summer 2024); Press and Blog sections have honest "migration in progress" placeholders linking to `/sitemap/` rather than fabricated content.
   - **Credits** → `/credits/`, unchanged route.
   - **Contribute** → `/join/`, unchanged route, still styled as the CTA.
   - **Site map removed from the primary menu entirely**, per explicit instruction ("dont add site map as menu"). It still exists as a page (`/sitemap/`) and is still linked from the shared footer only — not from the top nav.
   - All edition pages (26.md, bff25.md, 27.md, 24.md) had their internal "Site map" cross-links replaced with "Reel" links, since sitemap is no longer a primary nav destination.

5. **End-credits auto-scroll on the Credits page** (`assets/js/credits-roll.js`, new file, wired into `_layouts/default.html`):
   - After a 900ms pause on page load (or after a soft-navigation into `/credits/`), the credits roll drifts upward automatically via `requestAnimationFrame` + `window.scrollBy`, like a film's closing credits — the exact behavior the user asked for ("scrolling smoothly with user as end credits after movie").
   - **Permanently stops on any real user input** — wheel, touch, keydown, or pointerdown — via one-shot event listeners, so it never fights a reader who wants to scroll manually. This was explicitly designed to feel considerate, not gimmicky.
   - **Fully respects `prefers-reduced-motion: reduce`** — checked before ever scheduling the auto-scroll; if the user's OS/browser has reduced motion on, the page behaves as a normal static page.
   - Re-arms itself after every soft navigation via the same `bff:pagechange` event added for the nav-current-label sync, so navigating away from and back to `/credits/` restarts the effect correctly.
   - Auto-stops when it reaches the bottom of the page (no infinite scroll past content).
   - The credits data itself is unchanged from round 2 — real 85 entries across 5 sections (Crew, Support crew, Production Partners, Associate Producers, Special Cameos), sourced from the original `website/static-site/credits/index.php` and stored in `_data/credits.json`.

## Verification performed this session

- `bundle exec jekyll build --trace` — exits 0, no errors.
- HTTP spot-check on 4 new/changed routes (`/`, `/credits/`, `/reel/`, `/24/`) — all 200.
- **Real CDP browser test** (`C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\verify_round3.py`, reusable, run against headless Chrome on port 9224) at both 1440×1000 desktop and 390×844 mobile:
  - Nav bar height confirmed ≤56px (was ~72px before) — **PASS**.
  - Rabbit confirmed within 40px (right) / 60px (bottom) of the hero's own edges — **PASS**.
  - Left-side current-page indicator confirmed visible, showing "Home" with `href="#main-content"` on the homepage — **PASS**.
  - Menu label order confirmed exactly `["Storyboard", "Festivals", "Reel", "Credits", "Contribute"]` on both desktop and mobile — **PASS**.
  - "Site map" confirmed absent from the primary nav on both desktop and mobile — **PASS**.
  - Hovering a dim nav link over a real pointer-moved event confirmed a computed-style color change (dim → bright) — **PASS**.
  - Clicking Festivals → BFF'24 via real clicks confirmed a soft navigation (no full page reload — `navigationEntries === 1`) and the current-page label correctly updated to "BFF'24" — **PASS** (an early test script had a straight-quote/curly-quote string mismatch that made it look like a failure; the actual browser-reported value in the JSON output was the correct `"BFF'24"` — confirmed correct on manual read).
  - Credits auto-scroll: **confirmed the code path is sound but the automated headless-Chrome test environment itself reports `prefers-reduced-motion: reduce` by default**, so the script correctly refused to auto-scroll in that test run — this is the intended reduced-motion behavior, not a bug. Manually reviewed the JS logic line-by-line to confirm: it checks `prefersReduced.matches` before scheduling, uses `requestAnimationFrame` for smooth per-frame movement, stops permanently on the first real wheel/touch/key/pointer event via `{ once: true }` listeners, and stops at the true bottom of the page. **This should be spot-checked once in a normal (non-automation) browser with standard motion settings before final sign-off**, since the automated harness couldn't exercise the "motion allowed" path end-to-end.
  - Zero console errors, zero failed network requests, zero JS exceptions across the whole desktop+mobile sequence.
  - Screenshots saved: `C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\round3-home-desktop.png`, `round3-credits-autoscroll.png`, `round3-home-mobile.png`.
- Visually reviewed both new screenshots via `vision_analyze`: confirmed thin nav, dim/lit menu labels, working left current-page indicator, correct bottom-right rabbit placement (with the minor overlap noted above), and a correctly-populated mobile menu with no Site map entry.

**What has NOT been done**: the round-3 screenshots have not yet been shown to the user in this session (they will be attached in the same chat turn as this handoff). The minor rabbit/showtime-row overlap has not been fixed. The credits auto-scroll effect has not been manually eyeballed in a real (non-headless, non-reduced-motion) browser session — only its code logic was reviewed.

## Deployment readiness — what's needed to push to GitHub for a friend to edit

**Short answer: yes, this is deployable to GitHub Pages today, and yes, a collaborator can edit pages with custom design in this Jekyll setup — but a few concrete steps remain before "push and share" is turned into reality.** Details below.

### What already works in favor of a clean handoff to a collaborator

1. **Standard Jekyll + GitHub Pages compatible stack.** `Gemfile`/`Gemfile.lock` pin `github-pages` gem (v232) and Jekyll 3.10.0 — the exact versions GitHub Pages' own build infrastructure uses, so `git push` to a `gh-pages`-style setup (or GitHub Pages' native Jekyll build from `main`) should "just work" without a custom Actions workflow, though a custom Action is also fine and more flexible if wanted.
2. **Modular, documented architecture** — a friend does not need to touch layout/CSS files to make routine edits:
   - Menu structure: edit `_data/navigation.yml` only.
   - Credits roster: edit `_data/credits.json` only.
   - Site map roster: edit `_data/sitemap.json` only.
   - New pages: drop a `.md` file with front matter (`layout: default`, `title`, `nav_label`, `permalink`, `screen: blue|paper`) at the site root — the shared shell (logo, nav, footer, cinema bezel, seats, black ending) is automatic, nothing to duplicate.
   - New newsletters: drop a `.md` file into `_newsletters/` — automatically picked up by the Reel page's newsletter list and gets its own dated route.
   - Design system is documented in `site/design.md` (locked tokens, spacing scale, cinema-screen spec, nav spec, footer spec, motion easings) and `tokens.css` (the actual CSS custom properties) — a friend making a **custom-design page** can follow `design.md` and reuse `tokens.css` variables instead of guessing colors/spacing, and it's written specifically to be handed to a second person.
   - `site/README.md` documents the verified Windows/Ruby 3.3 local build workflow.
3. **Real local build verified repeatedly this session and prior sessions** — `bundle exec jekyll build --trace` exits 0, `bundle exec jekyll serve` works, no missing gems, no broken includes.

### What is genuinely missing before "push to GitHub" is real

1. **No Git repository exists yet.** `search_files` for `.git` in the project root returned zero matches this session. This needs to be created (`git init`, initial commit) before anything can be pushed anywhere. This is a deliberate gap — HANDOFF.md's original staged plan explicitly deferred GitHub/deployment work until the shell was visually accepted, which just happened this session.
2. **No GitHub remote/repository has been created or chosen.** Need to decide: new repo under your account/org, public or private, and whether it becomes the official `bitcoinfilmfest.com` custom-domain GitHub Pages site or a staging/preview repo first.
3. **No GitHub Pages / custom domain wiring has been done.** For `bitcoinfilmfest.com` (or a subdomain) to serve this Jekyll build via GitHub Pages: a `CNAME` file needs to be added to the site root with the domain, DNS needs an `A`/`ALIAS`/`CNAME` record pointing at GitHub Pages, and GitHub's repo settings need Pages enabled pointing at the right branch/folder. None of this exists yet — it's genuinely a "next phase" task, not something silently missing from what's built so far.
4. **Collaborator access/permissions** — once a repo exists, your friend needs to be invited as a collaborator (or work via fork+PR, which also works fine with this setup and might be safer for a first pass).
5. **Bulk content migration is still ~40 pages deep** (newsletters, interviews, press articles, special-project pages) — all catalogued honestly in `/sitemap/` as "planned" with their exact original source paths. This is NOT a blocker for pushing the current shell + implemented pages to GitHub — a partially-migrated site is a completely normal, safe thing to deploy incrementally — but it's worth setting expectations that the site won't have 100% of the old content on day one.
6. **`services.subscribe_endpoint` / real subscribe backend** is still a static npub/email fallback (`assets/js/subscribe.js`, unchanged since round 1) — fine to ship as-is, but flagged so it's not mistaken for a working mailing-list signup.
7. **Logo/rabbit asset reconciliation flagged in round 2** — three parallel research agents found that the exact assets live on the /26 and /27 microsites (`bff-logo.png` 800×268, `rabbit.png` 600×834 seated-in-chair pose) might be slightly different files from the ones currently wired into `nav.html`/`index.md` (`bff-logo-flat.png` 4574×1530, `mr-rabbit.png` 193×212 camcorder pose). The user has now seen and approved the current rabbit in round 2 review ("rabbit was sitting in bottom right" — a positioning note, not an asset swap request), so this is likely resolved/moot, but worth a final visual confirmation once round 3 is reviewed.

### Recommended path to "push and share" (in order)

1. Get round-3 sign-off from the user (nav thinness/dimness, current-page indicator, rabbit position, new menu, credits auto-scroll).
2. `git init` in `rebuild-jekyll/` (or just `site/` — decide the repo root; recommend the whole `rebuild-jekyll/` folder so `HANDOFF.md`/`PLAN.md`/this file travel with the code as documentation, with `site/` as the actual Jekyll root GitHub Pages builds from — GitHub Pages supports building from a subfolder via repo settings).
3. Add a `.gitignore` for `_site/`, `.jekyll-cache/`, `.jekyll-metadata` (Bundler/Ruby artifacts already handled — `Gemfile.lock` is deliberately tracked for reproducibility, per round-1 decision).
4. Create the GitHub repository (ask user: public or private, name, personal account or org).
5. Push initial commit.
6. Decide GitHub Pages source (native Pages Jekyll build vs. a GitHub Actions workflow — Actions gives more control if custom plugins are ever needed beyond the `github-pages` gem's whitelist).
7. If deploying to the real `bitcoinfilmfest.com` domain: add `CNAME` file + DNS changes (needs the user's DNS provider access — cannot be done by the agent alone).
8. Invite the friend as a collaborator (or set up fork+PR flow).
9. Only after the above: resume bulk content migration per the original PLAN.md staged approach, or let the collaborator start building custom-design pages using `design.md`/`tokens.css` as their style guide.

**None of steps 2–8 have been started this session** — this session's work was entirely local-only redesign iteration per explicit user direction to verify visually before touching GitHub. The user's current message asks for a plan and readiness check, which this section answers; actual repo creation/push should happen only after explicit go-ahead, since it's a one-way, externally-visible action (unlike everything done so far, which stayed local).

## Known gaps / open items for the next agent or session

1. **Round 3 has not been shown to the user yet** — screenshots exist, need to be surfaced in this chat turn.
2. **Rabbit/showtime-row minor visual overlap** at desktop 1440px — small polish fix, not urgent.
3. **Credits auto-scroll needs one real (non-automated) browser spot-check** — the automated CDP harness's default reduced-motion setting prevented exercising the "motion enabled" code path end-to-end, though the code was manually reviewed and looks correct.
4. **No Git repo / GitHub remote exists** — first real step of the deployment phase, pending user go-ahead per the plan above.
5. **Sitemap data (`_data/sitemap.json`) still needs reconciliation** with the more complete route list a research subagent found in round 2 (redirects like `/26/laurels/` → `/logos/`, live pages like `BFF26-guest-page/audiencevote/` not yet catalogued). Not blocking, but should happen before/soon after deployment so `/sitemap/` stays accurate.
6. **Mobile width (390×844) is now verified for round 3** (this session) — nav toggle, mobile menu open/close, and label correctness all confirmed via CDP. Round-2-era mobile gap is now closed.
7. **~40 "planned" pages remain unmigrated** (newsletters, interviews, special projects) — expected, deferred by design; see sitemap for the full list with exact source paths.
8. **`services.subscribe_endpoint`** and full subscribe-form state coverage (loading/error/duplicate-submit) still not implemented — static fallback only.
9. **Server management**: this session's jekyll serve background process is `proc_8e0455d1a46f`, confirmed responding 200. Does not survive a Hermes app restart — check `process(action='list')` before assuming it's still up.

## Key file map for orientation (updated for round 3)

```
rebuild-jekyll/                       <- recommended git repo root
  HANDOFF.md                          <- original scaffold brief
  PLAN.md                             <- architecture and migration plan
  HANDOFF-SESSION-2.md                <- round-2 handoff (superseded by this file for current state)
  HANDOFF-SESSION-3.md                <- this file
  site/                                <- Jekyll site root (GitHub Pages build root)
    design.md                          <- locked design system, hand this to a collaborator doing custom pages
    tokens.css                         <- canonical design tokens (OKLCH colors, spacing, easings, --nav-height)
    _config.yml                        <- Jekyll config; newsletters collection now sets nav_label/screen defaults
    _data/
      navigation.yml                    <- SINGLE SOURCE OF TRUTH for menu + footer links — edit here for menu changes
      sitemap.json                       <- site map data (needs reconciliation, see gap #5)
      credits.json                       <- 85 credits entries across 5 sections — edit here for roster changes
    _layouts/default.html               <- shared page shell; wires main.js, credits-roll.js, subscribe.js
    _includes/
      nav.html                           <- logo, left current-page indicator, Storyboard/Festivals/Reel/Credits/Contribute menu
      footer.html                        <- shared black-ending footer (still includes Site map link)
      head-meta.html                     <- meta/title/favicon/theme-color (per-page `screen: blue|paper`)
    assets/
      css/cinema-frame.css               <- full visual system: nav, bezel shadow, top pattern, seats, screens, credits roll
      js/main.js                         <- soft page transitions, active nav state, dispatches bff:pagechange event
      js/credits-roll.js                  <- NEW this session: end-credits auto-scroll for /credits/
      js/subscribe.js                     <- static npub/email fallback (unchanged)
      images/brand/                       <- bff-logo-flat.png, bff-logo-mark-white.png
      images/legacy-home/                 <- mr-rabbit.png (now bottom-right positioned), bff-home-parallax.png
      images/newsletters/summer-2024/     <- 7 recovered newsletter images
    index.md, about.md (Storyboard), credits.md, sitemap.md, join.md, reel.md (NEW), 27.md, 26.md, bff25.md, 24.md (NEW)
    _newsletters/2024-06-19-summer-2024.md  <- only implemented newsletter, feeds into /reel/#newsletter

C:\Users\Lenovo\AppData\Local\Temp\bff-rebuild\        <- one-off recovery/build scripts (reusable)
C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\   <- CDP verification scripts + screenshots (round 2 + round 3)
```

## How to resume verification quickly

```bash
# Build
C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace

# Serve (background) — use terminal(background=true, notify_on_complete=true):
unset MSYS2_ARG_CONV_EXCL MSYS_NO_PATHCONV && 'C:/Ruby33-x64/bin/jekyll.bat' serve --host 127.0.0.1 --port 4000 --trace

# Confirm it's up
curl --fail --silent --show-error --max-time 10 http://127.0.0.1:4000/ -o /dev/null -w "%{http_code}\n"

# Re-run the round-3 CDP interaction suite (needs its own headless Chrome on 9224):
# 'C:/Program Files/Google/Chrome/Application/chrome.exe' --headless=new --disable-gpu --no-sandbox \
#   --remote-debugging-port=9224 --remote-allow-origins='*' \
#   --user-data-dir='C:/Users/Lenovo/AppData/Local/Temp/bff-chrome-redesign' about:blank
python 'C:/Users/Lenovo/AppData/Local/Temp/bff-jekyll-verify/verify_round3.py'
```

## Recommended next steps (priority order)

1. Show round-3 screenshots to the user, get sign-off on: thinner/dimmer nav, left current-page indicator, rabbit bottom-right placement, new Storyboard/Festivals/Reel/Credits/Contribute menu, and the end-credits auto-scroll concept.
2. Fix the minor rabbit/showtime-row overlap if the user flags it.
3. Spot-check the credits auto-scroll manually in a normal browser (not headless/automation) to visually confirm the drift feels right (speed, pause point, restart behavior).
4. On explicit go-ahead: `git init`, create `.gitignore`, create the GitHub repo, push, decide Pages source, invite the collaborator — see the "Recommended path to push and share" section above for the full sequence.
5. Reconcile `_data/sitemap.json` with the more complete route list from round-2 research.
6. Resume staged content migration per PLAN.md, or hand the design.md/tokens.css style guide to the collaborator to start building custom pages.
