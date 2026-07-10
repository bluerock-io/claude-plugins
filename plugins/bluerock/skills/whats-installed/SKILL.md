---
name: whats-installed
description: >-
  Show what's in my BlueRock toolkit — the skills and agents I have — and save a
  browsable list to my Hub so I can see them. Use when I say "what can I do",
  "what's installed", "what skills do I have", "what agents do I have", "show my
  toolkit", or "what does the plugin give me".
---

The BlueRock plugin installs at the user level, so its skills and agents don't show up as
files in my Hub — I can't browse what I have. This skill fixes that: read what's actually
installed and write a plain, browsable list into my Hub.

## First — anchor to the Hub

The list belongs in the builder's Hub (the repo they cloned from the starter), not wherever
the session started. In an SSH/cloud container the session usually starts in the **home
folder**, with the Hub one level down. Identify the Hub by its signature, not its name: run
`ls`; if you see `CLAUDE.md` and `design/` side by side, you're in it. If not, find it
(`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`), `cd` in, and capture its **absolute path** with
`pwd` — write `your-toolkit.md` to that full path. Can't find it? Ask the builder to open
their Hub folder. (Do NOT confuse this with `~/.claude/`, which is where the plugin lives —
see below.)

## What to do

1. **Find the installed plugin.** Its files live in the user plugin cache, NOT in the Hub —
   look under `~/.claude/plugins/marketplaces/*/plugins/bluerock/` (skills in
   `skills/*/SKILL.md`, agents in `agents/*.md`, version in `.claude-plugin/plugin.json`).
   If the path differs or you can't find it, fall back to the plugin's `README.md` in that
   cache, or to the slash-command list — but prefer the real files so the list is accurate.
2. **Read the set.** For each **skill**: its `name` + the one-line `description` from the
   SKILL.md frontmatter. For each **agent**: its `name` + `description`. Grab the plugin
   version too.
3. **Write `your-toolkit.md` at the Hub root** — a friendly, browsable reference, overwritten
   in place each run (so it stays current after a plugin update). Shape:
   - A one-line header: how to use these — say what you want in plain language (everyday
     path), or use the `/bluerock:` command (explicit path).
   - **Skills** (things you run): each = name, what it does, and how to trigger it (a plain
     phrase + the `/bluerock:<verb>` command).
   - **Agents** (specialists you point at work): each = name + what it does.
   - Footer: the plugin version and "regenerate this anytime by saying 'what can I do'."
4. **Show a short summary** in the panel — count of skills + agents, plugin version, and
   where you saved it ("Your toolkit → your-toolkit.md"). Don't reprint the whole file.

## Rules

- **Read-only against the plugin.** The only thing you write is `your-toolkit.md` in the Hub.
- **Reflect what's ACTUALLY installed.** Don't invent skills or agents that aren't there; if
  something's missing, say so rather than pad the list.
- Plain English, no infra vocabulary — this is the builder's map of what they can do.
- Re-runnable: overwrite `your-toolkit.md` so it refreshes whenever the plugin updates.
