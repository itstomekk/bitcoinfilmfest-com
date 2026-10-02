# GitHub guide for Nomishka

Simple, click-by-click. No command line needed. Everything happens on github.com.

**Your repo (the fork):** https://github.com/Nomishka/bitcoinfilmfest-com-fork
**Tomek's main repo (upstream):** https://github.com/itstomekk/bitcoinfilmfest-com
**Live site:** https://itstomekk.github.io/bitcoinfilmfest-com/

How it flows:

```text
Claude works on a branch → PR into YOUR fork → you review & merge
→ you open a PR from your fork to TOMEK's repo → Tomek reviews & merges → site goes live
```

Only Tomek's `main` publishes the website. Nothing in your fork can break the live site.

---

## Step 1 — Review Claude's pull request (in your fork)

1. Open the PR link Claude gives you (or: your fork → **Pull requests** tab).
2. Read the description at the top — what changed and why.
3. Click **Files changed**. Check:
   - only the expected files are there;
   - text, names, dates, and links are correct;
   - nothing private (emails of contacts, private notes, passwords).
4. Scroll to the bottom and check the **checks**:
   - green ✅ = good;
   - red ❌ = tell Claude "the check failed on PR #…" and it will fix it.
5. Want a change? Click **Files changed** → hover a line → click the blue **+** → write your comment → **Start a review** → **Submit review**. Then tell Claude.

**Preview link:** once Cloudflare previews are set up, the Cloudflare bot posts a comment on each PR with a link. Open it to see the changed website before merging. Check the pages that changed on both a computer and a phone.

## Step 2 — Merge it into your fork

1. On the PR's **Conversation** tab, click **Merge pull request** → **Confirm merge**.
2. Click **Delete branch** (safe — the work is now in `main`).

## Step 3 — Send it to Tomek (upstream PR)

1. Go to your fork's main page.
2. If you see **"This branch is X commits ahead of itstomekk:main"**, click **Contribute** → **Open pull request**.
3. Check the top says: `base repository: itstomekk/bitcoinfilmfest-com` · `base: main` ← `head repository: Nomishka/bitcoinfilmfest-com-fork` · `compare: main`.
4. Title: short and clear, e.g. `Add five new film profiles`.
5. Description: paste the PR description from Step 1 (Claude writes it for you).
6. Click **Create pull request**. Tomek gets notified.

## Step 4 — Keep your fork up to date (do this before asking Claude for new work)

1. Your fork's main page → click **Sync fork** → **Update branch**.
2. If it says there's a conflict, don't guess — tell Claude or Tomek.

## Step 5 — After Tomek merges

1. Wait a few minutes, then open the live site and check the page.
2. The **Actions** tab on Tomek's repo shows a green ✅ when publishing finished.

---

## Rules to remember

- Never merge a PR with a red ❌ check.
- One PR = one topic (e.g. "new films" separately from "homepage text").
- Any website change must include a dated line in `CHANGELOG.md` — Claude adds this, just check it's there.
- The repo is **public**: never add passwords, private contacts, contracts, or private Notion/Drive links.
- Unsure? Ask Claude: "Explain this PR in simple words" or "What should I click next?"

## Useful phrases to give Claude

- "Read the knowledge base and continue from the handoff."
- "Make this change and open a PR into my fork."
- "The check failed on my PR — fix it."
- "Write the description for my upstream PR to Tomek."
- "Update the organisation log and handoff."
