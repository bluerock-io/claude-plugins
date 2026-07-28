---
name: check
description: Confirm your AI Work Hub is live in your secure workspace and you're ready to build your first real thing. Runs quick read-only checks behind the scenes and reports the milestone in plain language. Use right after you connect, or any time something feels off.
---

You are marking a milestone for a BlueRock builder: their AI Work Hub is live in their
secure workspace, and they're ready to build their first real thing. They may be in GTM,
RevOps, or ops, not a developer, so this is a "signs of life" moment, not an audit.
Run the **read-only** checks below quietly, then report the milestone the way the Report
section describes. **Never change anything, never run a destructive command.**

The checks below are plumbing. The builder should never see `ls`, `python3`, or `git` as
line items; they roll up into the four-line report.

## Naming (applies to everything you write back)

- **BlueRock plugin skills always take the full prefix:** `/bluerock:check`,
  `/bluerock:onboard`, `/bluerock:today`, `/bluerock:wrap-up`, `/bluerock:scorecard`.
  Never write the bare short form for a plugin skill, even though it resolves.
- **Skills and agents seeded in the builder's Hub stay bare:** `/capture`,
  `/meeting-recap`, `/research`, and agents like `daily-brew`, `scribe`, `meeting-prep`.
  They live in the Hub's `.claude/`, not the plugin.
- The word is **"live,"** never "alive."
- The only emoji in the report is the ✅ on the checklist lines. No others.

## Checks (all read-only, run behind the scenes)

1. **Claude Code is working.** The fact this skill ran is the proof.
2. **Your AI Work Hub is here.** Run `ls` and look for the Hub's signature: `CLAUDE.md` and a
   `design/` folder (holding `design/dashboard.html`) side by side, plus the curriculum.
   If they're right there, you're set. If not, take **one quick look** for the Hub nearby:
   `ls */CLAUDE.md` (one level down) and `ls ~/*/CLAUDE.md` (one level under home). That's
   it. **Do not run a wide `find` or keep widening the search** — spidering the whole home
   folder is slow and never the answer.
   - **If the Hub is right here OR the quick look finds it as a subfolder nearby (e.g.
     `my-hub`): that's a PASS.** This is by design: the Hub runs *inside* the workspace, so
     in the cloud workspace the session starts at the workspace root with the Hub one level
     down. BlueRock tools install at the account level and every skill finds the Hub on its
     own, so the builder does not need to open the Hub folder. Just name where it is.
   - **Never suggest opening the Hub folder** (`File → Open Folder`, a new window, or
     reopening the project). In the cloud workspace that reloads the window over the
     connection and drops the attach. There is no upside to offer and a real cost. If the
     Hub is found, say nothing about folders beyond naming where it is.
   - **If nothing turns up, stop and conclude — don't keep hunting:** they most likely
     **haven't created their Hub yet**. This is the one thing that genuinely needs attention.
     Say so warmly and send them back to Session 1, steps 6 and 7 (make their own copy of the
     Starter project, then clone it into their workspace). This is a normal state right after
     setup, not an error.
3. **Python is available** (quietly powers `/bluerock:wrap-up` and the dashboard):
   `python3 --version` — need 3.x.
4. **Git is available** (quietly powers saving your work): `git --version`.
5. **The BlueRock plugin is installed.** This check running confirms the plugin is active.

## Report

This is a "signs of life" milestone: headline, then the receipt, then where to go next.
Four checklist lines, always in this order, each one ✅ when it passes. Keep every line in
builder language — no bare command names, no version numbers.

**When the Hub is here (right here or as a nearby subfolder):**

```
**Your AI Work Hub is live.**

✅ **Claude Code** — running
✅ **Your Hub** — `my-ai-work-hub`
✅ **The BlueRock plugin** — your skills and agents are ready
✅ **Under the hood** — Python and Git ready

Your Hub runs in your workspace, and every BlueRock skill writes there.

**Next: build your first real thing.**
Session 2 — Meet your first agent team:
https://learn.bluerock.io/session/meet-your-first-agent-team

Questions as you go? The BlueRock Builders Discord is the fastest way to get unstuck:
https://discord.gg/5c2kQjxxwq
```

Substitute the Hub's real folder name on the Hub line. Keep the Session 2 link and the
Discord line — the builder is in an editor panel, not a browser, and naming the session
without linking it is where momentum dies. The Session 2 link is the call to action; the
Discord line is a quieter second, never given equal weight.

**If exactly one thing fails** (say Python is missing): mark that line ❌ instead of ✅, keep
the other three, and put the single fix directly under the checklist in place of the "Next"
block. One thing to do, nothing more. Don't turn a single failure into a report about
everything that could be wrong.

**When the Hub doesn't exist yet (the one "needs attention" case):**

```
**Your Hub isn't here yet** — that's normal right after setup, and it's a quick fix.

Head back to Session 1 and do steps 6 and 7: make your own copy of the Starter project,
then clone it into your workspace.
https://learn.bluerock.io/get-started

Stuck on it? Ask in the Discord: https://discord.gg/5c2kQjxxwq
```

Hold the checklist until the Hub is in place — a receipt for tools with nowhere to write
isn't reassuring.

Keep the whole thing short. A beginner should feel their Hub just came to life, not that
they passed an inspection.

## Tone

Warm, plain, brief, and guiding — always end pointing at the next action, with a link.
No jargon, no hedging, no reassurance about problems they haven't raised. Read-only, always.
