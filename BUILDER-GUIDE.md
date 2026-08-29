# Bitcoin FilmFest - Builder Guide

This is the current entry point for anyone extending the Bitcoin FilmFest site. Start here, then read `site/README.md` and `site/design.md` before changing code or content.

## Current status

- Source repository: https://github.com/itstomekk/bitcoinfilmfest-com (private, `main`)
- Site engine: Jekyll 3.10.0 via the `github-pages` gem
- Site source directory: `site/`
- Local production build: verified on Windows 11 with RubyInstaller Ruby 3.3.12 and Bundler 2.5.22
- Pages workflow: `.github/workflows/deploy-pages.yml`
- GitHub Pages is **not live yet** because the current GitHub plan does not allow Pages for this private repository. The workflow build configuration is committed and ready. See `BUILD-LOG.md`.
- Custom domain: deliberately deferred. Do not add a `CNAME` file or change DNS until the owner asks.

## Read these in order

1. `site/README.md` - practical editing, build, preview, and deployment instructions.
2. `site/design.md` - the locked visual system and page-design rules.
3. `site/_data/navigation.yml` - live menu and footer data.
4. `BUILD-LOG.md` - verified milestones, open work, and external blockers.
5. `PLAN.md` - original migration strategy and source inventory.

## Historical handoffs

These are dated session records. They are retained for evidence and recovery, **not** as the current operating manual:

- `HANDOFF.md` - original scaffold brief from before the build and GitHub repository existed.
- `HANDOFF-SESSION-2.md` - redesign and asset-recovery session snapshot.
- `HANDOFF-SESSION-3.md` - nav, credits-roll, GitHub repository, and Pages-attempt snapshot.

When the documents disagree, this guide, `site/README.md`, the actual source files, and `BUILD-LOG.md` win.

## Ownership map

| Change needed | Edit this first | Do not duplicate |
| --- | --- | --- |
| Add a normal page | `site/<slug>.md` | Do not copy navigation, footer, or cinema-frame markup. |
| Add a newsletter | `site/_newsletters/<yyyy-mm-dd>-<slug>.md` | Do not manually build a separate shell. |
| Change menu or footer links | `site/_data/navigation.yml` | Do not hard-code links in page files. |
| Change shared page frame | `site/_layouts/default.html`, `site/_includes/` | Keep the black tail, cinema seats, logo home link, and skip link. |
| Change palette, typography, spacing, or motion | `site/tokens.css`, then `site/design.md` | Do not add one-off colors or fonts. |
| Change component/layout styling | `site/assets/css/cinema-frame.css` | Use existing token variables. |
| Change soft navigation | `site/assets/js/main.js` | Preserve ordinary-link fallback and reduced-motion behavior. |
| Change credit auto-scroll | `site/assets/js/credits-roll.js` | Preserve permanent user-input stop behavior. |
| Replace subscribe behavior | `site/assets/js/subscribe.js` | Do not put API keys in the repository. |

## Rules that must not regress

- Every route uses the shared shell: logo-home link, nav, cinema bezel, top perforation pattern, fixed seats, footer, and true black page ending.
- `site/_data/navigation.yml` is the only primary/footer navigation source.
- Use real BFF assets. Do not recreate the logo as text or replace the rabbit with generic illustrations.
- Use `site/design.md` and `site/tokens.css` for new custom page designs.
- Same-origin transitions are enhancement only. Normal links must work if JavaScript fails.
- Respect keyboard access, focus styles, and `prefers-reduced-motion`.
- Build before committing. Do not commit `site/_site/`, caches, secrets, or local dependencies.

## Fast handoff prompt

> Read `BUILDER-GUIDE.md`, `site/README.md`, `site/design.md`, and `BUILD-LOG.md`. Confirm the current git status, run the documented Jekyll build, then make only the requested change. Keep the shared cinema shell and data-driven navigation intact.
