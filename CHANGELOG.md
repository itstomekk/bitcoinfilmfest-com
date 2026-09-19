# Bitcoin FilmFest — changelog

Short, human-readable record of public website changes. One dated entry is required for every source change that affects the website.

## 2026-09-18 — Two new Reel posts: 2023 history and BFF25 cinema retrospective

- Published "Our History Begins in 2023" at `/reel/our-history-begins-2023/`, a fact-checked retrospective on BFF23 Warsaw and the BFF Mini Lisboa activation, rewritten from a private source with owner-authorized reuse and no unsupported attendance/programme claims.
- Published "Bitcoin FilmFest 2025: Kino Poza Schematami" (Polish) at `/reel/bff25-kino-poza-schematami/`, a retrospective on the BFF25 cinema programme (generative-cinema block, upcoming-productions block, The PoWies, the pitching contest, and the Revolución Bitcoin / Unbankable / Hotel Bitcoin screenings), reframed in past tense with the canonical `/25/` link and current social URLs.
- Both entries carry `category: articles` with no `archived` flag, so they render under the Reel page's Posts section as the first new writing since the archive migration.

## 2026-09-18 — Reel Chronicle, Posts, and Archive structure

- Reordered `/reel/` into Chronicle, Posts, and Archive sections, with in-page navigation matching the new anchors.
- Split fresh Reel entries from archived entries and added a clean empty state for Posts until new writing is published.
- Combined interviews, articles, and newsletters into one newest-first Archive list with visible category labels; newsletters no longer have a separate section.

## 2026-09-18 — Reel/newsletter migration finalized

- Completed the unified Reel migration: 10 prior interviews/articles and 13 Bitcoin Cinema Digest issues now live in `site/_reel/`, for 23 archived entries and 23 detail routes.
- Removed the separate `_newsletters` collection. Editorial type is carried by the shared `category` taxonomy, and the former Summer 2024 issue is included with the 12 remaining migrated newsletters.
- Verified the Windows Jekyll build, real body content on representative newsletter and interview/article routes, and the Chronicle → Posts → Archive order on `/reel/`.
- Removed a stale WordPress CDN migration note from the About source so the clean generated output contains no old upload-path markers.

## 2026-09-18 — Press kit and BFF'26 press room restored

- Added `/presskit/`, preserving the verified local branding book with BFF logos, rabbit mark, posters, laurels, SVG/PDF vector assets, colour palette, and Syne Mono/Courier Prime specimens.
- Linked the press kit from Storyboard, the BFF'26 Press Kit section, and the restored press-room pages.
- Reconstructed `/26/press/` from the local BFF26 guest-page source: 34 static EN/PL hub, info-base and article pages, with local project-relative asset links and the current presskit destination.
- Replaced the old BFF'26 press/gallery/laurels links with local routes or the existing BFF'25 photo archive; no private source notes or FTP tooling were copied.
- Updated the route map and sitemap inventory to 101 generated / 89 public-indexable routes.

## 2026-09-18 — README rewritten as marketing-first project intro

- Rewrote the root `README.md`: opens with the "heart of the Bitcoin Cinema industry" / unfiat-the-culture mission instead of a plain code description, then keeps the practical content-editing table and technical/build documentation below it.
- No website source, layout, or data changes — documentation only.

## 2026-09-18 — SEO and AI-discovery audit fixes

- Excluded the 11 legacy redirect stub pages (old interview/newsletter URLs, `/bff25/`) from `sitemap.xml` via `sitemap: false`, matching their existing `robots: noindex`. They no longer appear in the public sitemap.
- Added a unique `description` front-matter field to all 30 film pages and 7 company pages (derived from each entry's `synopsis`/`bitcoin_angle`), so search results and social previews no longer show the same site-wide description on every film/company page.
- Added `site/llms.txt`, a plain-language site summary and key-page index for AI agents and LLM crawlers, alongside the existing `robots.txt` and `sitemap.xml`.
- Verified via a local Jekyll build: sitemap entry count dropped as expected, film/company meta descriptions are now unique, `/llms.txt` renders correctly.

## 2026-09-18 — Custom domain cutover to bitcoinfilmfest.com

- Set `bitcoinfilmfest.com` as the GitHub Pages custom domain and added the repository `CNAME` file.
- Switched DNS: apex `A`/`AAAA` records now point at GitHub Pages; the previous website IP moved to `mail.bitcoinfilmfest.com`, and `MX`/`ftp` were repointed accordingly so mail and FTP keep working. Full pre-change zone backed up locally before any edit.
- Switched the deploy workflow to build with only `_config.yml`, so canonical/OG/sitemap URLs now render as `https://bitcoinfilmfest.com` instead of the temporary Pages preview.
- Next: wait for DNS propagation and GitHub's certificate, then enable Enforce HTTPS and verify the live domain per `DOMAIN-SEO-CUTOVER.md`.

## 2026-09-16 — Reel archive migration and public-media boundary

- Added exactly 10 public-safe legacy interviews, guest posts, and an event report to the unified `/reel/` archive, with the original routes retained as noindex compatibility redirects.
- Removed unreconciled WordPress and `/media/` image hotlinks from every Reel entry instead of publishing unverified image assets; the text remains available while local rights-cleared derivatives are absent.
- Kept `/25/` as the canonical BFF'25 route and changed the migrated Luke Willms links to point there rather than to the redirect-only `/bff25/` route.

## 2026-09-16 — Next ten public cinema profiles

- Added ten new public Bitcoin Cinema film profiles: Aimy in a Cage, New Money, What the F*ck Is My Password?!, LifeHack, Bitcoin Heist, Immutable Democracy, Unbankable, Death Athletic: A Dissident Architecture, The 1Up Fever, and God Bless Bitcoin.
- Profiles use public sources only and add no private data or media.

## 2026-09-16 — Archive visual and photo-loading pass

- Rebalanced archive/current edition composition with a stronger BFF'27 hero mark treatment and a deliberately asymmetric BFF'24 selection lead.
- Kept the complete BFF'23 (554 frames) and BFF'25 (152 frames) public albums, but moved them behind native disclosure controls so the first view stays focused while every image remains lazy-loaded.
- Fixed BFF'27 archive-accent color resolution and preserved the shared cinema shell, fixed seats, responsive grids, focus styles, and reduced-motion behavior.
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

\`\`\`markdown
## YYYY-MM-DD — Short change title

- What visitors or collaborators can now do.
- What route, component, or workflow changed.
- What was verified, if the change involved a build or deployment.
\`\`\`

For detailed test output, blockers, and implementation history, use `BUILD-LOG.md` and the Git commit or pull request.
