# /cinema/ — small-task handoff for delegated agents

**Read this whole file before doing anything.** It is written for a small/low-tier agent working alone, with no memory of other agents' work. Every task below is self-contained — you should not need to read `PLAN-CINEMA.md` or the KB's full structure to complete one, though links are given if you want more context.

## Before you start — 3 rules that override everything else

1. **Never invent facts.** Every field you write must come from the source file/line given in your task, or from a source URL you can see with your own eyes. If a fact isn't there, leave the field empty (`null` or omit it) — do not guess, estimate, or fill a gap "reasonably."
2. **Never copy these tags or notes into the public file, even by accident:** `[sourcing-pending]`, `[unverifiable]`, `[scope-review]`, `[adjacent]`, `[not-a-film]`, `[duplicate]`, `[stalled]`, any line starting `**Notes:**` that discusses *how the research was done* (contact names, "3rd research pass," internal disputes). These are private research annotations. Only copy the plain facts (director, cast, country, what the film is about, sources).
3. **If anything is ambiguous, stop and write it in your task's "Questions" section instead of guessing.** A short list of unanswered questions is a good outcome. A wrong or invented fact is not.

## What this is

`/cinema/` is a new section of bitcoinfilmfest.com — a public film database (`/cinema/films/`) and company directory (`/cinema/companies/`) proving Bitcoin cinema is a real, active industry. Full background: `PLAN-CINEMA.md` in this repo root. Field-by-field schema: `site/_cinema-schema.md`. You mostly need the schema, not the plan.

Each film or company is **one Markdown file**. Adding one is a self-contained task — no code, no build step required from you, just a correctly-formatted file.

## Repo basics for every task

- Work in `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\website\rebuild-jekyll` (or wherever this repo is checked out for you).
- Films go in `site/_films/{slug}.md`. Companies go in `site/_companies/{slug}.md`.
- `{slug}` = lowercase, hyphens instead of spaces, no punctuation. Example: "The Gimp and the Hitman" → `the-gimp-and-the-hitman.md`.
- **Before creating a file, check it doesn't already exist** (`ls site/_films/` / `ls site/_companies/`) — another agent may have already done this task.
- Source facts come from `C:\Users\Lenovo\OneDrive\Bitcoin FilmFest\Claude news\bitcoin-cinema-kb.md` — a large private file. Use the line number given in your task to jump straight to the right entry (in most editors: Ctrl+G / Go to Line). Do not read the whole file.
- When done, list the file you created in your task's output. Do not commit/push yourself unless your task explicitly says to — a human or a dedicated integration task will batch-commit.

## Two starter task cards (fully worked examples — read these first)

Use these as your template for the field-by-field style expected in every task below.

<details>
<summary>Example: film entry</summary>

Source: `bitcoin-cinema-kb.md` line 60, entry "The Gimp and the Hitman."

```yaml
---
title: "The Gimp and the Hitman"
year: 2024
type: Feature
status: released
director: "Dimitri Raft"
cast:
  - "Jon-Paul Gates"
  - "Gina Stavroulaki"
  - "Lia Ikkos"
  - "Dimitri Raft"
studio: "Baby D Productions"
company: null
country: "Greece"
runtime: null
synopsis: >
  A scheming couple try to embezzle the Bitcoin fortune of a wealthy professor
  who has put his entire net worth into Bitcoin. A dark comedy-thriller of
  manipulation, seduction, and double-crosses, shot in Athens.
bitcoin_angle: >
  Bitcoin is the central prize driving the heist plot — the professor's
  all-in Bitcoin holdings are what every character is scheming to get their
  hands on.
platform: null
trailer: "https://www.youtube.com/watch?v=YH6zkQTu1DA"
sources:
  - label: IMDB
    url: "https://www.imdb.com/title/tt19799572/"
  - label: Baby D Productions
    url: "https://www.babydproductions.com/post/new-trailer-gimp-and-the-hitman"
bff_screening: "BFF'26 Official Selection"
featured: true
---
```

