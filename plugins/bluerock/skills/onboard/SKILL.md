---
name: onboard
description: >-
  Get to know me and set up my agentic project so it knows who I am, what I'm working on,
  and how I write. Use when I say "onboard me", "get to know me", "set up my
  project", "prime my project", "build my profile", or when I paste what ChatGPT/Claude
  already knows about me.
---

You are running the get-to-know-you for a new BlueRock builder. They may be in
GTM, RevOps, or ops — not a developer — so speak plainly, never use infra
vocabulary, and keep it warm. By the end you will have written three
builder-owned files into their project root: `CLAUDE.md` (who they are + how to
help), `voice.md` (how they write), and `objectives.md` (what they're working
on). The better these are, the better every other skill works — so this is the
highest-leverage thing they can do first.

## First — anchor to the project

The three profile files belong in the builder's project — the repo they cloned from the
starter kit (some older docs and repos call the same repo a Hub — same thing; never rename
the builder's folder, and never say "Hub" to the builder: the word is always "your project"). In an SSH/cloud container the session usually starts in the **home folder**,
with the project one level down. The builder named it when they cloned (`maria-hub`,
`alex-hub` — don't assume a fixed name like `my-workspace`); identify it by its
signature, not its name. Before writing: run `ls`. See `CLAUDE.md` and `design/` side
by side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` into that folder,
capture its **absolute path** with `pwd`, and write all three files to that full path
(e.g. `/home/you/maria-hub/CLAUDE.md`) — never a bare `CLAUDE.md`, so nothing lands in
the home folder. Can't find it at all? Ask the builder where they cloned their project.
Never write their files outside it.

## Next — refresh the starter files (silent preflight)

The project began as a baked copy of the starter template, which may be behind the
template repo. Once anchored, and before you write anything, attempt one refresh.
The rule that governs everything here: **failure of any kind means skip silently** —
no git output, no error message, no question. Continue onboarding exactly as if this
section didn't exist. Worst case the builder keeps the baked copy, which is what they
had anyway.

Using the project's absolute path (`git -C <project>`, never a bare `cd`), proceed
only if ALL three hold:

1. `.git` exists in the project root.
2. One of the project's remotes points at the template: in `git remote -v`, a remote
   whose URL contains `bluerock-io/my-workspace` or `bluerock-io/hub-starter` (the old
   name for the same repo — treat both as the template). Baked workspaces name it
   `upstream`; older or hand-cloned projects name it `origin` — accept either, and use
   whichever remote matched in the commands below (call it the template remote).
3. `git status --porcelain` prints nothing (no edits, nothing untracked).

**Between checks 2 and 3, one one-time repair.** Freshly provisioned workspaces ship
with `main` unborn — the repo exists but has zero commits, so every starter file shows
as untracked and check 3 would fail forever. If checks 1 and 2 pass but
`git rev-parse HEAD` fails (no commits yet), attach the project to the template's
history first: `git fetch <template-remote> main`, then
`git reset --mixed <template-remote>/main`. This changes no file on disk — it only
points `main` at the template's history and marks the starter files as tracked, so
check 3 can pass and the builder's first commit later carries only their own changes.
Say nothing about it. If either command fails, skip it silently like everything else
here. Never run it when `main` already has commits: a project with real history that
cannot fast-forward has no safe automatic repair.

If all three pass: `git fetch <template-remote>`, then
`git merge --ff-only <template-remote>/main` — explicitly `/main`, because some
workspaces sit on a branch named `master` while the template's default branch is
`main` (a bare `git pull` would fail on that mismatch; never use it).

Afterwards, exactly one of three outcomes:

- **It advanced:** tell the builder one friendly line at most — "I refreshed your
  starter files to the latest" — no commit hashes, no branch names, no git vocabulary.
- **Already current:** say nothing.
- **Anything else** (a check failed, the fetch failed — e.g. offline — or the merge
  refused because of local commits): say nothing, change nothing, move on.

Never merge without `--ff-only`, never stash, never reset, never touch the builder's
files to force the refresh through. This preflight goes quiet over a project's life
by design — the builder's own work dirties the tree, their commits break the
fast-forward, and on older projects a swapped `origin` stops matching. That is
correct behavior, not a failure to fix.

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
