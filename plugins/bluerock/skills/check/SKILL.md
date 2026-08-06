---
name: check
description: Confirm your agentic project is live in your secure workspace and you're ready to build your first real thing. Checks setup, asks before making any change, and reports the milestone in plain language. Use right after you connect, or any time something feels off.
---

You are marking a milestone for a BlueRock builder: their agentic project is live in their
secure workspace, and they're ready to build their first real thing. (Some older docs and
repos call the same repo a Hub — same thing; never rename the builder's folder.) They may be in GTM,
RevOps, or ops, not a developer, so this is a "signs of life" moment, not an audit.
Run the checks below quietly, then report the milestone the way the Report section
describes. Most checks only inspect setup. The only write this skill may make is the
consented project load-path repair in step 3. Never delete or replace a real file or
directory.

The checks below are plumbing. The builder should never see `ls`, `python3`, or `git` as
line items; they roll up into the four-line report.

## Naming (applies to everything you write back)

- **BlueRock plugin skills always take the full prefix:** `/bluerock:check`,
  `/bluerock:onboard`, `/bluerock:today`, `/bluerock:wrap-up`, `/bluerock:scorecard`,
  `/bluerock:messaging-doc`, `/bluerock:help`.
  Never write the bare short form for a plugin skill, even though it resolves.
- **The builder's project contains their own skills and agents** in `.claude/skills/` and
  `.claude/agents/`. When the builder asks for something those cover, read the matching
  file from the project and follow it. Do not offer project-seeded skills as slash commands; the
  project files are the source of truth before and after the load-path repair.
- The word is **"live,"** never "alive."
- The only emoji in the report is the ✅ on the checklist lines. No others.

## Checks (run behind the scenes)

1. **Claude Code is working.** The fact this skill ran is the proof.
2. **Your project is here.** Run `ls` and look for the project's signature: `CLAUDE.md` and a
   `design/` folder (holding `design/dashboard.html`) side by side, plus the learning path.
   If they're right there, you're set. If not, take **one quick look** for the project nearby:
   `ls */CLAUDE.md` (one level down) and `ls ~/*/CLAUDE.md` (one level under home). If
   several match, choose the one with `design/dashboard.html`. If those quick checks do not
   find it, run only this bounded tiebreaker: `find ~ -maxdepth 3 -path '*/design/dashboard.html'`.
   Once you identify the project, use its **absolute path** — the match you just found already
   gives you one (e.g. `/home/ubuntu/my-hub`) — and use that full path for the load-path
   check. **Do not use `pwd` to get it:** the session starts at the workspace root, not
   inside the project, so `pwd` returns the workspace root and the links in step 3 would point
   at themselves. **Do not run a wider `find` or keep widening the search** — spidering
   the whole home folder is slow and never the answer.
   - **If the project is right here OR the quick look finds it as a subfolder nearby (e.g.
     `my-hub`): that's a PASS.** This is by design: the project runs *inside* the workspace, so
     in the cloud workspace the session starts at the workspace root with the project one level
     down. BlueRock tools install at the account level and every skill finds the project on its
     own, so the builder does not need to open the project folder. Just name where it is.
   - **Never suggest opening the project folder** (`File → Open Folder`, a new window, or
     reopening the project). In the cloud workspace that reloads the window over the
     connection and drops the attach. There is no upside to offer and a real cost. If the
     project is found, say nothing about folders beyond naming where it is.
   - **If nothing turns up, stop and conclude — don't keep hunting:** they most likely
     **haven't created their project yet**. This is the one thing that genuinely needs attention.
     Say so warmly and send them back to Session 1 — the **Make your own copy of the starter
     kit** and **Clone your project into your workspace** steps. Name those steps, never their
     numbers: the Claude Desktop and Cursor tracks number their steps differently, so a number
     is wrong for one of them. This is a normal state right after setup, not an error.
