# Bitcoin FilmFest — changelog

Short, human-readable record of public website changes. One dated entry is required for every source change that affects the website.

## 2026-09-16 — Next ten public cinema profiles

- Added ten new public Bitcoin Cinema film profiles: Aimy in a Cage, New Money, What the F*ck Is My Password?!, LifeHack, Bitcoin Heist, Immutable Democracy, Unbankable, Death Athletic: A Dissident Architecture, The 1Up Fever, and God Bless Bitcoin.
- Profiles use public sources only and add no private data or media.
## 2026-09-16 — Archive visual and photo-loading pass

- Rebalanced archive/current edition composition with a stronger BFF’27 hero mark treatment and a deliberately asymmetric BFF’24 selection lead.
- Kept the complete BFF’23 (554 frames) and BFF’25 (152 frames) public albums, but moved them behind native disclosure controls so the first view stays focused while every image remains lazy-loaded.
- Fixed BFF’27 archive-accent color resolution and preserved the shared cinema shell, fixed seats, responsive grids, focus styles, and reduced-motion behavior.
- Verified the Jekyll build, edition validators, local asset loading, keyboard focus, mobile widths, and album toggles.

## 2026-09-15 — Public documentation and repository cleanup

- Reworked the root README into a branded guide for collaborators and future builders.
- Added the public-repository safety review and documented what must stay outside Git.
- Documented the cinema design system, the CSS/JavaScript split, and the FormSubmit subscription adapter.
- Added the repository description, homepage, and discovery topics on GitHub.
- Added a pull-request check that requires a dated changelog entry when website source changes.

## 2026-09-15 — FormSubmit subscription

- Connected the shared footer form on every route to FormSubmit AJAX.
- Added the `/thanks/` confirmation page, honeypot field, and cache-busting for the subscription script.
- Signups are forwarded to `mails@bitcoinfilmfest.com`; this is notification delivery, not a subscriber database.

## 2026-08-29 — GitHub Pages launch

- Published the Jekyll site through GitHub Actions and GitHub Pages.
- Established the shared cinema shell, navigation, footer, design tokens, and public builder documentation.

## How to add an entry

Add the newest date at the top, using plain language:

```markdown
## YYYY-MM-DD — Short change title

- What visitors or collaborators can now do.
- What route, component, or workflow changed.
- What was verified, if the change involved a build or deployment.
```

For detailed test output, blockers, and implementation history, use `BUILD-LOG.md` and the Git commit or pull request.