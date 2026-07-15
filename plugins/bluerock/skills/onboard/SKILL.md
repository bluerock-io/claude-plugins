---
name: onboard
description: >-
  Get to know me and set up my Hub so it knows who I am, what I'm working on,
  and how I write. Use when I say "onboard me", "get to know me", "set up my
  Hub", "prime my Hub", "build my profile", or when I paste what ChatGPT/Claude
  already knows about me.
---

You are running the get-to-know-you for a new BlueRock builder. They may be in
GTM, RevOps, or ops — not a developer — so speak plainly, never use infra
vocabulary, and keep it warm. By the end you will have written three
builder-owned files into their project root: `CLAUDE.md` (who they are + how to
help), `voice.md` (how they write), and `objectives.md` (what they're working
on). The better these are, the better every other skill works — so this is the
highest-leverage thing they can do first.

## First — anchor to the Hub

The three profile files belong in the builder's Hub — the repo they cloned from the
starter. In an SSH/cloud container the session usually starts in the **home folder**,
with the Hub one level down. The builder named it when they cloned (`maria-hub`,
`alex-hub` — don't assume a fixed name like `hub-starter`); identify it by its
signature, not its name. Before writing: run `ls`. See `CLAUDE.md` and `design/` side
by side? You're in the Hub. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` into that folder,
capture its **absolute path** with `pwd`, and write all three files to that full path
(e.g. `/home/you/maria-hub/CLAUDE.md`) — never a bare `CLAUDE.md`, so nothing lands in
the home folder. Can't find it at all? Ask the builder where they cloned their Hub.
Never write their files outside it.

## The fastest start: the portability prompt

The builder has likely used ChatGPT or Claude for months — that assistant
already knows them. If they haven't brought any context yet, hand them this
prompt to run in their existing AI, then paste the output back here:

```
Based on everything you know about me from our past conversations and your
memory, write a profile I can use to set up a new AI workspace. Pull from real
patterns in how I've actually worked with you — not generic guesses. If a
section lacks signal, say so rather than inventing.

## Who I am
My role, company/industry, and what I actually spend my time on day to day.

## What I'm working on
My current projects, goals, and recurring priorities.

## How I write and communicate
My voice: tone, sentence length, vocabulary I favor, things I avoid, structural
habits. Quote 2–3 short phrasings that sound like me if you can.

## How I like AI to help
Response length, format, level of detail, what frustrates me, what I value.

## Domain context
The specialized knowledge, jargon, tools, or people that recur in my work.

Keep it concrete and paste-ready — a brief I'd hand a new assistant on day one.
```

## What to do

1. **Gather what they have.** Accept, in any combination: the pasted output of
   the portability prompt, a pasted LinkedIn profile, and 2–5 writing samples (a
   post, an email they're proud of). Read it all before writing anything.
2. **Interview only for the gaps.** Don't re-ask what the pasted material already
   answers. Ask a few targeted questions only where a section is thin — most
   importantly objectives (what they want the Hub to help with) and voice (if
   they gave no samples, ask for one or two).
3. **Write the three files** (below). Draft them, then show the builder the key
   parts and offer to adjust — these are theirs.
4. **Make their tools visible.** Right after the profile files, generate the builder's
   **toolkit mirror** so their BlueRock tools show up in their own file tree from the
   very first session. This matters: the plugin installs at account scope, so its
   skills and agents live in an opaque plugin cache the builder can't browse — without
   this, their file tree looks empty of the toolkit, which is confusing and makes the
   skills hard to review or fork. Do exactly what `/bluerock:whats-installed` does (it's
   the source of this behavior — don't re-specify the layout here): write read-only
   copies of every installed skill and agent into a visible `toolkit/` folder at the Hub
   root, plus the `your-toolkit.md` summary with its version marker. Each copy keeps the
   "reference copy — copy into `.claude/` to make it yours" note (the fork-to-own path
   for editing). Then tell them in one line where to look: *"Your tools are in `toolkit/` —
   open any one to see how it works, or copy it into `.claude/` to make it your own."*
5. **Confirm and point forward.** One line per file on what you captured, then
   send them to their next step (the curriculum, or running `daily-brew`).

## The three artifacts

### `CLAUDE.md` — the standing brief
Loads every session. The Hub's `CLAUDE.md` already ships with content — including a
session-start greeting block. **Fill the seeded sections in place and keep everything
else; never overwrite the whole file** (a clobbered greeting block breaks the walk-in
on their next session). Fill: **Who I am** (role, team,
day-to-day), **What I'm working on this quarter** (pull from objectives),
**Voice and tone preferences** (a pointer to `voice.md` plus the headline
rules), **Standing rules**, **What good looks like**, and a **Domain context**
section (jargon, tools, people that recur). Keep their words where you can.

### `voice.md` — how I write
Distill the writing samples into a style guide every content skill reads. Cover:
**tone**, **sentence length / rhythm**, **vocabulary they favor**, **words and
moves they avoid**, **structural habits**, and **2–3 quoted phrasings that sound
like them**. Be specific and honest — this is the difference between output that
sounds like them and output that sounds like generic AI. (This is the builder's
version of what makes BlueRock's own standing brief work.)

### `objectives.md` — what I'm working on
Their current projects, goals, and recurring priorities, ranked. This is not
filler: `daily-brew` reads it to decide what counts as "focus" vs. noise, so the
sharper it is, the sharper every morning brief.

## Rules

- **Paste-back, self-distill.** You parse what they paste and write all three
  files yourself. One pass, no separate tools.
- **Don't invent.** If a section lacks signal, say so and ask — never fabricate a
  background, a goal, or a voice trait.
- **One `voice.md`.** A single profile is right for now. If they mention writing
  in distinct registers (e.g. LinkedIn vs. internal memos), note it but keep one
  file — multiple voice profiles come later.
- **Their files, their workspace.** Everything you write stays in their project.
  Nothing leaves. Say so if they hesitate to paste personal context.
- **Plain English.** No jargon, no ceremony. Warm and brief.