Saved as `site/_films/the-gimp-and-the-hitman.md`. Notice: `synopsis` and `bitcoin_angle` are rewritten in plain public language, not copied from the KB's researcher notes. `company` is `null` because there's no matching `_companies/` entry yet — don't invent one just to fill the field.

</details>

<details>
<summary>Example: company entry</summary>

Source: `bitcoin-cinema-kb.md` line 2153, entry "Angel Studios."

```yaml
---
title: "Angel Studios"
type: Studio
established: 2013
status: active
founders:
  - "Neal Harmon"
  - "Daniel Harmon"
  - "Jeffrey Harmon"
  - "Jordan Harmon"
location: "Provo, Utah, USA"
website: "https://www.angel.com"
bitcoin_angle: >
  A publicly traded film studio (NYSE: ANGX) holding Bitcoin as a strategic
  treasury reserve — describing it as "a for-profit endowment for the arts
  based on the Bitcoin standard," meant to fund filmmakers for generations.
  Also produced the first kids' TV episodes built around Bitcoin, part of its
  Tuttle Twins animated series.
productions:
  - "Sound of Freedom"
  - "Cabrini"
  - "Tuttle Twins"
  - "Bitcoin Brigade: Adventures in Satoshi City"
sources:
  - label: Angel Studios IPO announcement
    url: "https://www.angel.com/press/release/angel-studios-to-become-a-publicly-traded-company-via-business-combination"
  - label: Fintech.tv profile
    url: "https://fintech.tv/angel-studios-goes-public-a-new-era-for-values-driven-storytelling/"
featured: true
---
```

Saved as `site/_companies/angel-studios.md`.

</details>

## Full field reference

Copy this table into your working notes — don't go re-read `_cinema-schema.md` unless something here is unclear.

**Film fields:** `title` (string, required), `year` (number, required), `type` (one of `Feature`/`Documentary`/`Short`/`TV`/`Stage`, required), `status` (one of `released`/`in-production`/`upcoming`/`development`, required), `director` (string or omit), `cast` (list of strings or omit), `studio` (string or omit), `company` (slug of a matching `_companies/` file, or `null` — only fill if that file already exists), `country` (string or omit), `runtime` (number of minutes or omit), `synopsis` (1-3 sentences, required, your own words), `bitcoin_angle` (1-3 sentences, required, your own words), `platform` (string or omit), `trailer` (YouTube URL or omit), `sources` (list of `{label, url}`, required, 1-3 items), `bff_screening` (string like `"BFF'26 Official Selection"`, or omit — only if actually true), `featured` (`true` only for the small curated set your task tells you to mark — default omit/false).

**Company fields:** `title` (required), `type` (one of `Studio`/`Production Company`/`Distribution`/`Funding Platform`/`Venue`, required), `established` (year or string like `"est. 2019"`, or omit), `status` (one of `active`/`defunct`/`stalled`/`status-uncertain`, required), `founders` (list of strings or omit), `location` (string or omit), `website` (URL or omit), `bitcoin_angle` (required, your own words), `productions` (list of plain-text film titles or omit), `sources` (required, 1-3 items), `featured` (same rule as films).

## Task list — Phase 1 (first batch, one task per entry)

Each row below is one task. Assign each to a separate agent run. Every task follows the same recipe:

1. Open `bitcoin-cinema-kb.md` at the given line.
2. Read that single entry (stop at the next `###` heading or `---`).
3. Fill the schema fields above from what's actually written there.
4. Rewrite `synopsis` and `bitcoin_angle` in your own plain words — do not copy researcher phrasing verbatim, and strip any bracketed tags per Rule 2 above.
5. Save as `site/_films/{slug}.md` or `site/_companies/{slug}.md`.
6. Report back: file created, and a "Questions" list of anything you weren't sure about (leave it empty if none).

### Films

