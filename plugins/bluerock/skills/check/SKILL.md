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
2. **You're in your Hub.** Run `ls` and look for the Hub's signature: `CLAUDE.md` and a
   `design/` folder (holding `design/dashboard.html`) side by side, plus the curriculum.
   If they're there, you're set. If they're missing, the session started outside the Hub —
   in an SSH/cloud container it usually starts in the home folder, with the Hub one level
   down. The BlueRock skills load from anywhere, but they read and write files *in the
   Hub*, so this is the one thing that matters most. Help them fix it, don't just flag it:
   find the Hub by its signature, not a fixed name — `ls */CLAUDE.md`, then
   `ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path '*/design/dashboard.html'` — then
   `cd` into that folder (the one they named when they cloned, like `maria-hub`). Tell
   them the exact folder you found and confirm they're in it. Re-run the check to be sure.
3. **Python is available** (powers `/bluerock:wrap-up` and the dashboard): `python3 --version`
   — need 3.x. If missing, that's the one thing to flag.
4. **Git is available** (for saving work): `git --version`.
5. **The BlueRock skills are installed.** `/bluerock:check` running confirms the plugin is
   active; mention that `/bluerock:wrap-up` and the BlueRock agents are available too.

## Report

Give a short checklist — each line marked **Ready** or **Needs attention**, with the
**one** thing to do. Then a single closing line:
- **All green:** "You're all set — head into your curriculum" (or "run your first agent").
- **Something missing:** name the single next step, nothing more.

Keep the whole thing scannable — a beginner should feel reassured, not audited.

## Tone

Warm, plain, brief. "Let's make sure you're set up." No jargon. Read-only, always.