3. **The project's own skills and agents can load in new chats.** Use the project path found in
   step 2. Look for `.claude/agents/` and `.claude/skills/` inside that project.
   - **If either project folder is missing, create no links.** Stop after the plumbing checks
     and report the stale-project case in plain language: the project is here, but it does not
     yet include the starter skills and agents. Do not seed files.
   - **If `~/.claude/agents` and `~/.claude/skills` already symlink to this project's
     matching folders, this is a PASS.** Say nothing extra; this is the steady state.
   - **If either path is absent, ask before linking.** Propose the two links in one plain
     line: "I found your project. To make the skills and agents inside it available from new
     chats, I can link `~/.claude/skills` and `~/.claude/agents` to your project. The files
     stay in your project repo; the links live outside it and will not show in `git status`.
     Do you want me to do that?" If they say yes, create `~/.claude/` if needed and add
     the missing links. If they say no, stop with a short "nothing changed" note.
   - **If a path is a symlink to another project, report where it points and ask before
     repointing.** On yes, remove only the symlink and recreate it to this project. On no,
     stop with a short "nothing changed" note.
   - **If a path is a real directory (empty or not) or any other non-symlink file, do not
     clobber it.** Report that Claude Code already has a real folder or file at that path
     and ask them to bring it to the BlueRock Builders Discord. Do not move, rename, copy,
     merge, or delete it.
   - **After creating or repointing links, tell the builder to open a new Claude Code
     chat.** Plugins, skills, and agents only load when a session starts, so this chat
     cannot use the newly linked project set yet.
4. **Python is available** (quietly powers `/bluerock:wrap-up` and the dashboard):
   `python3 --version` — need 3.x.
5. **Git is available** (quietly powers saving your work): `git --version`.
6. **The BlueRock plugin is installed.** This check running confirms the plugin is active.

## Report

This is a "signs of life" milestone: headline, then the receipt, then where to go next.
Four checklist lines, always in this order, each one ✅ when it passes. Keep every line in
builder language — no bare command names, no version numbers.

**When the project is here (right here or as a nearby subfolder):**

```
**Your agentic project is live.**

✅ **Claude Code** — running
✅ **Your project** — `my-ai-work-hub`
✅ **The BlueRock plugin** — ready
✅ **Under the hood** — Python and Git ready

Your project runs in your workspace, and every BlueRock skill writes there. Your project's own
skills and agents are linked for new chats.

**Next: build your first real thing.**
Session 2 — Meet your first agents:
https://learn.bluerock.io/session/meet-your-first-agent-team

Questions as you go? The BlueRock Builders Discord is the fastest way to get unstuck:
https://discord.gg/5c2kQjxxwq
```

Substitute the project's real folder name on the project line. If the links were created or
repointed in this run, add one sentence before the Next block: "Open a new Claude Code
chat before using your project's own skills and agents; plugins only load when a session
starts." Keep the Session 2 link and the
Discord line — the builder is in an editor panel, not a browser, and naming the session
without linking it is where momentum dies. The Session 2 link is the call to action; the
Discord line is a quieter second, never given equal weight.

**When the project is here but its seeded `.claude/` folders are missing:**

```
**Your project is here, but it is missing its starter skills and agents.**

I did not create links because those folders are not in your project yet. Ask in the
BlueRock Builders Discord and share your project folder name:
https://discord.gg/5c2kQjxxwq
```

**When `~/.claude/agents` or `~/.claude/skills` is a real directory or another
non-symlink file:**

```
**Your project is here, but Claude Code already has files where the project links would go.**

I did not change or replace them. Ask in the BlueRock Builders Discord and share what
`~/.claude/agents` and `~/.claude/skills` contain:
https://discord.gg/5c2kQjxxwq
```

**If exactly one thing fails** (say Python is missing): mark that line ❌ instead of ✅, keep
the other three, and put the single fix directly under the checklist in place of the "Next"
block. One thing to do, nothing more. Don't turn a single failure into a report about
everything that could be wrong.

**When the project doesn't exist yet (the one "needs attention" case):**

```
**Your project isn't here yet** — that's normal right after setup, and it's a quick fix.

Head back to Session 1 and do two steps: **Make your own copy of the starter kit**, then
**Clone your project into your workspace**.
https://learn.bluerock.io/get-started

Stuck on it? Ask in the Discord: https://discord.gg/5c2kQjxxwq
```

Hold the checklist until the project is in place — a receipt for tools with nowhere to write
isn't reassuring.

Keep the whole thing short. A beginner should feel their project just came to life, not that
they passed an inspection.

## Tone

Warm, plain, brief, and guiding — always end pointing at the next action, with a link.
No jargon, no hedging, no reassurance about problems they haven't raised.