| # | Title | KB line | Notes for this task |
|---|---|---|---|
| F1 | One Attempt Remaining | 208 | `status: in-production`. Netflix/21 Laps. |
| F2 | Dutch & Razzlekhan | 176 | `status: in-production`. Amazon MGM. Note: a *separate, stalled* Amazon MGM project also called "Razzlekhan" (different director) exists in the KB — read carefully, don't merge them into one entry. If genuinely unsure which is which, stop and flag it rather than guessing. |
| F3 | Money Electric: The Bitcoin Mystery | 1323 | `status: released`. HBO, dir. Cullen Hoback. |
| F4 | Hotel Bitcoin | 403 | `status: released`. Netflix. |
| F5 | The Satoshi Affair | 389 | `status: development`. David O. Sacks Productions. |
| F6 | Cold Wallet | 109 | `status: released`. SXSW premiere, Amazon/theatrical. |
| F7 | Sovereign | 74 | `status: released`. **Do not mark `featured: true` without asking first** — this entry is tagged `[adjacent]` in the KB (Bitcoin is never mentioned in the film itself). Build the file with everything else, but leave `featured` unset and write "flagging: this is a [adjacent] entry, is it OK to publish?" in your Questions section. A human needs to decide the site's policy on adjacent content before this one goes live-featured. |

### Companies

| # | Name | KB line | Notes for this task |
|---|---|---|---|
| C1 | Bitfilm Production | 2167 | `status: active`. |
| C2 | New Roots Films | 2178 | `status: active`. The KB entry also mentions a second production, *Bitcoin Millionaires*, flagged `⚠️ scope-borderline` inside the KB — do not list it under `productions:` for this task; only list *God Bless Bitcoin* and *God Bless Bitcoin: Layer 2*. |
| C3 | Whitepaper Studio (with Forager) | 2190 | `status: active`. `type: Funding Platform`. This is two related entities (Forager + Whitepaper Studio) — use "Whitepaper Studio" as the title, mention Forager in the bitcoin_angle text since it's the parent/related studio. |
| C4 | Geyser Fund | 2216 | `status: active`. `type: Funding Platform`. |
| C5 | Ordain | 2205 | `status: active`. `type: Funding Platform`. |
| C6 | Custos Media Technologies | 2239 | The KB flags this one `⚠️ Status uncertain` — use `status: status-uncertain`, not `active`. `type: Distribution`. |

## After Phase 1 tasks are done — integration task (assign to one capable agent, not a small one)

This step needs judgment and should NOT be split further:

1. Confirm all 13 files above exist and pass this checklist per file: required fields present, `type`/`status` use only the allowed values, no banned tags anywhere in the file, `sources` has at least 1 real URL.
2. Run a real local Jekyll build (`bundle exec jekyll build --trace` from `site/`) — this has not been possible from the cloud sandbox that built Phase 0 (no ruby-dev headers). Needs to happen on a machine with a working Ruby/Jekyll install.
3. Spot-check 3-4 profile pages and both index pages render correctly, desktop and mobile.
4. Decide the open `[adjacent]` policy question raised by F7 (Sovereign) — see `PLAN-CINEMA.md`'s "Open items."
5. Commit and push (or open the PR) for the whole Phase 0 + Phase 1 batch together, since Phase 0 is also still uncommitted as of this handoff.

## Later phases (do not start until Phase 1 + integration above is done and confirmed live)

`PLAN-CINEMA.md` has the full Phase 2 (batch-migrate the rest of the KB's ~150 remaining entries, ~15-20 at a time) and Phase 3 (companies backlog, in-production strip, news feed, cross-linking) plans. Once Phase 1 is proven live, the same "one task = one file, one KB line pointer" pattern extends directly — a human just needs to pull the next batch of KB line numbers and write task cards the same shape as the table above.

---
*Written 2026-08-30 for delegation to multiple small/low-tier agents. Pairs with `PLAN-CINEMA.md` (full plan) and `site/_cinema-schema.md` (schema source of truth — this file's field reference is copied from it for convenience; if they ever disagree, `_cinema-schema.md` wins).*
