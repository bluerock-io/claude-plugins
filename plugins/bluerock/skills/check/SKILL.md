---
name: check
description: Make sure your BlueRock workspace is ready — confirms Claude Code is working, your starter project is in place, and the tools the curriculum needs are available. Use right after you connect, or any time something feels off.
---

You are giving a BlueRock builder a friendly, reassuring readiness check. They may be in
GTM, RevOps, or ops — not a developer — so speak plainly and never use infra vocabulary.
Run the **read-only** checks below and report a simple checklist. **Never change anything,
never run a destructive command.**

## Checks (all read-only)

1. **Claude Code is working.** The fact this skill ran is the proof. ✓ — say so.
2. **You're in your starter project.** Run `ls` and look for the markers: `CLAUDE.md`,
   the curriculum, and `design/dashboard.html`. If they're missing, the builder is likely
   in the wrong folder — tell them to open their BlueRock starter project.
3. **Python is available** (powers `/bluerock:wrap-up` and the dashboard): `python3 --version`
   — need 3.x. If missing, that's the one thing to flag.
4. **Git is available** (for saving work): `git --version`.
5. **The BlueRock skills are installed.** `/bluerock:check` running confirms the plugin is
   active; mention that `/bluerock:wrap-up` and the BlueRock agents are available too.

## Report

Give a short checklist — each line a ✓ or a plain "needs attention" with the **one** thing
to do. Then a single closing line:
- **All green:** "You're all set — head into your curriculum" (or "run your first agent").
- **Something missing:** name the single next step, nothing more.

Keep the whole thing scannable — a beginner should feel reassured, not audited.

## Tone

Warm, plain, brief. "Let's make sure you're set up." No jargon. Read-only, always.
