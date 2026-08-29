# Historical Handoff - Bitcoin FilmFest Jekyll Rebuild (session 2)

> **Historical session record (2026-08-28).** This captures the redesign/asset-recovery point in time. It is not the live operating manual; start with `BUILDER-GUIDE.md`, `BUILD-LOG.md`, and `site/README.md`.

Date: 2026-08-28
Prior handoff: `HANDOFF.md` (original scaffold brief) — this file supersedes it for current state.
Project root: `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll`
Site root: `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\site`

## Where things stand — short version

The Jekyll scaffold builds and serves cleanly. Round 1 (basic shared shell: footer, black ending, logo-home, responsive) was verified and accepted. Round 2 — the user's detailed redesign feedback (real brand assets, blue hero, cinema-screen depth/pattern, credits page, hover-unfolding edition menu, active-nav highlighting, soft page transitions, sitemap, modularity) — has been implemented and machine-verified via CDP, but **has not yet been re-confirmed by the user visually**. Say so plainly if you pick this up: it works, it hasn't been eyeballed and approved yet.

## What was just done (this session, after compaction)

1. **Recovered real brand assets** from `website/rebuild-jekyll/site-mirror.tar.gz`-style archive at `C:\Users\Lenovo\AppData\Local\Temp\bff-rebuild\site-mirror.tar.gz` (a wayback/legacy mirror) and from `BFF26-guest-page/26-assets/`, `logos-page/laurels-assets/`:
   - `site/assets/images/brand/bff-logo-flat.png` (4574×1530, horizontal wordmark+mark) — now the nav/footer wordmark.
   - `site/assets/images/brand/bff-logo-mark-white.png` (530×530 aperture mark) — compact brand mark.
   - `site/assets/images/legacy-home/mr-rabbit.png`, `mr-rabbit-logo.png`, `bff-home-parallax.png` — recovered rabbit + old blue parallax background reference.
   - `site/assets/images/newsletters/summer-2024/*.png` — 7 real newsletter images (spotlight, love-is-bitcoin banner, recent-updates, films, monthly-highlight, money-money-money, mr-rabbit), replacing the dead `bitcoinfilmfest.com/wp-content/...` URLs in `_newsletters/2024-06-19-summer-2024.md`.
   - Recovery scripts (reusable if more assets are needed): `C:\Users\Lenovo\AppData\Local\Temp\bff-rebuild\recover_mirror.py`, `recover_newsletter_assets.py`.

2. **Rebuilt the design system as a locked, documented spec**:
   - `site/design.md` — full Hallmark-style design.md (genre, macrostructure, theme OKLCH tokens, typography, spacing, cinema-screen spec, nav spec, footer spec, motion, CTA voice, modularity notes, multi-format token exports).
   - `site/tokens.css` — canonical token file (project root, imported by page CSS). Includes room/screen/paper/ink/accent colors in OKLCH, spacing scale, cinema-frame dimensions (`--frame-side`, `--frame-bottom`, `--nav-height`), easings.
   - `site/.hallmark/log.json` — diversification/project-memory record for future design work.

3. **Rebuilt shared shell** (all in `site/_includes/` and `site/_layouts/default.html`):
   - `nav.html` — real logo (wordmark + mark) linking to `/`, edition items (`BFF'27`, `BFF'26`, `BFF'25`) grouped under an "Editions" `<details>`/`<summary>` disclosure that **opens on hover AND `:focus-within` on desktop, and via native tap on mobile** (no hover-only trap). Active-page detection via `data-route` + JS (`main.js`) marks the current page/group in blue with `aria-current="page"`.
   - `footer.html` — one shared footer, room-black background, includes logo, statement, nav/footer links from `_data/navigation.yml`, social, sitemap link, copyright. Ends flush on black — verified via CDP that `footerBg === bodyBg` at true scroll bottom.
   - `_data/navigation.yml` — single source of truth for nav + footer links (replaces the old inline arrays in `_config.yml`). Edit this file to change menu structure without touching templates.
   - `default.html` — wires everything together, includes `data-page-main` wrapper (the soft-navigation swap target), skip link, `#main-content`.

