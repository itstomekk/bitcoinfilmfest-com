# Build Log - Bitcoin FilmFest Jekyll Rebuild

This is a short operational record for builders. It records verified facts and active blockers. For implementation details, use `BUILDER-GUIDE.md` and `site/README.md`.

## 2026-08-29 - Builder clarity and cinema polish pass

### Verified

- Added a welcoming root `README.md` that explains the website source, public/private boundaries, content flow, safe editing paths, and deployment pipeline in non-developer language.
- Confirmed `site/` remains the Jekyll website source directory by design. It is conventional and avoids needless deployment-path churn; documentation calls it the website source in plain language.
- Added the official Instagram link `https://instagram.com/bitcoin_filmfest` through the central social config and shared footer.
- Desktop menu groups now open on real hover, retain native keyboard/touch disclosure behavior, and close every other open group. Mobile permits only one expanded subgroup at a time.
- Homepage rabbit was pushed deliberately farther into the bottom-right screen edge. Showtime controls were narrowed and shortened.
- Fixed cinema seats now use a dedicated foreground z-layer and a reduced-motion-safe scroll-driven zoom where the browser supports scroll timelines.
- Credits now uses a dedicated raised-black auditorium screen, with historic Credits data rendered as centered one-name-per-line end credits rather than a paper page or multi-column list.
- Local normal build and GitHub Pages-equivalent build both passed. Real browser checks passed 8/8: desktop hover, mutual submenu closure, mobile single disclosure, Instagram, foreground seats, rabbit placement, compact showtimes, and dark Credits layout.

### Known follow-up

- The source repository is public. Keep private film/licensing/contact data outside it. A separate private source plus GitHub Actions secrets can generate an approved public movie snapshot later.
- Credits auto-roll remains intentionally disabled when a visitor prefers reduced motion; it should be visually revisited whenever credit typography changes.

## 2026-08-29 - GitHub Pages deployment is live

### Verified

- Repository is public: https://github.com/itstomekk/bitcoinfilmfest-com
- GitHub Pages source is **GitHub Actions**, using `.github/workflows/deploy-pages.yml` because the Jekyll source is in the `site/` subdirectory.
- Deployment run `33260175248` completed successfully: both the Jekyll build and Pages deploy jobs passed.
- Live temporary URL: https://itstomekk.github.io/bitcoinfilmfest-com/
- A remote web fetch verified the deployed homepage title: `Bitcoin FilmFest — the heart of Bitcoin Cinema`.
- The workflow pins Ruby 3.3 and installs gems outside `site/` to prevent Jekyll 3.10 from scanning Bundler templates as site posts on GitHub runners.

### Deliberately not done

- No `CNAME` file.
- No DNS changes.
- No custom domain connection.
- No collaborator invite (requires the collaborator's GitHub username).

## 2026-08-29 - Initial private-repository Pages attempt (resolved)

### Verified

- Created and pushed private repository: https://github.com/itstomekk/bitcoinfilmfest-com
- Default branch: `main`.
- Initial source commit contains the Jekyll site, modular shared shell, current content pages, local assets, design system, and handoff history.
- Added `.github/workflows/deploy-pages.yml`, which builds the real Jekyll root in `site/` and deploys a GitHub Pages artifact.
- Added `site/_config.github-pages.yml` so a temporary project-site deployment uses `/bitcoinfilmfest-com` correctly without changing the future custom-domain configuration.
- Verified the Pages-equivalent local build:

  ```bash
  C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace --config _config.yml,_config.github-pages.yml
  ```

  It exits successfully and emits the expected `/bitcoinfilmfest-com/assets/` paths.

### Historical note

Before the repository was made public, GitHub returned HTTP 422 because private Pages was unavailable on the account plan. The owner then made the repository public, which resolved this specific blocker. The successful live deployment is recorded above.

### Deliberately not done at that point

- No `CNAME` file.
- No DNS changes.
- No custom domain connection.
- No collaborator invite (requires the collaborator's GitHub username).

## 2026-08-28 - Site shell, content, and interaction baseline

### Verified

- Jekyll build succeeds using `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`.
- Shared cinema shell is in place: dark room frame, bezel shadow, fixed cinema seats, logo-home link, and shared charcoal footer canvas.
- Main navigation is data-driven and currently contains Storyboard, Festivals (BFF'24-27), Reel, Credits, and Contribute. Public sitemap page and footer menu links were removed.
- Soft same-origin navigation preserves the shell, updates active navigation/current label, and falls back to standard navigation when unavailable.
- Desktop and mobile checks verified no horizontal overflow; current-page indicator, dim-to-bright nav behavior, bottom-right rabbit placement, and menu structure were checked.
- Credits source was migrated to structured data and rendered as a respectful end-credits roll. The animation stops after user input and respects reduced-motion settings.

### Known work still open

- Roughly 40+ historical routes/content pieces are catalogued but not migrated.
- The subscription UI is a safe mailto/Nostr fallback, not a backend list service.
- Credits auto-scroll needs a final visual check in a normal browser where reduced motion is not active.
- The rabbit slightly overlaps one BFF'26 showtime label; minor visual polish only.
- Final custom-domain configuration will require a separate small commit and DNS changes when the owner is ready.
