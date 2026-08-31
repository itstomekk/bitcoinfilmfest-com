# /cinema/ front-matter schema

Reference for anyone adding a film or company entry. See `PLAN-CINEMA.md` (repo root) for the full phased plan and the data-source boundary rules — read that before pulling anything from the private research KB into either collection.

Both collections are plain Jekyll collections: one Markdown file per entry, front matter carries the structured fields, the Markdown body (optional) renders as longer-form prose on the profile page below the fields. Filenames become the URL slug (`site/_films/one-attempt-remaining.md` → `/cinema/films/one-attempt-remaining/`) — use lowercase, hyphenated, no special characters.

## Film entry (`site/_films/*.md`)

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `title` | string | yes | Display title, as the public would recognize it. |
| `year` | number | yes | Release year, or expected year for unreleased titles. |
| `type` | string | yes | One of: `Feature`, `Documentary`, `Short`, `TV`, `Stage`. |
| `status` | string | yes | One of: `released`, `in-production`, `upcoming`, `development`. |
| `essential_rank` | number | no | Editorial rank for the Cinema hub's curated Top 10. Lower numbers appear first. |
| `director` | string or `null` | no | Omit or `null` if unconfirmed. |
| `cast` | list of strings | no | Notable cast only, not a full call sheet. |
| `studio` | string | no | Studio/network/production company name, as public sources credit it. |
| `company` | string (slug) | no | Cross-link to a matching `_companies/` entry by filename slug, once one exists. Leave `null` until it does — don't invent the company entry just to fill this field. |
| `country` | string | no | Production country. |
| `runtime` | number or `null` | no | Minutes. |
| `synopsis` | string (block) | yes | 1–3 sentences, public voice — rewritten, not copy-pasted researcher notes. |
| `bitcoin_angle` | string (block) | yes | What makes this Bitcoin cinema, in public voice. This is the field most likely to carry KB researcher phrasing by accident — always rewrite. |
| `platform` | string or `null` | no | Where to watch, if known (e.g. "Netflix", "Amazon Prime Video"). |
| `trailer` | URL or `null` | no | YouTube link preferred. |
| `sources` | list of `{label, url}` | yes | 1–3 credible public sources. Never link BFF-internal files. |
| `bff_screening` | string or `null` | no | e.g. `"BFF26 Official Selection"` — only when true; ties the database back to the festival. |
| `featured` | boolean | no | Surfaces the entry in the `/cinema/` hub's curated highlights. Keep this to a small, deliberately curated set. |

## Company entry (`site/_companies/*.md`)

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `title` | string | yes | Company/platform/venue name. |
| `type` | string | yes | One of: `Studio`, `Production Company`, `Distribution`, `Funding Platform`, `Venue`. |
| `established` | string or number | no | Year or approximate ("est. 2019"). |
| `status` | string | yes | One of: `active`, `defunct`, `stalled`, `status-uncertain`. |
| `founders` | list of strings | no | |
| `location` | string | no | City/country. |
| `website` | URL or `null` | no | |
| `bitcoin_angle` | string (block) | yes | What makes this a Bitcoin-cinema company, public voice. |
| `productions` | list of strings | no | Notable film titles, plain text — cross-link via each film's own `company` field, not the reverse, to avoid two places needing to stay in sync. |
| `sources` | list of `{label, url}` | yes | 1–3 credible public sources. |
| `featured` | boolean | no | Same as films — small curated set for the hub. |

## What never goes in either collection

Per `PLAN-CINEMA.md`'s data-source boundary — copied here so it's visible right next to the schema, not just in the plan doc:

- Internal KB tags: `[sourcing-pending]`, `[unverifiable]`, `[scope-review]`, `[adjacent]`, `[not-a-film]`, `[duplicate]`, `[stalled]` (as a bracketed tag — `status: stalled` as a plain field value is fine)
- Contact names, emails, BFF-internal notes, sourcing commentary written for the research team
- Anything without at least one credible public source
- BFF-PARTNERS-DATABASE.md entries — those are event sponsors, not Bitcoin-cinema companies; don't add them here

## Adding an entry

1. Confirm the source material has clean public sourcing (a mainstream outlet, an official studio/streamer announcement, or similar) — check `UNCERTAINTY.md` first if in doubt.
2. Copy the relevant KB entry's facts, rewriting `synopsis`/`bitcoin_angle` in plain public voice.
3. Save as `site/_films/{slug}.md` or `site/_companies/{slug}.md`.
4. Build locally, check the profile page renders and the entry appears on the matching index page.
5. PR as usual per `HANDOFF-CURRENT.md`'s workflow.