4. **Cinema-screen visual depth** (`assets/css/cinema-frame.css`, full rewrite, ~28KB):
   - Inner bezel shadow (`box-shadow: inset ... var(--color-room)`) — gives the screen physical depth without a grey tail.
   - Small film-perforation pattern (`repeating-linear-gradient`) along the screen's top edge.
   - Fixed cinema seats stay pinned to the true bottom edge (preserved from round 1).
   - Blue screen (`stage--blue`) for home/edition pages using the recovered brand blue; warm paper screen (`stage--paper`) for reading pages (about, credits, sitemap, join, newsletters).

5. **New pages**:
   - `site/credits.md` (`/credits/`) — built from `website/static-site/credits/index.php`, now in shared shell, in nav footer.
   - `site/sitemap.md` (`/sitemap/`) — human-readable site map driven by `_data/sitemap.json` (also built this session — 64 discovered routes classified: implemented/planned/redirect-candidate/excluded).
   - `site/27.md`, `site/26.md`, `site/bff25.md` — edition landing pages, blue screen, cross-link to sitemap/join instead of dead placeholder links.
   - `site/join.md` — contribute page, paper screen.
   - Homepage (`site/index.md`) rewritten: blue screen, real rabbit + logo, no generic "Next Edition" cards — programme/showtime-style rows instead, per user's explicit complaint about the too-generic card blocks.

6. **Soft page transitions** (`assets/js/main.js`, full rewrite):
   - Same-origin link clicks are intercepted, fetch the target HTML, swap only `[data-page-main]`, use View Transitions API when available (`document.startViewTransition`), fall back to instant swap otherwise, full page load as ultimate fallback on fetch failure.
   - Nav/footer/logo/bezel/seats **stay mounted** across navigation — verified via a DOM sentinel (`window.__bffShellSentinel`) that survives multiple soft navigations with `performance.getEntriesByType('navigation').length === 1`.
   - Active-nav state, `aria-current`, and edition-group highlighting update on every soft navigation.
   - Respects `prefers-reduced-motion`.

7. **Config cleanup**: `_config.yml` now excludes `design.md`, `.hallmark/`, `SITEMAP-PLAN.md` from the Jekyll build output (they were leaking into `_site/` as raw pages before this was added).

## Verification performed this session

- `bundle exec jekyll build --trace` — exits 0.
- Static HTTP/DOM assertion suite (execute_code, urllib+HTMLParser) — 32/32 checks passed: single footer/nav/main per page across 10 routes, all shell links 200, all key assets load with real bytes, `design.html` correctly 404s (excluded), CSS contains the black-footer token, inset bezel shadow, perforation pattern, `.nav-link.active` rule, and reduced-motion query.
- **Real CDP browser interaction test** (`C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\verify_redesign_interactions.py`, run against a dedicated headless Chrome on port 9224 — reusable script) at 1440×1000:
  - No horizontal overflow.
  - Real logo + rabbit assets load with nonzero natural dimensions.
  - Hovering the Editions summary opens the dropdown (`opacity:1`, `visibility:visible`, `pointerEvents:auto`).
  - Clicking the summary also opens the native `<details>` disclosure (touch/keyboard path).
  - Clicking `/26/` inside the dropdown performs a **soft navigation** (shell sentinel persists, `navigationEntries === 1`, i.e. no hard reload) and correctly marks both the Editions group and the `/26/` link `aria-current="page"`.
  - Clicking the logo soft-navigates back to `/`.
  - Scrolling to true bottom: footer background equals body background (both `oklch(0.07 0.005 245)`) — confirmed black ending, not grey.
  - Zero console errors, zero failed network requests, zero JS exceptions throughout the whole interaction sequence.
  - Screenshots saved: `C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\redesign-home-desktop.png` and `redesign-home-ending-desktop.png`.

**What has NOT been done**: the two screenshots above have not yet been shown to / approved by the user. Mobile (390×844) has not been re-verified against the *new* redesign (it was verified for round-1 shell only). The `vision_analyze` calls on the two new screenshots were dispatched but their content was not read back into this summary before the session was interrupted by the async delegation batch — re-run `vision_analyze` on those two paths if you need the visual QA description restated.

## Parallel research (async subagent batch, completed, informs next steps but NOT yet applied)

Three subagents ran in parallel and returned before this handoff was written. Full outputs are on disk; read them before doing more visual/asset work to avoid redoing this research:

