# Bitcoin FilmFest website

Welcome. This repository contains the source code, content, visual design system, and deployment instructions for the Bitcoin FilmFest website.

**Live temporary website**

https://itstomekk.github.io/bitcoinfilmfest-com/

**Source repository**

https://github.com/itstomekk/bitcoinfilmfest-com

The public URL will later move to `bitcoinfilmfest.com`. Until then, do not add a `CNAME` file or edit DNS records. The owner-approved release procedure is documented in `DOMAIN-SEO-CUTOVER.md`.

## 🎬 What this project is

This is a **Jekyll static website**. Jekyll turns Markdown content, data files, templates, CSS, images, and JavaScript into ordinary HTML files. GitHub Actions performs that build whenever `main` changes, then GitHub Pages publishes the result.

You do not need to be a developer to make routine changes. Most content work happens in Markdown (`.md`) and YAML (`.yml`) files.

## 🧭 Start here

| If you want to... | Read or edit... |
| --- | --- |
| Understand the project in plain language | This README |
| Add or edit a page | `site/README.md` |
| Make a page match the visual system | `site/design.md` |
| Change primary navigation links | `site/_data/navigation.yml` |
| Understand technical ownership and non-regression rules | `BUILDER-GUIDE.md` |
| See verified milestones and current open work | `BUILD-LOG.md` |
| Follow the current future-builder handoff | `HANDOFF-CURRENT.md` |
| See the old-site migration roadmap | `REBUILD-PHASES.md` |

## 🗂️ Folder map

```text
.
├── site/                         The actual website source
│   ├── index.md                  Homepage content
│   ├── *.md                      Standalone pages: editions, Storyboard, Credits, Reel...
│   ├── _newsletters/             One Markdown file per newsletter
│   ├── _data/                    Editable structured data: navigation, credits, builder-only route inventory
│   ├── _includes/                Shared fragments: navigation, footer, HTML head
│   ├── _layouts/                 Shared page structures
│   ├── assets/                   Browser files: images, CSS, JavaScript
│   ├── tokens.css                Shared visual values: colours, type, spacing, layering
│   ├── design.md                 Written visual system for custom page work
│   └── README.md                 Practical editing and local-build guide
├── .github/workflows/            GitHub Actions deployment instructions
├── BUILDER-GUIDE.md              Builder and agent handoff guide
├── BUILD-LOG.md                  Verified history and open work
├── HANDOFF-CURRENT.md            Current operational handoff
├── REBUILD-PHASES.md             Phased old-site migration roadmap
└── HANDOFF*.md                   Historical session records, not the current manual
```

`site/` is a conventional, short name for the Jekyll source directory. It is called the **website source** throughout the documentation. We are intentionally keeping this folder name because changing it would add needless deployment and documentation churn without changing the public website.

## How information flows

```text
Markdown pages + YAML data + local images
                ↓
Jekyll templates and shared cinema frame
                ↓
GitHub Actions builds static HTML into site/_site
                ↓
GitHub Pages publishes the generated website
```

### Where content comes from

| Information | Current source | Where to change it now |
| --- | --- | --- |
| Homepage, editions, Storyboard, Reel, Credits, Contribute | Markdown files in `site/` | Edit the matching `.md` file |
| Navigation and footer links | `site/_data/navigation.yml` | Edit that one file |
| Credits roster | Recovered from the historic PHP Credits page | `site/_data/credits.json` |
| Newsletter content | Markdown in `site/_newsletters/` | Add or edit newsletter files |
| Brand logo, rabbit, cinema imagery | Local production assets | `site/assets/images/` |
| Site title, social links, collections | `site/_config.yml` | Edit carefully, then restart local Jekyll |
| Visual language | `site/design.md` and `site/tokens.css` | Read first; change tokens before component CSS |
| Interactive behavior | JavaScript files in `site/assets/js/` | See comments at the top of each file |

## 🔒 Important: public versus private

This repository is public. **Anything committed here is readable by anyone**, even if it is not published as a web page.

- A folder outside `site/` is not automatically published to GitHub Pages, but it is still visible in the public repository.
- `.gitignore` prevents a file from being committed. It does not hide a file that was already committed.
- Never commit passwords, API keys, mailing-list exports, private contact lists, raw movie-license documents, or a private movie database.

### Can this website use private movie data?

Yes, with a deliberate data boundary:

1. Keep the original movie database in a **separate private repository** or a real database service.
2. Store access credentials only as **GitHub Actions secrets**, never in this repository.
3. During the build, a script can fetch approved public fields, such as title, year, director, image, screening status, and synopsis.
4. Generate a small public YAML/JSON snapshot inside the build output.
5. Remember: any information sent to the visitor’s browser becomes public. A static website cannot keep browser-delivered data secret.

This is a good next phase when the movie catalogue is ready. It should be designed before adding credentials or database code.

## Safe editing for non-developers

