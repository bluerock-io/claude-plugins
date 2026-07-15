---
name: whats-installed
description: >-
  Show what's in my BlueRock toolkit — the skills and agents I have — and save a
  browsable list plus read-only copies of the actual skill/agent files into my
  Hub so I can open and read them. Use when I say "what can I do", "what's
  installed", "what skills do I have", "what agents do I have", "show my toolkit",
  or "what does the plugin give me".
---

The BlueRock plugin installs at the user level, so its skills and agents don't show up as
files in my Hub — they live in an opaque plugin cache I can't browse. This skill fixes that:
read what's actually installed, write a plain browsable list, AND drop read-only copies of the
real skill/agent files into my Hub so I can open and read them in my file tree.

## First — anchor to the Hub

Everything this skill writes belongs in the builder's Hub (the repo they cloned from the
starter), not wherever the session started. In an SSH/cloud container the session usually
starts in the **home folder**, with the Hub one level down. Identify the Hub by its signature,
not its name: run `ls`; if you see `CLAUDE.md` and `design/` side by side, you're in it. If
not, find it (`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`), `cd` in, and capture its **absolute
path** with `pwd` — write to that full path. Can't find it? Ask the builder to open their Hub
folder. (Do NOT confuse the Hub with `~/.claude/`, which is where the plugin lives — see below.)

## What to do

1. **Find the installed plugin.** Its files live in the user plugin cache, NOT in the Hub —
   look under `~/.claude/plugins/marketplaces/*/plugins/bluerock/` (skills in
   `skills/*/SKILL.md`, agents in `agents/*.md`, version in `.claude-plugin/plugin.json`).
   If the path differs or you can't find it, fall back to the plugin's `README.md` in that
   cache, or to the slash-command list — but prefer the real files so everything is accurate.
2. **Read the set.** For each **skill**: its `name` + the one-line `description` from the
   SKILL.md frontmatter. For each **agent**: its `name` + `description`. Grab the plugin
   version too.
3. **Write `your-toolkit.md` at the Hub root** — a friendly, browsable reference, overwritten
   in place each run. Shape:
   - **First line — a version marker, exactly this format:**
     `<!-- bluerock-toolkit-version: X.Y.Z -->` where `X.Y.Z` is the installed plugin
     version from step 2. This is a machine marker `/bluerock:check` reads to tell the builder
     when their toolkit is out of date — always write it, always the real version, never a
     placeholder.
   - A one-line header: how to use these — say what you want in plain language (everyday path),
     or use the `/bluerock:` command (explicit path).
   - **Group everything by what it's FOR, not by skill-vs-agent.** A builder thinks "I'm
     prepping a meeting," not "I need an agent." Use these categories, in this order, and put
     each installed skill and agent under the one that fits:

     | Category | What it's for | Belongs here |
     |---|---|---|
     | **Set up your Hub** | Getting oriented and staying current | `onboard`, `check`, `whats-installed` |
     | **Your daily rhythm** | The loop that runs your day | `daily-brew`, `today`, `capture` (+ `scribe`), `wrap-up` |
     | **Meetings** | Before a call, after a call | `meeting-prep`, `meeting-recap` |
     | **Account research** | Point a team at a company | `research` (+ `researcher`, `signal-scanner`, `composer`) |

   - Under each category, list its items. For a **skill** (something you run): name, what it
     does, and how to trigger it (a plain phrase + the `/bluerock:<verb>` command). For an
     **agent** (a specialist you point at work): name + what it does. A one-word tag —
     `(run)` for skills, `(specialist)` for agents — keeps the distinction without splitting
     the list.
   - **Anything installed that doesn't match a category above goes in a final "More in your
     toolkit" group** — never drop it, never force it into the wrong category. This keeps the
     map honest as the plugin grows (new vertical packs and skills will land here until this
     skill learns their category).
   - A line pointing to the files: "Want to read how any of these actually work? Open the
     `toolkit/` folder — it holds a copy of every skill and agent."
   - Footer: the plugin version (human-readable, e.g. "Generated from the BlueRock plugin
     vX.Y.Z") and "regenerate this anytime by saying 'what can I do'."
4. **Mirror the actual files into a visible `toolkit/` folder at the Hub root** — so the
   builder can open and read every skill and agent in their file tree (the live versions run
   from the plugin, which isn't browsable). For each skill, copy its `SKILL.md` to
   `toolkit/skills/<name>.md`; for each agent, copy its file to `toolkit/agents/<name>.md`.
   Copy the **full, verbatim** content, and **prepend** this note as the first lines of each
   copy (fill in the real version):
   ```
   > Reference copy — this is what's installed via your BlueRock plugin (vX.Y.Z). The live
   > version runs from the plugin; editing this file does nothing. To make one yours, copy it
   > into .claude/commands/<name>/SKILL.md (a skill) or .claude/agents/<name>.md (an agent) and
   > change it there. Refresh these copies anytime by saying "what can I do".
   ```
   Also write `toolkit/README.md` — one short paragraph on what the folder is (read-only
   reference copies of your installed toolkit), how to fork-to-own, and that it refreshes on
   re-run — with `<!-- bluerock-toolkit-version: X.Y.Z -->` as its first line.
   Use your file tools (read each plugin file, write the copy) so this works even if the shell
   is unavailable. **Overwrite the `toolkit/` folder each run** so it tracks plugin updates.
   Only ever write inside `toolkit/` and the Hub-root `your-toolkit.md`; never delete anything
   else.
5. **Show a short summary** in the panel — count of skills + agents, plugin version, and where
   you saved things ("Your toolkit → `your-toolkit.md`; the full files → `toolkit/`"). Don't
   reprint the files.

## Rules

- **Read-only against the plugin.** You only write in the Hub: `your-toolkit.md` and the
  `toolkit/` folder. Never modify the plugin cache, and never touch the builder's own
  `.claude/` files.
- **Reflect what's ACTUALLY installed.** Don't invent skills or agents that aren't there; if
  something's missing, say so rather than pad the list.
- **Copies are verbatim + clearly marked reference.** Every mirrored file carries the "reference
  copy — editing does nothing, fork to own" note so a builder never edits a dead copy by mistake.
- Plain English, no infra vocabulary — this is the builder's map of what they can do.
- Re-runnable: overwrite `your-toolkit.md` and the `toolkit/` folder so both refresh whenever
  the plugin updates.
