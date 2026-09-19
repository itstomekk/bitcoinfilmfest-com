# Bitcoin FilmFest — changelog

Short, human-readable record of public website changes. One dated entry is required for every source change that affects the website.

## 2026-09-18 — Press kit and BFF’26 press room restored

- Added `/presskit/`, preserving the verified local branding book with BFF logos, rabbit mark, posters, laurels, SVG/PDF vector assets, colour palette, and Syne Mono/Courier Prime specimens.
- Linked the press kit from Storyboard, the BFF’26 Press Kit section, and the restored press-room pages.
- Reconstructed `/26/press/` from the local BFF26 guest-page source: 34 static EN/PL hub, info-base and article pages, with local project-relative asset links and the current presskit destination.
- Replaced the old BFF’26 press/gallery/laurels links with local routes or the existing BFF’25 photo archive; no private source notes or FTP tooling were copied.
- Updated the route map and sitemap inventory to 101 generated / 89 public-indexable routes.

## 2026-09-18 — Custom domain cutover to bitcoinfilmfest.com

- Set `bitcoinfilmfest.com` as the GitHub Pages custom domain and added the repository `CNAME` file.
- Switched DNS: apex `A`/`AAAA` records now point at GitHub Pages; the previous website IP moved to `mail.bitcoinfilmfest.com`, and `MX`/`ftp` were repointed accordingly so mail and FTP keep working. Full pre-change zone backed up locally before any edit.
- Switched the deploy workflow to build with only `_config.yml`, so canonical/OG/sitemap URLs now render as `https://bitcoinfilmfest.com` instead of the temporary Pages preview.
- Next: wait for DNS propagation and GitHub's certificate, then enable Enforce HTTPS and verify the live domain per `DOMAIN-SEO-CUTOVER.md`.

## 2026-09-16 — Reel archive migration and public-media boundary

- Added exactly 10 public-safe legacy interviews, guest posts, and an event report to the unified `/reel/` archive, with the original routes retained as noindex compatibility redirects.
- Removed unreconciled WordPress and `/media/` image hotlinks from every Reel entry instead of publishing unverified image assets; the text remains available while local rights-cleared derivatives are absent.
- Kept `/25/` as the canonical BFF’25 route and changed the migrated Luke Willms links to point there rather than to the redirect-only `/bff25/` route.

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