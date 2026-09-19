<p align="center">
  <img src="site/assets/images/brand/bff-logo-white.png" alt="Bitcoin FilmFest" width="180">
</p>

<h1 align="center">Bitcoin FilmFest 🧡</h1>

<p align="center">
  <strong>The heart of the Bitcoin Cinema industry.</strong>
</p>

<p align="center">
  <a href="https://bitcoinfilmfest.com">bitcoinfilmfest.com</a> ·
  <a href="https://github.com/itstomekk/bitcoinfilmfest-com/actions">Build status</a>
</p>

---

## 🧡 What Bitcoin FilmFest is

Bitcoin FilmFest is the center of the Bitcoin Cinema industry — the festival, the archive, and the publishing home for the films, filmmakers, and stories that are orange-pilling culture through cinema.

We are not a side track at a finance conference. We run our own festival editions, we curate and champion the films that carry Bitcoin's ideas into culture, and we build the public record — the film database, the company and builder directory, the Chronicle, the newsletters — that ties the whole industry together in one place.

**Our mission is simple: unfiat the culture.** Every film we platform, every festival edition, every archive entry is another push to move storytelling, art, and culture away from the fiat mindset and toward a Bitcoin-standard world. This repository is how we build and publish that mission in public.

This is the public source code for **[bitcoinfilmfest.com](https://bitcoinfilmfest.com)** — the Jekyll website, the editorial content, the film and company database, the design system, and the GitHub Actions pipeline that deploys it.

## 🎬 How the site is put together

The site is a static site: no server, no database at runtime — just files that get built once and served fast.

```text
Markdown + YAML content (films, companies, articles, newsletters)
            ↓
Jekyll layouts, includes, CSS, and JavaScript (the cinema design system)
            ↓
GitHub Actions builds the site
            ↓
GitHub Pages publishes bitcoinfilmfest.com
```

Push a change to `main` and, a couple of minutes later, it's live on the real domain. No FTP, no manual upload, no separate hosting panel.

## 🧭 If you just want to edit content

You don't need to know how to code to do most of the everyday editing here. It's Markdown and YAML files — plain text with simple structure.

| I want to... | Edit this |
| --- | --- |
| Add or update a **film** in the database | `site/_films/` — one file per film |
| Add or update a **company / builder / ecosystem entry** | `site/_companies/` — one file per company |
| Write a **Chronicle** entry (news, editorial, story) | `site/_chronicle/` |
| Publish a **newsletter** | `site/_newsletters/` |
| Add or edit a **normal page** (About, Cinema, Festivals…) | the matching `.md` file directly in `site/` |
| Change **menu links** | `site/_data/navigation.yml` |
| Update the **credits roll** | `site/_data/credits.json` |
| Match the **look and feel** of the cinema design | read `site/design.md` first, reuse values from `site/tokens.css` |

Each of those content folders holds small, self-contained files — copy an existing one as a template, change the fields, and you have a new film, company, or story without touching any code.

For the full step-by-step (with examples of every field), see [`site/README.md`](site/README.md).

## ⚙️ Technical overview

| Topic | Where |
| --- | --- |
| Practical editing + local build guide | [`site/README.md`](site/README.md) |
| Visual design system (colors, type, layout rules) | [`site/design.md`](site/design.md) |
| Shared visual tokens (CSS variables) | [`site/tokens.css`](site/tokens.css) |
| Component / layout styling | [`site/assets/css/cinema-frame.css`](site/assets/css/cinema-frame.css) |
| Interactive behavior (nav, forms, motion) | [`site/assets/js/`](site/assets/js/) |
| Shared page shell (header, footer, seats, bezel) | [`site/_layouts/default.html`](site/_layouts/default.html) |
| Migration / roadmap plan | [`REBUILD-PHASES.md`](REBUILD-PHASES.md) |
| Current handoff and ownership rules | [`BUILDER-GUIDE.md`](BUILDER-GUIDE.md) and [`HANDOFF-CURRENT.md`](HANDOFF-CURRENT.md) |
| Verified milestones / history | [`BUILD-LOG.md`](BUILD-LOG.md) |
| Public/private data-safety rules | [`docs/PUBLIC-REPO-SAFETY.md`](docs/PUBLIC-REPO-SAFETY.md) |

### Local development on Windows

Verified local toolchain: RubyInstaller Ruby 3.3.12, Bundler 2.5.22, GitHub Pages 232, Jekyll 3.10.0.

```bash
cd site
C:/Ruby33-x64/bin/bundle.bat install
C:/Ruby33-x64/bin/bundle.bat exec jekyll build --trace
C:/Ruby33-x64/bin/jekyll.bat serve --host 127.0.0.1 --port 4000 --trace
```

Open `http://127.0.0.1:4000/` to preview locally before pushing.

### Contribution workflow

1. Start from an up-to-date `main` branch.
2. Create one focused branch for one change.
3. Edit the smallest responsible source file — a single film, a single page, one data file.
4. Add a short comment only when the reason, boundary, or fallback isn't obvious from the code itself.
5. Build locally and check the affected page at desktop and mobile widths.
6. Run `git diff --check` and the public-repository safety check before committing.
7. Commit with an honest message (`Add BFF26 golden rabbit winners`, `Fix mobile nav overlap`).
8. Open a pull request. A push to `main` triggers the live GitHub Pages deployment automatically.
9. Verify the public URL and the green Actions run before calling anything "done".

### How decisions are logged

- **Code comments** — local implementation choices and safety boundaries.
- **`CHANGELOG.md`** — short, dated public changes; required on every website-source PR.
- **`BUILD-LOG.md`** — detailed verified milestones, tests, deployments, and known gaps.
- **`BUILDER-GUIDE.md`** — ownership and non-regression rules.
- **`HANDOFF-CURRENT.md`** — current operational state, for whoever picks this up next.
- **Git commit messages and pull requests** — the full change history.
- **`docs/`** — durable research notes and public/private data-boundary guidance.

Do not put private conversations, credentials, contact lists, or unverified claims into comments or commit messages — see repository safety below.

## 🔒 Public repository safety

This repository is public. **Anything committed here is readable by anyone**, even if Jekyll never turns it into a web page.

Never commit:

- passwords, API keys, private keys, cookies, or access tokens;
- mailing-list exports or private contact databases;
- film contracts, licensing documents, or private production notes;
- `.env` files, backups, local databases, or private cloud links;
- information that's only "safe" because a page is currently unlinked.

[`scripts/check-public-repo.py`](scripts/check-public-repo.py) runs in every pull request and scans tracked files for forbidden paths and common credential patterns. See [`docs/PUBLIC-REPO-SAFETY.md`](docs/PUBLIC-REPO-SAFETY.md) for the full audit and current review items.

## 🗂️ Project structure

```text
site/                       Jekyll website source
site/_films/                Film database — one record per film
site/_companies/            Company / ecosystem / builder directory
site/_chronicle/            Editorial news and stories
site/_newsletters/          Published newsletter records
site/_includes/             Shared navigation, footer, and head fragments
site/_layouts/              Shared page structures
site/_data/                 Navigation, credits, and builder data
site/assets/css/            Cinema-frame component styling
site/assets/js/             Progressive-enhancement behavior
site/assets/images/         Local production media
.github/workflows/          Build and GitHub Pages deployment
scripts/                    Repository safety checks

docs/                       Durable research and safety guidance
BUILD-LOG.md                Verified project record
BUILDER-GUIDE.md            Ownership and builder rules
HANDOFF-CURRENT.md          Current project handoff
```

## License and content use

This repository is the collaboration and publishing source for Bitcoin FilmFest. Code and content may carry different rights. Do not reuse festival logos, photography, film stills, contributor names, or third-party editorial material without checking the relevant permission and source notes.
