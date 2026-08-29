# Build Log - Bitcoin FilmFest Jekyll Rebuild

This is a short operational record for builders. It records verified facts and active blockers. For implementation details, use `BUILDER-GUIDE.md` and `site/README.md`.

## 2026-08-29 - GitHub repository and Pages preparation

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

### Active blocker

GitHub returned HTTP 422 while enabling Pages:

```text
Your current plan does not support GitHub Pages for this repository.
```

The repository must stay private unless the owner explicitly requests a visibility change. To publish through GitHub Pages while private, upgrade to a plan that supports private Pages, then enable Pages using the existing workflow. Alternative paths are making the repository public with explicit approval or deploying the same static output to another host.

### Deliberately not done

- No `CNAME` file.
- No DNS changes.
- No custom domain connection.
- No collaborator invite (requires the collaborator's GitHub username).

## 2026-08-28 - Site shell, content, and interaction baseline

### Verified

- Jekyll build succeeds using `C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace`.
- Shared cinema shell is in place: black room frame, bezel, perforation pattern, fixed cinema seats, logo-home link, shared footer, black ending.
- Main navigation is data-driven and currently contains Storyboard, Festivals (BFF'24-27), Reel, Credits, and Contribute. Site map remains footer-only.
- Soft same-origin navigation preserves the shell, updates active navigation/current label, and falls back to standard navigation when unavailable.
- Desktop and mobile checks verified no horizontal overflow; current-page indicator, dim-to-bright nav behavior, bottom-right rabbit placement, and menu structure were checked.
- Credits source was migrated to structured data and rendered as a respectful end-credits roll. The animation stops after user input and respects reduced-motion settings.

### Known work still open

- Roughly 40+ historical routes/content pieces are catalogued but not migrated.
- The subscription UI is a safe mailto/Nostr fallback, not a backend list service.
- Credits auto-scroll needs a final visual check in a normal browser where reduced motion is not active.
- The rabbit slightly overlaps one BFF'26 showtime label; minor visual polish only.
- Final custom-domain configuration will require a separate small commit and DNS changes when the owner is ready.