1. **Visual asset audit** — `C:\Users\Lenovo\AppData\Local\hermes\profiles\webdev\cache\delegation\subagent-summary-0-20260828_125913_446424.txt` (16KB). Confirms canonical assets:
   - Canonical horizontal logo: `BFF26-guest-page/26-assets/bff-logo.png` (800×268) — **note**: this is a *different, smaller* web-optimized lockup than the `bff-logo-flat.png` (4574×1530) I already wired into nav/footer. Worth comparing both visually before deciding which is canonical for the nav — the 800×268 is what was actually used live on /26 and /27 pages.
   - Canonical rabbit: `BFF26-guest-page/26-assets/rabbit.png` (600×834, seated-in-cinema-chair pose, glasses/popcorn/drink) — different pose from the `mr-rabbit.png` I recovered from the mirror archive (Mr Rabbit newsletter mascot, different pose). Byte-identical copy at `_assets\brand\KrolikBFF-web.png`. High-res master: `_assets\brand\KrolikBFF.png` (5073×7051).
   - **Action needed**: compare `bff-logo-flat.png` vs `bff-logo.png` (800×268) and `mr-rabbit.png` vs `rabbit.png` (600×834) visually with the user or via vision_analyze, then standardize on one pair. Right now the homepage may be using a different rabbit pose than what was live on the most recent BFF26/27 microsites.

2. **Full site map** — `C:\Users\Lenovo\AppData\Local\hermes\profiles\webdev\cache\delegation\subagent-summary-1-20260828_125913_447422.txt` (38KB, ~picks up where my own `_data/sitemap.json` build left off, likely more complete/more accurate on redirects). Notable findings not yet reflected in `site/_data/sitemap.json`:
   - `/26/laurels/`, `/26/logo/`, `/26/logos/` are all legacy redirect targets that should 301 to `/logos/` (not "planned" pages as my sitemap.json currently has `/26/laurels/`).
   - `BFF26-guest-page/audiencevote/`, `BFF26-guest-page/wintrezor/`, `BFF26-guest-page/prague/` are live pages not yet in my sitemap.json at all.
   - Recommends excluding `internal://bff26/venue-slides`, `internal://bff26/volunteer`, and three internal print-poster artifacts from the public sitemap.
   - **Action needed**: reconcile this against `site/_data/sitemap.json` (currently 64 routes) — likely needs updating/expanding, and the `/sitemap/` page output should be regenerated after.

3. **Modular architecture recommendations** — `C:\Users\Lenovo\AppData\Local\hermes\profiles\webdev\cache\delegation\subagent-summary-2-20260828_125913_448421.txt` (15KB). Broadly validates the architecture already built this session (`_data/navigation.yml`, shared includes, tokens.css) but also recommends:
   - A dedicated `_includes/brand.html` partial (I inlined the logo markup directly in `nav.html`/`footer.html` instead — low-risk to extract later if the user wants the logo reused in a third place).
   - A `services.subscribe_endpoint` config value (empty by default) in `_config.yml` to make the subscribe form's future backend swap explicit and documented — not yet added.
   - Explicit states for the subscribe form (empty endpoint / mock endpoint / timeout / duplicate-submit) — `assets/js/subscribe.js` currently only has the static npub/email fallback verified in round 1; not re-tested this session.

## Known gaps / open items for the next agent or session

