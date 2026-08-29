# Historical Handoff - bitcoinfilmfest.com Jekyll rebuild

> **Historical record only (2026-08-28).** This original scaffold brief predates the verified build, expanded pages, GitHub repository, and Pages deployment attempt. Start with `BUILDER-GUIDE.md`, `BUILD-LOG.md`, and `site/README.md` instead.

Updated: 2026-08-28

## Where this stands

We're rebuilding bitcoinfilmfest.com as a static Jekyll site, deployed on GitHub Pages, code on GitHub so others can collaborate. Planning is done, a proof-of-concept scaffold exists locally with 3 real pages migrated. **Nothing has been build-tested or pushed to GitHub yet.** No repo exists. This session had no root access and couldn't install Jekyll to test the build — that's the first job.

## Done this session

- [verified] Full rebuild plan written: `website/rebuild-jekyll/PLAN.md`
- [verified] Jekyll scaffold built at `website/rebuild-jekyll/site/` (17 files) — config, layouts, includes, CSS, JS, 3 sample content pages. Full list below.
- [verified] Cinema-frame design spec captured and implemented in CSS: black margins 3% top / 5% sides / 10% bottom, fixed cinema seats image glued to the bottom edge, full width, applied site-wide via the shared layout. Adapted from the already-working pattern on `/26/`, not invented from scratch.
- [verified] Archive.org content recovery: 6 pages recovered that were missing from the July 2026 site scrape — `website/wayback-recovered-2026-08-28/`.
- [unverified] Whether the site actually builds with `jekyll build` / `jekyll serve`. Sandbox had no root and no `ruby-dev`, so `gem install jekyll` failed on native extensions. Only checked: YAML front matter parses, Liquid `{% %}` / `{{ }}` tags balance, `_config.yml` is valid YAML. That is not the same as a working build.

## What Hermes needs to do

1. **Get the build working first.** Open a terminal in `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\site\`, run `bundle install` then `bundle exec jekyll serve`, fix whatever breaks. This has never actually run — treat it as an unverified prototype, not finished code.
2. **Once it builds and looks right**, create a GitHub repo (Tomek needs to say public/private — public is required for free GitHub Pages custom domain on a personal account), push the contents of `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\site\` as the repo root, enable GitHub Pages in repo Settings, add a `CNAME` file for `bitcoinfilmfest.com`, point DNS at GitHub's Pages IPs.
3. **Migrate the rest of the content.** Only 3 pages are done (homepage, About, one newsletter) out of ~55+15 newsletters. Source priority order is in `PLAN.md` under "Content migration sources."
4. **Fix image paths.** Migrated content still points at the old WordPress CDN (`bitcoinfilmfest.com/wp-content/uploads/...`). Real image files are in the mirror — see Gotchas below.
5. **Design iteration with Tomek.** The 3/5/10 cinema-frame numbers are a first pass, not final — Tomek said this needs a few rounds of back-and-forth once there's something to look at.

## Key documents and code — read in this order

All paths below are relative to `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\`.

1. **`website\rebuild-jekyll\PLAN.md`** — the full plan: why Jekyll, why GitHub Pages, repo structure, migration steps in order, what's explicitly out of scope (`/tickets/`, Matomo analytics).
2. **`website\rebuild-jekyll\site\README.md`** — inside the scaffold itself: local build instructions, file-by-file explanation of what each part does, known gaps.
3. **`website\rebuild-jekyll\site\`** — the actual scaffold. Start here:
   - `_config.yml` — nav, footer links, social links, site title/tagline. Edit this, not individual pages, to change nav site-wide.
   - `_layouts\default.html` — the page shell: head meta, nav, cinema frame markup, footer, seats image, script tags.
   - `assets\css\cinema-frame.css` — the whole design system in one file. This is the important one for the cinema-frame work.
   - `assets\js\main.js` — scroll-reveal animation (`data-reveal` attribute triggers it).
   - `assets\js\subscribe.js` — the email/npub subscribe form. **Placeholder only** — just does mailto: for emails, shows a static message for npub. Real Nostr DM signing or a Mailchimp/database backend is future work, not this pass.
   - `index.md`, `about.md` — the 2 migrated standalone pages.
   - `_newsletters\2024-06-19-summer-2024.md` — the 1 migrated newsletter, proves the Jekyll collection pattern works.
4. **`website\static-site\`** — the OLD plan's output (PHP includes, ~55 pages already cleaned into HTML bodies with real SEO meta). This is the richest content source for migrating the rest — read each `<slug>\index.php`, strip the PHP, keep the body + `$page_title`/`$page_description`/`$page_image` values.
5. **`BFF26-guest-page\index.html`** — the live, working `/26/` page (this one is a sibling of `website\`, not inside it — full path `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\BFF26-guest-page\index.html`). Its inline `<style>` block (lines ~36–900+) is where the cinema-frame CSS in `cinema-frame.css` was adapted from. If the frame needs adjusting, cross-check against this file — it's the proof that the pattern works in production.
6. **`website\wayback-recovered-2026-08-28\README.md`** — 6 pages recovered from archive.org that aren't in the main content archive. Fold these in during full migration.
7. **`website\bff-content-archive-2026-07-16.zip`** (`content\*.md` inside it) — the original scrape. Fallback source if `static-site\` seems incomplete for a given page.
8. **`website\bff-site-mirror-2026-07-16-parts\`** — full offline HTML+image mirror, split into 13 parts. This has the actual image files needed to fix the WordPress CDN paths. See its `HOW-TO-REASSEMBLE.txt`.

## Decisions and why

- **Jekyll over 11ty**: GitHub Pages builds Jekyll natively, no CI config needed. Tomek wants collaborators; fewer moving parts wins. Revisit if a collaborator strongly prefers a JS-based stack.
- **PHP dropped entirely**: GitHub Pages can't run PHP. The old `static-site/` PHP-include plan is now a content source only, not the build target.
- **Cinema-frame is site-wide, not just `/26/`**: Tomek's explicit instruction, even though archive.org confirms the original bitcoinfilmfest.com homepage never had this treatment — it was `/26/`-only. This is a deliberate new direction, not a restoration of old design.
- **`/tickets/` and Mailchimp/database subscribe backend are out of scope**: Tomek confirmed both — tickets move to an outside system, subscribe stays Nostr-DM-flavored for now with real backend deferred.

## Gotchas

- **No root/sudo in the cloud sandbox** — can't `apt install ruby-dev`, can't test the build here. Has to happen on a machine with normal permissions.
- **OneDrive stale-read risk**: per the folder's own `CLAUDE.md`, files edited in a cloud sandbox session can read back truncated. If Hermes edits large files here, verify integrity (check for a clean EOF) before trusting them, or better, do heavy edits from Tomek's own machine.
- **Images not yet migrated** — every image URL in the 3 migrated pages still points at the live WordPress CDN. Works today because that CDN is still up, but it's not what a from-scratch GitHub Pages deploy should depend on long-term.
- **`bff-site-backup-2026-07-13/` is NOT the real BFF site** — it's a different hosting account (Smarthost `kolotoms`), confirmed and flagged in `website/README-HANDOFF.md`. Don't pull images from there.

## Pick up here

Paste this to start:

> Read `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\HANDOFF.md`, then `PLAN.md` in that same folder, then `site\README.md`. Get the Jekyll scaffold at `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll\site\` building locally — open a terminal in that folder and run `bundle install && bundle exec jekyll serve` — and fix whatever breaks; it's never been build-tested. Once it builds and the cinema-frame layout looks reasonable, report back before migrating more content or touching GitHub.
