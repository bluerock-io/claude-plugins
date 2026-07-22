---
name: check
description: Confirm your AI Work Hub came alive in your cloud workspace and you're ready to build your first real thing. Runs quick read-only checks behind the scenes and reports the milestone in plain language. Use right after you connect, or any time something feels off.
---

You are marking a milestone for a BlueRock builder: their AI Work Hub just came alive in
their cloud workspace, and they're ready to build their first real thing. They may be in
GTM, RevOps, or ops, not a developer, so this is a "you're alive" moment, not an audit.
Run the **read-only** checks below quietly, then report the milestone the way the Report
section describes. **Never change anything, never run a destructive command.**

The checks below are plumbing. The builder should never see `ls`, `python3`, or `git` as
line items; they roll up into the plain-language report.

## Checks (all read-only, run behind the scenes)

1. **Claude Code is working.** The fact this skill ran is the proof.
2. **Your AI Work Hub is here.** Run `ls` and look for the Hub's signature: `CLAUDE.md` and a
   `design/` folder (holding `design/dashboard.html`) side by side, plus the curriculum.
   If they're right there, you're set. If not, take **one quick look** for the Hub nearby:
   `ls */CLAUDE.md` (one level down) and `ls ~/*/CLAUDE.md` (one level under home). That's
   it. **Do not run a wide `find` or keep widening the search** — spidering the whole home
   folder is slow and never the answer.
   - **If the Hub is right here OR the quick look finds it as a subfolder nearby (e.g.
     `my-hub`): that's a PASS — you're set.** This is by design. Your BlueRock tools install
     at the account level, so they work from anywhere, and every skill finds your Hub on its
     own and writes there. You do **not** need to open the Hub folder to be ready. Just name
     where it is (e.g. "your Hub is in `my-hub`"). You can add one **optional** soft tip, not
     a to-do: *"Tip: if you'd like a focused file tree and the welcome greeting, open the
     `my-hub` folder (File: Open Folder) — totally optional, everything already works either
     way."* Do **not** tell them to open the folder and re-run to "turn green" — it's already
     alive.
   - **If nothing turns up, stop and conclude — don't keep hunting:** they most likely
     **haven't created their Hub yet**. This is the one thing that genuinely needs attention.
     Say so warmly and point them to the *"Get the Starter → your AI Work Hub"* step
     (make a copy of the template, clone it into the home folder, Cancel the "open cloned
     repository?" popup — it becomes a subfolder and the skills step in). This is a normal
     state right after setup, not an error.
3. **Python is available** (quietly powers `wrap-up` and the dashboard): `python3 --version`
   — need 3.x.
4. **Git is available** (quietly powers saving your work): `git --version`.
5. **The BlueRock skills are installed.** This check running confirms the plugin is
   active. While here, read the installed plugin **version** from
   `~/.claude/plugins/marketplaces/*/plugins/bluerock/.claude-plugin/plugin.json` — you'll use
   it in the toolkit check.
6. **Your tools are visible + current** (optional, never a blocker). Two light reads,
   both in the Hub:
   - **The visible `toolkit/` folder is present.** Check the Hub root for a `toolkit/`
     folder with `toolkit/skills/` and `toolkit/agents/` inside — the browsable copies of
     every skill and agent (written by `/onboard` on first setup, or
     `/whats-installed` anytime). If it's there, note it. If it's **absent**, that's the soft
     tip below, not a "needs attention" (the plugin still works from the cache; the folder is
     just the window onto it).
   - **The list is current.** `your-toolkit.md` carries a marker line
     `<!-- bluerock-toolkit-version: X.Y.Z -->` on its first line. Compare it to the
     installed version from check 5: **match** → current, nothing to say; **missing, still
     the placeholder, or older** → stale/ungenerated, soft tip below; **can't read either**
     → say nothing, never nag on ambiguity.

## Report

This is a "signs of life" moment, not a checklist to audit. Report it as a milestone.

**When the Hub is here (right here or as a nearby subfolder):**

1. **Lead with the milestone.** Open with *"Your AI Work Hub is alive."* Name where it is if
   it's a subfolder (e.g. "your Hub is in `my-hub`"). This is the payoff line, so it comes
   first.
2. **One line for your tools.** Roll checks 1, 3, 4, and 5 into a single reassurance:
   *"Your tools are ready."* Do **not** list Claude Code, Python, Git, and the plugin as
   separate items. **Surface a specific item only if something is actually wrong** (for
   example, Python missing): then, and only then, name that one thing and the single fix.
   When everything passes, the builder sees one calm line, not four green checks.
3. **Point to the first win.** Close by pointing forward to building the first real thing:
   *"You're ready to build your first real thing — say hello to your first agent team in
   Session 2."* Name the next session; don't send them to "the curriculum" generically.

**When the Hub doesn't exist yet (the one "needs attention" case):**
Say it warmly and give the single next step: create your AI Work Hub from the Starter (the
*"Get the Starter"* step above). One thing to do, nothing more. Hold the tools reassurance
until the Hub is in place.

When the Hub is alive, add one line about their toolkit (from check 6), phrased to the
situation — always a soft invitation, never a "needs attention":
- **Toolkit folder present + current, or you couldn't compare versions:** *"Want to see
  everything you can do? Your tools are in `toolkit/` — open any one, or say 'what can I do'
  to refresh the list."*
- **`toolkit/` folder or list missing / still the placeholder:** *"Want your tools where you
  can see them? Say 'what can I do' and I'll write browsable copies of every skill and agent
  into a `toolkit/` folder in your Hub."*
- **Toolkit is an older version than what's installed:** *"Your BlueRock tools updated since
  your toolkit was written (you're on vX.Y.Z now) — say 'what can I do' to refresh it."*

All three run `/whats-installed`. Refer to tools by their short form (`/wrap-up`, `/today`),
not the long `/bluerock:` form — the short form works and reads friendlier.

Keep the whole thing short and celebratory. A beginner should feel their Hub just came to
life, not that they passed an inspection.

## Tone

Warm, plain, brief. "Your Hub is alive — you're ready to build." No jargon, no line-item
audit. Read-only, always.