1. **User has not seen the redesign yet.** Do not claim final acceptance. Show screenshots or open the live preview (`http://127.0.0.1:4000/`) and ask for sign-off on: real logo/rabbit choice, blue hero feel, cinema bezel/pattern, hover-unfolding edition menu, active-page highlighting, soft transitions, and the credits/sitemap pages.
2. **Logo/rabbit asset reconciliation** (see subagent finding #1 above) — decide between `bff-logo-flat.png`/`mr-rabbit.png` (currently wired in) vs `bff-logo.png`(800×268)/`rabbit.png`(600×834) (what was live on /26,/27). This is the single highest-value next step since it directly answers the user's "why is there no logo of us, why is there no rabbit" complaint with the *exact* assets they remember.
3. **Sitemap data reconciliation** (see subagent finding #2) — merge the more complete sitemap into `site/_data/sitemap.json`, regenerate `/sitemap/`.
4. **Mobile (390×844) has not been re-verified for the round-2 redesign.** Only desktop 1440×1000 was CDP-tested this session. Re-run `verify_redesign_interactions.py`-style checks at mobile width, particularly the edition-menu (must be native tap-based on mobile, not hover), before calling this done.
5. **`services.subscribe_endpoint` and subscribe-form full state coverage** — not implemented this session; `assets/js/subscribe.js` unchanged since round 1.
6. **The 40+ "planned" pages in the sitemap (newsletters, interviews, special projects) are still unmigrated** — expected, deferred by design per the original PLAN.md staged approach. Do not attempt bulk migration without user direction; it's a large, separate phase.
7. **No GitHub repository or deployment exists yet.** Everything is local-only, matching the original HANDOFF.md constraint to verify before deploying.
8. **Server management**: the jekyll serve background process from earlier in this session (`proc_07ea54d576c8`) exited (exit code 1, likely killed when its terminal tab was closed or the session recycled — the log shows it was serving fine with auto-regeneration before the abrupt stop). A fresh one was started this turn: `proc_9206aa878746`, confirmed responding 200 at `http://127.0.0.1:4000/`. Check `process(action='list')` for current state before assuming it's still up — it does not survive a Hermes app restart.

## Key file map for orientation

```
site/
  design.md                 <- locked design system, read first
  tokens.css                <- canonical design tokens (OKLCH colors, spacing, easings)
  _config.yml                <- Jekyll config; nav/footer data moved OUT to _data/navigation.yml
  _data/
    navigation.yml           <- single source of truth for nav + footer links
    sitemap.json              <- site map data (64 routes; needs reconciliation, see gap #3)
  _layouts/default.html      <- shared page shell
  _includes/
    nav.html                  <- logo, edition hover/focus dropdown, active-state hooks
    footer.html                <- shared black-ending footer
    head-meta.html             <- meta/title/favicon/theme-color (per-page `screen: blue|paper`)
  assets/
    css/cinema-frame.css      <- full visual system: bezel shadow, top pattern, seats, screens
    js/main.js                  <- soft page transitions + active nav state
    js/subscribe.js             <- static npub/email fallback (unchanged this session)
    images/brand/               <- bff-logo-flat.png, bff-logo-mark-white.png (reconcile, see gap #2)
    images/legacy-home/         <- mr-rabbit.png, mr-rabbit-logo.png, bff-home-parallax.png
    images/newsletters/summer-2024/  <- 7 recovered newsletter images
  index.md, credits.md, sitemap.md, join.md, 27.md, 26.md, bff25.md, about.md  <- implemented pages
  _newsletters/2024-06-19-summer-2024.md  <- only implemented newsletter, images now local

C:\Users\Lenovo\AppData\Local\Temp\bff-rebuild\        <- one-off recovery/build scripts (reusable)
C:\Users\Lenovo\AppData\Local\Temp\bff-jekyll-verify\   <- CDP verification scripts + screenshots
```

## How to resume verification quickly

```bash
# Build
C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace

# Serve (background)
# use terminal(background=true, notify_on_complete=true):
unset MSYS2_ARG_CONV_EXCL MSYS_NO_PATHCONV && 'C:/Ruby33-x64/bin/jekyll.bat' serve --host 127.0.0.1 --port 4000 --trace

# Confirm it's up
curl --fail --silent --show-error --max-time 10 http://127.0.0.1:4000/ -o /dev/null -w "%{http_code}\n"

# Re-run the CDP interaction suite (needs its own headless Chrome on 9224):
# 'C:/Program Files/Google/Chrome/Application/chrome.exe' --headless=new --disable-gpu --no-sandbox \
#   --remote-debugging-port=9224 --remote-allow-origins='*' \
#   --user-data-dir='C:/Users/Lenovo/AppData/Local/Temp/bff-chrome-redesign' about:blank
python 'C:/Users/Lenovo/AppData/Local/Temp/bff-jekyll-verify/verify_redesign_interactions.py'
```

## Recommended next steps (priority order)

1. Reconcile logo/rabbit asset choice (gap #2) — highest value, directly answers the user's stated complaint.
2. Show the user the two desktop screenshots (or open `http://127.0.0.1:4000/` in preview) and get explicit sign-off on the round-2 redesign before doing more work.
3. Re-verify at mobile width (390×844), especially the edition menu's tap behavior.
4. Reconcile the sitemap (gap #3), regenerate `/sitemap/`.
5. Only then: resume staged content migration per the original PLAN.md, or move to GitHub/deployment per user direction.