- **Menu labels and links:** `site/_data/navigation.yml`
- **A normal page:** create or edit a file such as `site/26.md`
- **Newsletter:** create or edit `site/_newsletters/YYYY-MM-DD-title.md`
- **Credits names:** edit `site/_data/credits.json`
- **Social links:** `site/_config.yml`

Do not copy navigation, footer, cinema seats, or frame markup into a new page. They arrive automatically through the shared layout.

## 💾 Offline copy, Git workflow, and collaboration

Yes, there is an offline maintained copy. The local Git clone is:

`C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll`

It holds the full source and Git history. GitHub is the shared remote backup and the publishing trigger, not the only copy.

### Default process for every collaborator

1. Start from fresh shared work:
   ```bash
   git switch main
   git pull --ff-only origin main
   ```
2. Create a branch for one clear task:
   ```bash
   git switch -c content/add-bff26-press
   ```
3. Make the smallest focused edit. Coordinate before two people edit the same page, data file, or shared component.
4. Build locally from `site/`:
   ```bash
   C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace
   ```
5. Review the changed page at desktop and mobile sizes. Then inspect the exact change:
   ```bash
   git diff --check
   git status --short
   ```
6. Commit with an honest, focused message, push the branch, and open a pull request. Merge only after the change is reviewed.
7. GitHub Actions deploys only after a change reaches `main`. Confirm the Actions run is green and read the public URL back.

For a one-line urgent correction, a trusted maintainer may push to `main` after a local build. Branches and pull requests remain the normal safer process.

### Backup and milestones

- A pushed commit can be restored from Git history. Do not delete history to “clean up”.
- Before a large phase, create and push an annotated tag such as `phase-2-ready`.
- Store unreleased source files, private databases, contracts, and sensitive material separately. A public repository is not private storage.

## 🚀 Development and deployment

- A change pushed to `main` runs `.github/workflows/deploy-pages.yml`.
- The workflow uses Ruby 3.3, installs Jekyll dependencies, builds the `site/` folder, and deploys the generated output to GitHub Pages.
- The source files remain in `site/`; only the generated site output is published.
- Before changing or approving code, run the documented local build in `site/README.md`.

## Design rules that protect the BFF character

- Real BFF logo and rabbit assets, never recreated as styled text or generic illustrations.
- One shared cinema shell on every page: navigation, soft bezel shadow, fixed seats, and charcoal footer canvas.
- Navigation structure is data-driven, hover/focus accessible, and works on mobile.
- Custom pages must use `site/design.md` and token variables from `site/tokens.css`.
- Motion is progressive enhancement and must respect reduced-motion preferences.

## 🧱 Old-site rebuild roadmap

The public Site map page was intentionally removed: visitors should not see the migration queue. Builders can use `REBUILD-PHASES.md`, `site/SITEMAP-PLAN.md`, and `site/_data/sitemap.json` to plan internally.

The next work sequence is: archive triage and redirect decisions, completed festival edition hubs, a real Reel/publication archive, and then a safe build-time private movie-catalogue pipeline. Schema, a reviewed public XML sitemap, and `AGENTS.md` are later discovery/onboarding work, once enough real routes and data exist.

## ✨ Questions and improvements

Jekyll currently includes SEO metadata, feed support, and GitHub Pages compatibility. Schema and XML sitemap work are intentionally deferred. See `site/README.md` and `BUILD-LOG.md` before adding a plugin. Because deployment uses GitHub Actions, we can add carefully chosen build-time plugins later, but every plugin must be documented, pinned, and verified in the deployment workflow.

## Recent changes

This is the simplified, day-grouped change summary. `BUILD-LOG.md` remains the detailed verified record; Git history is the complete source of every file-level change.

### 2026-08-30

- Added SEO assets, structured metadata, `robots.txt`, XML sitemap, and the web manifest.
- Added safe pull-request checks, a downloadable PR build artifact, and collaboration guidance.
- Refined the cinema shell: optimized supplied favicon, SVG social marks, film-reel controls, screen texture, seat overlay/zoom, hero, footer, and navigation.
- Current temporary production URL remains the GitHub Pages project site. No custom-domain DNS/CNAME change was made.

### 2026-08-29

- Published the modular Jekyll rebuild through GitHub Actions Pages.
- Added shared navigation, Credits roll, footer, public builder guides, and the custom-domain cutover checklist.

## 🧾 Historical records

`HANDOFF.md`, `HANDOFF-SESSION-2.md`, and `HANDOFF-SESSION-3.md` are preserved snapshots of earlier work. They explain why decisions were made, but they are not the current source of truth. `HANDOFF-CURRENT.md` is the live handoff.

For current work, use:

1. `HANDOFF-CURRENT.md`
2. `BUILDER-GUIDE.md`
3. `site/README.md`
4. `site/design.md`
5. `REBUILD-PHASES.md`
6. `BUILD-LOG.md`
