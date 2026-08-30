# bitcoinfilmfest.com - Jekyll source

The Bitcoin FilmFest website is a static Jekyll site with a shared cinematic shell. Content is Markdown/YAML; the cinema frame, navigation, footer, and visual tokens are reusable site-wide.

**Builder entry point:** read `../BUILDER-GUIDE.md` first. It explains repository status, the historical handoffs, ownership boundaries, and the non-regression rules.

## What is here

- Homepage, Storyboard, Reel, Credits, Contribute, BFF'24, BFF'25, BFF'26, BFF'27, 404, and a migrated newsletter.
- Shared navigation, footer, cinema bezel shadow, fixed seats, logo-home control, and framed screen ending.
- Progressive same-origin navigation with ordinary navigation as fallback.
- A tokenized visual system in `design.md` and `tokens.css`.
- A GitHub Pages Actions workflow at `../.github/workflows/deploy-pages.yml`.

## Local setup - Windows 11 (verified)

Tested with RubyInstaller Ruby 3.3.12, Bundler 2.5.22, `github-pages` 232, and Jekyll 3.10.0.

```bash
# From the repository root
cd site

# Install dependencies if needed
C:/Ruby33-x64/bin/bundle.bat install

# Production build - required before committing
C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace

# Local preview
C:/Ruby33-x64/bin/jekyll.bat serve --host 127.0.0.1 --port 4000 --trace
```

Open http://127.0.0.1:4000/

The non-blocking Faraday `faraday-retry` notice may appear during builds. The verified build still exits successfully.

## Add or edit content

### Add a regular page

Create `site/<slug>.md`:

```md
---
layout: default
title: "Page title"
nav_label: "Menu label"
description: "One useful sentence for search/social previews."
permalink: /your-route/
screen: paper
---

<article class="page-content">
  <h1>Page title</h1>
  <p>Write content here.</p>
</article>
```

Use `screen: blue` for homepage/edition-style content and `screen: paper` for reading pages. The shared navigation, footer, seats, and black ending are automatic - do not copy them into a page.

### Add a newsletter

Create `site/_newsletters/YYYY-MM-DD-your-title.md`. The collection automatically outputs at `/newsletters/your-title/`. See `site/_newsletters/2024-06-19-summer-2024.md` for the working pattern.

### Change menu links

Edit only `_data/navigation.yml`. Reel is a direct route; Festivals is the only current grouped menu. The footer intentionally has no repeated menu links.

### Change credits

Edit `_data/credits.json`. `credits.md` renders this structured data. `credits.yml` is not a current source of truth.

## Code map

| Path | Owner / responsibility |
| --- | --- |
| `_config.yml` | Global metadata, share-image default, social links, collections, plugins, and Jekyll exclusions. |
| `robots.txt`, `site.webmanifest` | Crawler/installability files. `robots.txt` points bots to the generated XML sitemap; the manifest references app icons. |
| `_config.github-pages.yml` | Temporary GitHub project-site URL/baseurl override. Use only for the GitHub Pages workflow. |
| `design.md` | Locked visual language and rules for custom designs. Read before design work. |
| `tokens.css` | Canonical colors, typography, spacing, z-index, frame, and motion tokens. |
| `_data/navigation.yml` | Sole source of truth for primary/footer navigation. |
| `_data/credits.yml`, `_data/credits.json` | Historic credits roster. |
| `_layouts/default.html` | Shared document structure and persistent cinema shell. |
| `_layouts/newsletter.html` | Newsletter/article layout. |
| `_includes/head-meta.html` | SEO, Open Graph, fonts, styles, favicon, View Transitions metadata. |
| `_includes/nav.html` | Data-driven navigation, logo-home link, current-page indicator. |
| `_includes/footer.html` | Shared footer, social links, subscription form. |
| `assets/css/cinema-frame.css` | Screen/frame/component styling. Use token variables, not ad-hoc design values. |
| `assets/js/main.js` | Mobile menu, active states, accessible soft navigation, route announcements. |
| `assets/js/credits-roll.js` | Optional Credits auto-scroll; stops after user input/reduced-motion. |
| `assets/js/subscribe.js` | Current safe fallback subscription behavior - no backend exists yet. |
| `assets/images/` | Local production image assets. |

## GitHub Pages status

The public GitHub repository and temporary GitHub Pages deployment are live:

https://github.com/itstomekk/bitcoinfilmfest-com

https://itstomekk.github.io/bitcoinfilmfest-com/

Pages uses the committed Actions workflow because the Jekyll source is in this `site/` subdirectory. The workflow pins Ruby 3.3 and keeps its temporary dependencies outside the Jekyll source tree.

When the custom domain is ready, update the deployment configuration deliberately and add a `CNAME` file only after the owner confirms DNS is ready.

## Contribution workflow

1. Create a branch from `main`.
2. Make the smallest focused change.
3. Run the production build command above.
4. Check the affected page at desktop and mobile widths.
5. Commit source only - never `site/_site/`, caches, local gems, secrets, or credentials.
6. Open a pull request or push only after review permission.

## Known gaps

- Around 40+ catalogued archive/content routes still need migration.
- Subscription is not connected to a mailing-list/database backend.
- The final custom-domain switch and DNS are intentionally deferred.
- Credits auto-scroll is accessibility-safe but should be visually checked in a normal browser with motion enabled after future UI changes.

## Older documents

`../HANDOFF.md`, `../HANDOFF-SESSION-2.md`, and `../HANDOFF-SESSION-3.md` are historical snapshots. Do not use them as the current plan; follow `../BUILDER-GUIDE.md` and `../BUILD-LOG.md`.
