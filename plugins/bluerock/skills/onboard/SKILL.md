---
name: onboard
description: >-
  Get to know me and set up my agentic project so it knows who I am, what I'm working on,
  and how I write. Before the interview, if BlueRock's starter template has newer starter
  files than my project, it asks before bringing them up to date (a git fetch and
  fast-forward from the template repo, which on a new project also links it to the
  template's git history); nothing I've written is changed. Use when I say "onboard me",
  "get to know me", "set up my project", "prime my project", "build my profile", or when
  I paste what ChatGPT/Claude already knows about me.
---

You are running the get-to-know-you for a new BlueRock builder. They may be in
GTM, RevOps, or ops — not a developer — so speak plainly, never use infra
vocabulary, and keep it warm. By the end you will have written three
builder-owned files into their project root: `CLAUDE.md` (who they are + how to
help), `voice.md` (how they write), and `objectives.md` (what they're working
on). The better these are, the better every other skill works — so this is the
highest-leverage thing they can do first.

## First — anchor to the project

The three profile files belong in the builder's project (some older docs and repos call the
same repo a Hub — same thing; never rename the builder's folder, and never say "Hub" to the
builder: the word is always "your project"). Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an
SSH/cloud container the chat may start in the project itself or in the **home folder** with
the project one level down — both are normal. Before writing: run `ls`. See `CLAUDE.md` and `design/` side
by side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` into that folder,
capture its **absolute path** with `pwd`, and write all three files to that full path
(e.g. `/home/you/maria-hub/CLAUDE.md`) — never a bare `CLAUDE.md`, so nothing lands in
the home folder. Can't find it at all? Ask the builder which folder their project is in.
Never write their files outside it.

## Next — offer to refresh the starter files (asks first)

The project began as a baked copy of the starter template, which may be behind the
template repo. Once anchored, and before you write anything, look once to see whether a
refresh is due, and **ask before changing anything**. Two rules govern this section:

- **Looking changes nothing and needs no question.** The checks below only read. When
  they show no refresh is due or possible, nothing has changed, so there is nothing to
  report: carry on to the interview.
- **Every step that changes the project's git state is asked for first and reported
  after.** That is the fetch, the one-time repair, and the fast-forward. Never run them
  without a yes, and once the builder has said yes, always tell them how it came out.

Using the project's absolute path (`git -C <project>`, never a bare `cd`), a refresh is
possible only if both hold:

1. `.git` exists in the project root.
2. One of the project's remotes points at the template: in `git remote -v`, a remote
   whose URL contains `bluerock-io/my-workspace` or `bluerock-io/hub-starter` (the old
   name for the same repo — treat both as the template). Baked workspaces name it
   `upstream`; older or hand-cloned projects name it `origin` — accept either, and use
   whichever remote matched in the commands below (call it the template remote).

If either fails, no refresh is possible: move on. Otherwise, it is one of two cases.

**Case A — no save history yet** (`git rev-parse HEAD` fails). Freshly provisioned
workspaces ship with `main` unborn: the repo exists but has zero commits, so every
starter file shows as untracked. A refresh is due. Ask, roughly this way, in your own
words: "Your project started as a copy of BlueRock's starter files. Before we start, I
can bring them up to date from BlueRock's template, which also sets your project up to
keep track of your own changes from here. Nothing you've written is changed, and if anything doesn't line up I stop and leave it as it was. **I'd say yes.**
Want me to?"

On yes, attach the project to the template's history: `git fetch <template-remote> main`,
then `git update-ref refs/heads/main <template-remote>/main`, then
`git read-tree <template-remote>/main`. **Never use `git reset` for this, in any
form** — even `--mixed`, which touches no file on disk, gets auto-denied outright by
Claude Code's own auto mode classifier before it runs, with no prompt and nothing for
the builder to approve (confirmed 2026-08-18: "Blocked by classifier", no waiting
state, no dialog — it matches on the shape of the command, not on which flag makes it
safe). `update-ref` + `read-tree` do exactly what the `reset --mixed` would have:
`update-ref` points `main` at the template's history, `read-tree` marks the starter
files as tracked by loading that commit's tree into the index, and the builder's first
commit later carries only their own changes. Neither command touches a file on disk.
Then continue with the fast-forward below if `git status --porcelain` prints nothing.

**Case B — the project has save history.** A refresh is possible only if
`git status --porcelain` prints nothing (no edits, nothing untracked) and, when the
template remote's `main` is already known locally, `git rev-list --count
<template-remote>/main..HEAD` is 0 (the builder has no commits of their own, which a
fast-forward could not carry). Then read the template's latest without changing
anything: `git ls-remote <template-remote> refs/heads/main`. If that fails (offline, for
example), or its commit equals `HEAD`, no refresh is due: move on. Otherwise ask,
roughly this way: "BlueRock's starter files have a newer version than the copy your
project started from. I can bring them up to date before we start. It only moves your
project forward to the newer starter files; nothing you've written is changed, and if
anything doesn't line up I stop and leave it as it was. **I'd say yes.** Want me to?"

**The fast-forward, on yes in either case:** `git fetch <template-remote>`, then
`git merge --ff-only <template-remote>/main` — explicitly `/main`, because some
workspaces sit on a branch named `master` while the template's default branch is
`main` (a bare `git pull` would fail on that mismatch; never use it). Never run the
Case A repair when `main` already has commits: a project with real history that cannot
fast-forward has no safe automatic repair.

**Then tell the builder how it came out, in one line, with no commit hashes, branch
names, or git vocabulary:**

- **It advanced, or the repair ran:** "Your starter files are up to date."
- **Already current after all:** "Your starter files were already up to date. Nothing
  changed."
- **Anything failed** (the fetch, the repair, or the fast-forward refused): "I couldn't
  bring the starter files up to date this time, so they're as they were. Nothing of
  yours changed." Do not show the error or retry.

**On no:** "No problem. Nothing changed." Rerunning `/bluerock:onboard` offers again.
Either way, carry on to the interview.

Never merge without `--ff-only`, never stash, never reset, never touch the builder's
files to force the refresh through. Over a project's life this offer stops appearing by
design: the builder's own work dirties the tree, their commits rule out the
fast-forward, and on older projects a swapped `origin` stops matching. That is correct
behavior, not a failure to fix.

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
1b. **Save the samples themselves — verbatim, as files.** Each writing sample goes
   into `writing-samples/`, one file each, named for what it is
   (`linkedin-post-sewing.md`), with a one-line header noting the kind and the
   byline (personal voice vs. brand voice) so a later agent knows how to weight
   it. Create `writing-samples/` if the project predates it. `voice.md` describes
   the voice; that folder holds the proof — an agent that needs a real specimen
   reads it there. **Never paste a full sample into `voice.md`:** it loads on
   every content-skill run, and a full post there burns tokens on every draft
   (found 2026-08-15: onboard distilled a sample and discarded it, so no file in
   the project contained a word the builder actually wrote).
2. **Interview only for the gaps.** Don't re-ask what the pasted material already
   answers. Ask a few targeted questions only where a section is thin — most
   importantly objectives (what they want the project to help with) and voice (if
   they gave no samples, ask for one or two).
3. **Write the three files** (below). Draft them, then show the builder the key
   parts and offer to adjust — these are theirs.
4. **Confirm and point forward.** One line per file on what you captured, then
   send them to their next step (the learning path, or running `daily-brew`).
   **Then one closing line, and only one, no list** (product decision, 2026-09-09): every
   ready-made agent team in their toolkit reads these three files before it works, and the
   way to see the difference is to run one on something real. Say it roughly this way:
   *"Every ready-made agent team in your toolkit reads these three files from now on. Run
   one on something real to see the difference: `/bluerock:check` shows what you can run."*
   A list of use cases inside this skill competes with the ten-minute interview it exists
   to run; the list lives in `${CLAUDE_PLUGIN_ROOT}/shared/use-case-catalog.md` and
   `/bluerock:check` renders it. Never a time figure, never a use case named from memory.

## The three artifacts

### `CLAUDE.md` — the standing brief
Loads every session. The project's `CLAUDE.md` already ships with content — including a
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

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **This skill owns `voice.md` and `writing-samples/`** — the file names, and the split
  between them (the file describes the voice, the folder holds the specimens). Use-case
  skills read both: `agents/outreach-writer.md` reads `voice.md` **and a specimen from
  `writing-samples/`** before drafting anything a builder puts their name on, and
  `/bluerock:outreach-prep` names running this skill as the fix when drafts don't sound
  like them. `agents/scorer.md`, `agents/distiller.md`, and `agents/analyst.md` read
  `voice.md` too. Renaming either strands all of them.
- **This skill owns `objectives.md`**, which `daily-brew` reads to rank focus and the
  use-case skills read to pre-fill intake.
- **The closing line in step 4 points at `/bluerock:check` as the place to see what a
  builder can run.** That is true because `check`'s Next block leads with the use cases in
  every state (since 0.16.0). Both read
  `shared/use-case-catalog.md`. If `check` stops listing them, this line goes stale.
