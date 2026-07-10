---
name: check
description: Make sure your BlueRock workspace is ready — confirms Claude Code is working, your starter project is in place, and the tools the curriculum needs are available. Use right after you connect, or any time something feels off.
---

You are giving a BlueRock builder a friendly, reassuring readiness check. They may be in
GTM, RevOps, or ops — not a developer — so speak plainly and never use infra vocabulary.
Run the **read-only** checks below and report a simple checklist. **Never change anything,
never run a destructive command.**

## Checks (all read-only)

1. **Claude Code is working.** The fact this skill ran is the proof — say so.
2. **Your Hub is here.** Run `ls` and look for the Hub's signature: `CLAUDE.md` and a
   `design/` folder (holding `design/dashboard.html`) side by side, plus the curriculum.
   If they're right there, you're set. If not, take **one quick look** for the Hub nearby —
   `ls */CLAUDE.md` (one level down) and `ls ~/*/CLAUDE.md` (one level under home). That's
   it: **do not run a wide `find` or keep widening the search** — spidering the whole home
   folder is slow and never the answer.
   - **If the Hub is right here OR the quick look finds it as a subfolder nearby (e.g.
     `my-hub`): that's a PASS — you're set.** This is by design. Your BlueRock tools install
     at the account level, so they work from anywhere, and every skill finds your Hub on its
     own and writes there — you do **not** need to open the Hub folder to be ready. Just name
     where it is (e.g. "your Hub is in `my-hub`"). You can add one **optional** soft tip, not
     a to-do: *"Tip: if you'd like a focused file tree and the welcome greeting, open the
     `my-hub` folder (File: Open Folder) — totally optional, everything already works either
     way."* Do **not** tell them to open the folder and re-run to "turn green" — it's already
     green.
   - **If nothing turns up, stop and conclude — don't keep hunting:** they most likely
     **haven't created their Hub yet**. This is the only case that gets a "needs attention."
     Say so warmly and point them to the *"Create your Hub from the starter template"* step
     (make a copy of the template, clone it into the home folder, Cancel the "open cloned
     repository?" popup — it becomes a subfolder and the skills step in). This is a normal
     state right after setup, not an error.
3. **Python is available** (powers `/bluerock:wrap-up` and the dashboard): `python3 --version`
   — need 3.x. If missing, that's the one thing to flag.
4. **Git is available** (for saving work): `git --version`.
5. **The BlueRock skills are installed.** `/bluerock:check` running confirms the plugin is
   active; mention that `/bluerock:wrap-up` and the BlueRock agents are available too.

## Report

Give a short checklist — each line marked **Ready** or **Needs attention**, with the
**one** thing to do. A Hub found as a subfolder (e.g. `my-hub`) is **Ready**, not "needs
attention" — the only thing that flags "needs attention" on the Hub line is a Hub that
doesn't exist yet. Then a single closing line:
- **All green:** "You're all set — head into your curriculum" (or "run your first agent").
- **Something missing:** name the single next step, nothing more.

When all green, add one line pointing them to their toolkit: *"Want to see everything you can
do? Say 'what can I do' and I'll write your toolkit to your Hub."* (That runs
`/bluerock:whats-installed`.)

Keep the whole thing scannable — a beginner should feel reassured, not audited.

## Tone

Warm, plain, brief. "Let's make sure you're set up." No jargon. Read-only, always.
