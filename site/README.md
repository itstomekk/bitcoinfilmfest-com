# bitcoinfilmfest.com — Jekyll source

Static site, built with Jekyll, deployed via GitHub Pages. See `../PLAN.md` (one level up) for the full rebuild plan and rationale.

## Local setup

Requires Ruby with dev headers (`ruby-dev` / `ruby-devel` — needed to build native gem extensions like `json`). On Windows 11, the tested setup is RubyInstaller 3.3 with MSYS2:

```bash
winget install --id RubyInstallerTeam.RubyWithDevKit.3.3 --exact
```

Open a new terminal after installation so Ruby is on `PATH`, then run:

```bash
gem install bundler
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000`.

The `github-pages` gem in the `Gemfile` pins Jekyll and all plugins to the exact versions GitHub's own servers run, so anything that builds cleanly here will also build cleanly when pushed.

The build was verified on Windows 11 with Ruby 3.3.12, Bundler 2.5.22, `github-pages` 232, and Jekyll 3.10.0 on 2026-08-28. The committed lockfile includes Windows and x86-64 Linux platforms for local and GitHub Pages builds.

## Structure

- `_config.yml` — site title, nav, footer links, social links, Nostr npub. Edit this to change the nav site-wide.
- `_layouts/default.html` — the shell every page uses: nav, cinema frame, footer, seats image, scripts.
- `_layouts/newsletter.html` — extends `default`, adds a dated article header. Used by the `_newsletters` collection.
- `_includes/` — nav, footer, and `<head>` meta tags, each pulled into `default.html`.
- `assets/css/cinema-frame.css` — the whole design system: palette, type scale, and the fixed black cinema-room frame (3% top / 5% sides / 10% bottom margins) with the seats image glued to the bottom edge. Adapted from the working pattern already live on `/26/`.
- `assets/js/main.js` — scroll-reveal (`data-reveal` attribute + IntersectionObserver), respects `prefers-reduced-motion`.
- `assets/js/subscribe.js` — the `your e-mail or npub` subscribe form. **Placeholder implementation**: currently just opens a mailto: for emails and shows a static message for npubs. Real NIP-04 DM sending (or a Mailchimp/database backend) is intentionally deferred — see `../PLAN.md`.
- `_newsletters/` — one Markdown file per newsletter issue, e.g. `2024-06-19-summer-2024.md`. Jekyll collection, auto-dated, ready for an auto-generated archive index later.
- `index.md`, `about.md` — standalone pages. One `.md` file per page, front matter sets `layout`, `title`, `description`.

## What's migrated so far (proof-of-concept, not the full site)

- Homepage (`index.md`)
- About (`about.md`)
- One newsletter (`_newsletters/2024-06-19-summer-2024.md`)

This is intentionally a small slice — enough to verify the cinema-frame layout, nav, footer, and newsletter collection all work together before mass-migrating the remaining ~50+ pages from `static-site/` and the content archive.

## Known gaps / next steps

- **Images still point at the old WordPress CDN** (`bitcoinfilmfest.com/wp-content/uploads/...`) in migrated content. Needs a pass to pull the real files from `../bff-site-mirror-2026-07-16-parts/` and rewrite paths to `/assets/images/...`.
- **Cinema frame proportions are a first pass** — Tomek wants to iterate on the design once more pages are in place to look at.
- **Subscribe form has no real backend** — see above.
- **Build verified locally** — `bundle install`, `bundle exec jekyll build`, and the served homepage/About/newsletter/404 pages have been exercised. Continue to run the build before every deploy.
- **Remaining ~50 pages** from `static-site/*/index.php` and the content archive not yet converted.
