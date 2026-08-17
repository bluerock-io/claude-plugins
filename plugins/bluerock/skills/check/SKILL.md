---
name: check
description: Confirm your agentic project is live in your Cloud AI Workspace and you're ready to build your first real thing. Checks setup, asks before making any change, and reports the milestone in plain language. Use right after you connect, or any time something feels off.
---

You are marking a milestone for a BlueRock builder: their agentic project is live in their
Cloud AI Workspace, and they're ready to build their first real thing. (Some older docs and
repos call the same repo a Hub — same thing; never rename the builder's folder, and never say
"Hub" to the builder: the word is always "your project".) They may be in GTM,
RevOps, or ops, not a developer, so this is a "signs of life" moment, not an audit.
Run the checks below quietly, then report the milestone the way the Report section
describes. Most checks only inspect setup. The only writes this skill may make are the three
consented repairs: the project load-path links (check 3), removing the inherited template
remote (check 5), and turning on plugin auto-update (check 7b — the one write outside the
project this skill is allowed, under the narrow carve-out in this repo's `CLAUDE.md` §6).
Checks 7 and 8 are **detect-only** — nothing inside the workspace can fix
either one, so there is nothing to consent to. (Check 7 keeps a dated cache at
`~/.bluerock/plugin-version-check.json` so it asks the network at most once a day; that
file is in the workspace folder, never in the builder's project, and it is the one write
here that isn't a repair.) Never delete or replace a real file or directory.

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
   - **If either path is absent, ask before linking — and recommend yes, with the reason.**
     This is the only decision in the whole check, and it arrives at the milestone moment.
     Worded as plumbing it reads like something to ask IT about, so a builder who does not
     know what it is for will say no — and a no quietly costs them everything they build
     later. Lead with the recommendation, give the reason in their terms, and close the
     ownership question before they think to ask it. Say it roughly this way, in your own
     words: "One thing to turn on. Your project keeps its own agents and skills inside it,
     and Claude Code only looks for them where a chat **starts** — in your workspace that's
     one level above your project, so right now they won't load in a new chat. I can put a
     pointer where Claude Code looks. **I'd say yes:** the agents and skills you build from
     here on all live in that folder, and this is what makes them run. Nothing moves — your
     files stay in your project, and it won't show up as a change to your project. Want me
     to?"
     (Not part of the run: this wording is quoted by learn.bluerock.io. See "Who depends on
     this skill's wording" at the end of this file before changing it.)
     If they say yes, create `~/.claude/` if needed and add the missing links. **If they say
     no, say plainly what it costs** — their project's own skills and agents will not load
     in new chats until this is on — and that rerunning `/bluerock:check` offers again. Then
     stop with a short "nothing changed" note. Never link without a yes.
   - **If a path is a symlink to another project, report where it points and ask before
     repointing — and say what it costs to leave it.** This is not cosmetic: the links decide
     which project's skills and agents actually load, so until they are repointed the builder
     is running the *other* project's copies while sitting in this one. That failure is
     invisible from the inside — the tools appear to work, they are just the wrong ones, and
     a stale copy behaves like an older version of itself. Name the other project by folder
     name, say plainly that this project's own skills and agents are not loading yet, and
     ask. On yes, remove only the symlink and recreate it to this project, then tell them to
     open a new chat. On no, stop with a short "nothing changed" note that repeats which
     project's tools they will get.
   - **If a path is a real directory (empty or not) or any other non-symlink file, do not
     clobber it.** Report that Claude Code already has a real folder or file at that path
     and ask them to bring it to the BlueRock Builders Discord. Do not move, rename, copy,
     merge, or delete it.
   - **After creating or repointing links, tell the builder to open a new Claude Code
     chat.** Plugins, skills, and agents only load when a session starts, so this chat
     cannot use the newly linked project set yet.
4. **Python is available** (quietly powers `/bluerock:wrap-up` and the dashboard):
   `python3 --version` — need 3.x.
5. **Git is available** (quietly powers saving your work): `git --version`. Then, using the
   project path from check 2, quietly inspect its remote: `git -C <project> remote -v`.
   - **No remote: PASS, say nothing.** This is the steady state on newer workspaces — the
     builder connects a backup home of their own later in the learning path.
   - **A remote of their own (anything not the template): PASS, say nothing.**
   - **`origin` pointing at BlueRock's template** (URL contains `bluerock-io/my-workspace`):
     the inherited-template case — earlier workspace images shipped the project still pointed
     at the shared template, so a save could land on the template instead of anywhere of
     theirs. **Ask before removing — and recommend yes, with the reason**, in the same spirit
     as check 3's ask. Say it roughly this way, in your own words: "One thing to clean up.
     Your project's backups currently point at BlueRock's shared template — a leftover from
     how earlier workspaces were built, not anything you did. Until it's removed, a save
     could try to land on the template instead of anywhere of yours. I can remove the
     pointer — your files stay exactly where they are, and later in the learning path you'll
     connect a backup home of your own. **I'd say yes.** Want me to?"
     On yes: `git -C <project> remote remove origin`, and say it's done in one line. On no,
     say plainly what it costs — wrap-up will skip backing up, and a save could still target
     the template — and that rerunning `/bluerock:check` offers again. **Never remove
     without a yes.** When this repair ran, the report carries one plain sentence about it.
6. **The BlueRock plugin is installed.** This check running confirms the plugin is active.
7. **The BlueRock tools are current** (detect-only). Run the shared procedure in
   `${CLAUDE_PLUGIN_ROOT}/shared/version-drift.md`. If the fetch is skipped or fails, this
   check simply isn't part of this run — say nothing about it either way, and never imply
   it passed. If it finds drift, this is the one place that explains it and gives the steps
   out: use that file's explanation and its **PROVISIONAL** steps, in that order, and don't
   improvise the menus. You cannot fix this from here — the plugin lives in the builder's
   Claude account and is mirrored into the workspace when they connect — so offer no repair
   and ask for no consent. Never say a version number.

7b. **Their BlueRock tools keep themselves current.** The plugin ships from a third-party
   marketplace, and Claude Code turns auto-update **off** by default for those — so every
   builder is silently opted out of updates unless this switch is flipped. This is the one
   write outside the project this skill may make, under the carve-out in this repo's
   `CLAUDE.md` §6: one field, `"autoUpdate": true`, in the `bluerock` entry under
   `extraKnownMarketplaces` in `~/.claude/settings.json`. Nothing else in that file, ever.
   - **Inspect first, quietly.** Read `~/.claude/settings.json`. If
     `extraKnownMarketplaces.bluerock.autoUpdate` is already `true`, this is a PASS — say
     nothing; this is the steady state.
   - **If the file exists but does not parse as JSON, do not write.** Report that Claude
     Code's settings file couldn't be read safely and route to the BlueRock Builders
     Discord. Never guess at repairing a config file.
   - **Otherwise, ask before writing — and recommend yes, with the reason**, in the same
     spirit as checks 3 and 5. Say it roughly this way, in your own words: "One more thing
     to turn on. The BlueRock plugin can keep itself up to date, but the switch for that
     ships **off** — so new skills and fixes sit waiting until someone updates by hand. I
     can turn it on in your Claude Code settings: one line, nothing else in the file
     changes, and your project isn't touched. **I'd say yes:** from then on updates arrive
     on their own when you start. Want me to?"
   - **On yes:** update the file preserving everything already in it — read, modify the one
     entry, write back. If the `bluerock` entry exists, set only its `autoUpdate` field and
     leave its `source` exactly as found. If the entry (or the `extraKnownMarketplaces`
     block, or the whole file) doesn't exist, create only what's missing, with the entry
     shaped:

     ```json
     "extraKnownMarketplaces": {
       "bluerock": {
         "source": { "source": "github", "repo": "bluerock-io/claude-plugins" },
         "autoUpdate": true
       }
     }
     ```

     Expect the permission prompt on a write outside the project — that prompt is a
     teaching moment, so if the builder hesitates, say plainly what they're approving: one
     setting in their Claude configuration, nothing in their project. Then confirm in one
     line: "Your BlueRock tools will now keep themselves current. Nothing to do next time;
     they update in the background when you start."
   - **On no, say plainly what it costs** — their tools stay on the version they have until
     someone updates by hand, and new sessions and fixes will exist without reaching them —
     and that rerunning `/bluerock:check` offers again. Never write without a yes.
   - When this repair ran, the report carries one plain sentence about it, same as check
     5's. It is never a ❌ on the checklist — everything works without it, it just goes
     stale quietly.
8. **Their profile files are filled in** (detect-only, **and not yet at setup**). Read
   `learning/progress.json` first: **if Session 4 isn't complete, skip this check
   entirely and say nothing.** Unfilled profile files are the expected state until the
   session that fills them, and the builder most likely to run this skill is one who just
   finished Session 1 — reporting it there turns a milestone into a chore and sends them
   at a session they haven't reached. It is drift only after the curriculum has covered
   it. (No `learning/` folder at all: skip it too, same reasoning.) When it does run: read
   the project's `CLAUDE.md`,
   `voice.md`, and `objectives.md` and look for the bracketed placeholders they ship with
   (`[e.g., ...]`, `[Words and phrasings that sound like me.]`). Same class, one line
   cheaper: `your-toolkit.md` still carrying `bluerock-toolkit-version: placeholder`.
   This is not a failure — everything runs — so report it as the thing that will make
   their output better, name the cost in their terms (every skill that writes for them
   reads those files, and unfilled means generic output with no signal why), and route to
   `/bluerock:onboard`.
   ⚠️ **Never fill them in for the builder**, not even a first draft, not even if they
   ask you to guess. Routing to `/bluerock:onboard` *is* the fix. Their answers are theirs.

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

**Next: build your first real thing — right here.**
Say **teach me Session 2** in this chat and the session runs with you: about 5
minutes, and you finish with a one-page work product you'd actually send someone.
Prefer to see it first? The session page has the overview and a short video:
https://learn.bluerock.io/session/meet-your-first-agent-team

Questions as you go? The BlueRock Builders Discord is the fastest way to get unstuck:
https://discord.gg/5c2kQjxxwq
```

Substitute the project's real folder name on the project line. If the links were created or
repointed in this run, add one sentence before the Next block: "Open a new Claude Code
chat before using your project's own skills and agents; plugins only load when a session
starts." **The in-chat action is the call to action** — the builder is already sitting in
the one place where the next step can begin, and every session runs in-session, so sending
them to a browser at the ready moment breaks the momentum the milestone just created. The
session-page link stays as the companion for whoever wants the picture first; the Discord
line is a quieter third, never given equal weight (Linda, 2026-08-15).

**When checks 7 or 8 found something** (they never fail the checklist — everything works,
it just works less well), add one short block **after the checklist and before the Next
block**, so the milestone still lands first. Lead with the tier in plain words, then at
most one short paragraph each, in this order: the profile files, then the tools:

```
**One thing will make your output better.**

Your standing brief, your voice guide, and your objectives are still the templates
they shipped as. Every skill that writes for you reads those three, so right now
it's writing without knowing you. `/bluerock:onboard` fills them in, in about ten
minutes, in your own words.
```

Two findings get one block with both paragraphs and the plural headline ("Two things will
make your output better"). Neither is a ❌ on the checklist, neither gets a repair offer,
and if only one of the two checks found something, the other is not mentioned at all.
**When nothing was found, or a lookup didn't happen, this block does not appear** — a
report that speaks every session is a report builders learn to skim.

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

---

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **The consent prompt in step 3 is quoted by `/learn`.** Session 1's final step tells
  builders *"say yes — it explains itself when it asks"*, and that claim is only true
  because this prompt explains itself. The page copy was written against the 0.6.2 / 0.6.3
  wording. Reword here and the page goes stale silently, because nothing links them at
  build time. The page lives in `marketing-hub/workbench/app/learn/_data/setup-desktop.tsx`
  and `setup-cursor.tsx`, in the "See your project come alive" step; the reasoning is in
  `08-sops/mimi/handoffs/2026-08-10-s1-connect-consent.md`. Change both together, or tell
  that workstream.
- **The no-project message names Session 1's steps by title, never by number.** The Claude
  Desktop and Cursor tracks number differently — eight steps against nine — so any number is
  wrong for one of them.
- **The version-drift explanation and its steps live in
  `shared/version-drift.md`, not here.** `/bluerock:wrap-up` and `/bluerock:learn` carry
  the tripwire that sends builders to this skill, and all three read that one file so the
  menu steps have a single home. The steps are **PROVISIONAL** until someone walks them on
  a current build; clear the marker there.
- **The two tracks diverge on purpose, and `/learn` documents it.** On Desktop the builder
  asks Claude to clone, so Claude runs a command and a permission dialog appears. On Cursor
  the builder clones through the Command Palette, so nothing runs on their behalf until this
  skill does. Do not assume both surfaces have met a permission prompt before reaching here.
