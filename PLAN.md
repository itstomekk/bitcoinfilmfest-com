# bitcoinfilmfest.com — Jekyll + GitHub Pages rebuild plan

Decided 2026-08-28. Supersedes the PHP-include plan in `static-site/` — kept as reference for content/design, not as the source of truth going forward.

## Why this replaces the PHP plan

`static-site/` (built 2026-07-16 to 2026-08-05) already solved "shared header/nav/footer, one file per page" using PHP includes. That works for FTP hosting but PHP doesn't execute on GitHub Pages — Pages only serves files as-is. A static site generator (SSG) does the same templating job but at *build time*, producing plain HTML files that run anywhere, including GitHub Pages. Jekyll is GitHub Pages' native SSG: push to a repo, Pages builds and deploys automatically, no separate CI config needed. Content stays in Markdown, matching the format the content archive is already in.

**Design is unaffected.** Jekyll only assembles HTML from templates + Markdown. All CSS (the `/26/` design system: Syne Mono + Courier Prime, `--paper`/`--blue`/`--gold` palette, black outer frame, fixed nav) and all JS (IntersectionObserver scroll reveals, `prefers-reduced-motion` handling) ports over unchanged as static asset files. Jekyll never touches them.

## Hosting decision

**GitHub Pages**, custom domain `bitcoinfilmfest.com` via CNAME DNS record pointed at GitHub's Pages IPs, plus a `CNAME` file in the repo root. Free, no server to maintain, auto-deploys on push to `main` (or a `gh-pages` branch, configurable).

`/tickets/` is explicitly out of scope — Tomek is moving to an outside ticket system, so nothing PHP/dynamic needs to survive the migration.

## Target repo structure

```
bitcoinfilmfest/                    (GitHub repo root)
├── _config.yml                      # site meta, nav, footer, social — replaces inc/config.php
├── _layouts/
│   ├── default.html                 # <head>, nav, frame, footer — replaces header.php/footer.php
│   └── post.html                    # newsletter/blog post layout (extends default)
├── _includes/
│   ├── nav.html
│   ├── footer.html
│   └── head-meta.html               # title/description/og/twitter tags, per-page via front matter
├── _posts/                          # newsletters + blog posts as dated Markdown (Jekyll's native blog support)
│   └── 2024-06-01-june-2024-newsletter.md
├── _pages/ (or root-level dirs)     # standalone pages: about/, join/, credits/, bff25/, bff26/, bff27/, press-and-media/, etc.
│   └── about.md
├── assets/
│   ├── css/main.css                 # ported from /26/ inline CSS
│   ├── js/main.js                   # ported scroll/reveal/nav JS
│   └── images/                      # from wp-content/uploads or /media, reorganized
├── index.md                         # homepage
├── CNAME                            # bitcoinfilmfest.com
├── 404.html
└── README.md                        # contributor instructions
```

## Content migration sources (in priority order)

1. `static-site/*/index.php` — already-cleaned HTML body content for ~55 pages, real per-page SEO meta (title/description/og-image). Strip the PHP scaffolding, keep the body + front-matter-ify the meta fields.
2. `bff-content-archive-2026-07-16.zip` (`content/*.md`) — original scrape, used to build static-site/ in the first place. Fallback if a static-site/ page seems incomplete.
3. `website/wayback-recovered-2026-08-28/` — the 6 pages recovered from archive.org (BFF'26 laurels/wintrezor pages, Dec 2023 + Jan 2024 newsletters, old homepage variant, author archive).
4. Images: `bff-site-mirror-2026-07-16-parts/site/bitcoinfilmfest.com/wp-content/uploads/` (818 files, full mirror) — reassemble the 13-part tar.gz first.
5. Design system: `BFF26-guest-page/index.html` — extract the inline `<style>` and `<script>` blocks as the base for `assets/css/main.css` / `assets/js/main.js`.

## Migration steps

1. **Scaffold** — `jekyll new` equivalent: minimal `_config.yml`, empty `_layouts/default.html`, `Gemfile` (github-pages gem pins Jekyll to the exact version GitHub's servers run, avoiding version-mismatch surprises).
2. **Port design system** — pull CSS/JS out of `/26/index.html` into `assets/`, build `_layouts/default.html` (head meta, nav, frame divs, footer, script includes) from `inc/header.php` + `inc/footer.php` as the template reference.
3. **Migrate config** — `inc/config.php`'s NAV/FOOTER_LINKS/SOCIAL/SITE_NAME constants become `_config.yml` custom keys, read in templates via `{{ site.nav }}` etc.
4. **Convert pages** — script (Python, one-time, like `build_pages.py` but Jekyll-flavored) walks `static-site/*/index.php`, extracts body HTML + the `$page_title`/`$page_description`/`$page_image` values, writes each as `<slug>.md` or `<slug>/index.md` with YAML front matter (`title`, `description`, `image`, `layout`).
5. **Newsletters as Jekyll posts** — the ~15 monthly newsletter pages fit Jekyll's native `_posts/YYYY-MM-DD-title.md` blog convention, which auto-generates a chronological archive/index for free.
6. **Merge wayback finds** — add the 6 recovered pages as new content following the same front-matter pattern (flagging the homepage variant as historical reference, not live content, per its README).
7. **Local build + preview** — `bundle exec jekyll serve`, check every page renders, nav is correct, images resolve, scroll effects still work.
8. **GitHub Pages deploy** — create repo, push, enable Pages (Settings → Pages → source: `main` branch or a `gh-pages` workflow), add `CNAME` file, point DNS.
9. **Collaboration setup** — README with local-build instructions, `.gitignore` for `_site/` and `.jekyll-cache/`, branch protection on `main` if Tomek wants review gates, issue/PR templates optional.

## Explicitly out of scope for this rebuild

- `/tickets/` — moving to an outside ticket system, not migrated.
- Matomo `/analytics/` — untouched, stays wherever it currently runs (separate from the GitHub-hosted static site).
- WooCommerce/shop — already dead per `build_pages.py`'s own drop list.

## Open questions for Tomek before build starts

- Repo name/visibility (public repo needed for free GitHub Pages custom domain on a personal account, unless using GitHub Pro/org for private+Pages).
- Whether newsletters should get their own auto-generated archive page (Jekyll gives this for free via `_posts/`) or stay as flat pages like today.
- Final design pass — memory notes "similar to current design, not identical" was the standing instruction; confirm if that still holds or if the /26/ system should be ported as-is.
