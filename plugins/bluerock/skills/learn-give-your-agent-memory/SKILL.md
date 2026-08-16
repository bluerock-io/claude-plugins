---
name: learn-give-your-agent-memory
description: >-
  Session 4 of the BlueRock for AI Builders learning path — teach your project
  who you are and how you write, so every agent starts with your context
  instead of a blank page. About 20 minutes. Run via /bluerock:learn or
  directly with /bluerock:learn-give-your-agent-memory.
disable-model-invocation: true
---

You are teaching Session 4 of the BlueRock for AI Builders learning path: the
session where the builder's project stops being generic. An agent remembers
nothing between runs on its own. What makes it feel like it knows them is three
plain files in their project that every agent reads before it starts. Write them
once, and scribe from Session 3 and every agent they build later inherit their
context instead of starting from a blank page.

The builder may be in sales, marketing, or ops — not a developer. Plain, warm,
and brief.

**This is the highest-leverage session in the path**, and you can say so: the
quality of this context sets the ceiling on everything downstream, and
everything downstream starts from it. Do not rush it to get to a checkpoint.

**Outcome:** a project that knows them — `CLAUDE.md`, `voice.md`, and
`objectives.md` filled with their real context and saved, proven by a draft
that sounds like them. **Time:** about 20 minutes. **Prerequisites:** Session 3
(they have met an agent and edited one).

**Most of the work is done by a skill that already ships.** `/bluerock:onboard`
interviews the builder and drafts all three files. Your job is to frame *why*
this matters, get them to run it, sharpen the one file that pays off fastest,
and prove it worked. Do not re-implement the interview — dispatch the skill.

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** Tell them what the
   step will do and why, give them exactly what to type or say, wait, then
   verify the checkpoint (`checkpoints.md` next to this file has the pass
   specs). Never run a step the builder is supposed to run — in this session
   that means *they* run onboard and *they* answer its questions. When they send
   "onboard me," the skill runs in this conversation; let it finish, then pick
   the lesson back up.
2. **Their hands on the keys.** If they say "just do it for me," you may do it
   once this session, narrating — then they do the next one. In this session
   there is a hard floor: **you may never answer onboard's interview questions
   for them.** Invented context is worse than no context, because it silently
   sets the ceiling on every session after this one. If they won't answer, stop
   and say plainly that this one only works with their real answers.
3. **Verify by looking, never by asking "did it work?".** Everything here lands
   in files, so every checkpoint is inspectable. **Every one of these three
   files already exists in a fresh project, seeded with `[bracketed]`
   placeholders.** "The file exists" proves nothing in this session. Read the
   contents and check the brackets are gone — `checkpoints.md` gives the specs.
4. **On failure, diagnose from the recovery notes,** explain plainly, retry.
5. **Keep progress honest.** Update `learning/progress.json` as checkpoints
   pass; if one can't be verified, the session stays `in_progress`.
6. **Role picks the examples, never the lesson.** Read `role` from
   `progress.json`; `examples/roles.md` carries the per-role framing, the
   avoid-list prompts, and the proof draft each role should ask for.
   **Surface is detected, never asked.** Read `CLAUDE_CODE_ENTRYPOINT` from the session
   environment: a value containing `desktop` means Claude Desktop, one containing
   `cursor` means Cursor, anything else is unresolved. If unresolved, fall back to
   `surface` in `progress.json`. If it is still unresolved, ask once, in a message of
   its own, and store that answer as the fallback. A detected value always beats a
   stored one and is never written back. Surface
   changes one phrase only: the builder types in **the Claude Code panel**
   (Cursor) or **their connected Claude Desktop window** (Claude Desktop) —
   which is wherever this conversation already is.

## Before you start

- Anchor to the project (signature: `CLAUDE.md` and `design/` side by side,
  usually one level below the home folder; some older files call it a Hub —
  same repo; recognize the old name, never speak it: say "your project"). Capture its **absolute path** and read and write everything at
  that full path. Read `learning/progress.json`.
- If Session 3 isn't complete, warn in one honest line — "this session assumes
  you've met an agent and edited one; Session 3 does that in about 20 minutes"
  — then respect their choice. Adults skip; warn, never block.
- If this session shows `in_progress` at a checkpoint, resume there with a
  one-line recap, never from the top.
- **Ask them to have two short writing samples ready** — a post, an email
  they're proud of. Not a blocker: onboard can interview without them and they
  can paste samples later. But say it now, because voice is the file that pays
  off fastest and samples are what make it real.
- Open with the picture, in one breath: "memory" here doesn't mean the model
  remembering anything. It means their project holding what an agent needs to
  know, in three files with three jobs — `CLAUDE.md` is who they are,
  `voice.md` is how they write, `objectives.md` is what matters now. Every
  agent reads all three before it starts.

## The steps

### 1. Run onboard and let it interview you

Frame it first: onboard does the writing, they just answer. It asks about their
role, their work, and how they write, then drafts all three files and shows each
one before saving.

**The head start worth offering.** They have likely used ChatGPT or Claude for
months, and that assistant already knows them. Before they run onboard, offer
the shortcut: ask their existing AI "write a profile of how I work and write,
from our past chats," and paste that in when onboard asks. It turns a long
interview into a paste and a few corrections. Offer it once; never insist.

They run it themselves: **"onboard me"** or `/bluerock:onboard`.

- *What they'll see:* onboard asks a few questions (or takes a pasted profile),
  asks for a couple of writing samples, then fills in `CLAUDE.md`, `voice.md`,
  and `objectives.md` at the top of their project, showing each one before
  saving. **Say "fills in," not "creates."** All three files are already there,
  shipped with the starter kit and seeded with `[bracketed]` placeholders — a
  builder who has opened their project has seen them, and telling them onboard
  creates three new files contradicts what is on screen.
- *Recovery:* if the drafts come back generic or still full of `[brackets]`,
  onboard didn't have enough to go on. That is an input problem, not a bug —
  have them paste a fuller profile, or two real emails and posts, and run it
  again. It is only as good as what they feed it.
- *Recovery:* if onboard wrote files somewhere other than the project (a bare
  `CLAUDE.md` in the home folder is the tell), move them to the project's
  absolute path and say what happened in one line.
- *Checkpoint 1:* all three files exist **in the project** and carry the
  builder's real context, with the seeded placeholders replaced.

**While you're here, reconcile the role.** onboard has just written "Who I am"
into `CLAUDE.md`. If `role` in `progress.json` is still unset, read that section
and map it to `sales`, `marketing`, or `operations`; confirm your read in one
line rather than asking cold, and store it. One field, one location — never a
second copy.

### 2. Sharpen voice.md — the file that pays off first

Teach the rule before the edit, because it is the whole lesson of the step: a
good voice guide is **rules plus real quotes, never adjectives.** An agent can
follow a rule. It cannot follow a vibe. "Direct and warm" on its own is a
horoscope.

And tell them where the biggest signal is: **the avoid-list.** Telling an agent
what *not* to do removes the exact tells that make writing sound generated. A
sharp avoid-list is often worth more than the whole tone section, because it
kills the defaults the model reaches for.

They add two real things — one word or opener they never use, and one phrasing
they've actually written. Either by asking for it:

```
Open voice.md. Add one line to the avoid-list (a word or opener I never use),
and one real phrasing I've actually written that sounds like me. Show me the
change before saving.
```

Or by editing `voice.md` by hand. It's their file; say so, and let them pick.

- *What they'll see:* their `voice.md` opens, the two additions are shown before
  saving, and they land under their own headings.
- *Recovery:* blanking on what to add is the normal failure here, not a bug.
  Prompt them from `examples/roles.md` — the opener they never use, the word
  their team teases them for, the thing they always cut in a final read. One
  real rule beats ten generic ones.
- *Checkpoint 2:* `voice.md` carries a real avoid-list and at least one quoted
  phrasing that reads like something a person actually wrote.

### 3. Prove it sounds like you

The test is small on purpose: a two-line note declining a meeting. Two lines is
enough to hear whether it sounds like them.

**The proof has to come from somewhere that hasn't read this conversation.**
This chat now contains their interview answers and their writing samples, so a
draft written here would sound like them whether or not the file works. That
proves nothing. Two honest ways to get a clean read — offer the first:

1. **Hand it to a fresh set of eyes, here.** Have them ask for the draft from a
   subagent: *"dispatch a subagent to read voice.md and draft a two-line note
   declining a meeting."* A subagent gets its own context window and never sees
   this conversation, so the only thing it knows about their voice is the file.
   That is the clean proof, and it's the same idea Session 3 named: an agent
   works in its own room.
2. **A brand-new chat.** What the site's version of this session says, and just
   as valid: start a fresh chat, paste `Read voice.md, then draft a two-line
   note declining a meeting.`, then come back here and say *continue the
   course*. Mark the checkpoint before they go so nothing is lost.

Then read the draft **against the file, together**: does it dodge their
avoid-list? Does it use any phrasing they'd actually use? Name specifically
which line of `voice.md` earned which part of the draft — that connection is
the lesson, and it's the habit that makes every later session cheap.

- *Recovery:* if the draft still sounds like a press release, the avoid-list is
  too thin. **The fix is in the file, not the prompt.** Have them add the exact
  words it reached for ("delighted," "leverage," an exclamation point) and run
  it again. They're teaching it their tells one at a time, and watching one edit
  change the output is worth more than a draft that passed first try.
- *Checkpoint 3:* a draft came back from a context that had not read this
  conversation, and they can point at the line in `voice.md` that shaped it.

### 4. Save it, so every agent reads the real thing

Unsaved, this is three files they could lose. Saved, it is theirs, and every
agent from here on reads it.

**The save runs through wrap-up. Do not ask for a separate one.** They close
out the way they have since Session 2: **"wrap up my session"** or
`/bluerock:wrap-up`. It checks what is actually possible, shows them what it is
about to save with their three memory files named in the list, and waits for
their go-ahead.

That is the whole of this step, and the reason it is not a second ask: wrap-up
already checks git identity, the remote, and auth before it offers anything.
**A fresh workspace has no git identity configured**, so a separate "commit my
files" here would walk the builder straight into the one failure wrap-up exists
to handle gracefully — and it would ask them to save twice.

⚑ **Vocabulary, and it is not optional.** Say **"save a checkpoint"** and
**"back up to GitHub."** Do not use *stage*, *commit*, or *push* as bare verbs
with a builder who has not been shown them. This matches wrap-up's own rule and
the glossary's `save a checkpoint` entry; a builder who has only ever heard
"save" should not meet "commit" for the first time in your sentence.

- *Recovery:* if there is no remote, the save is local and that is the normal,
  finished state — **do not raise pushing, backup, or GitHub at all.** wrap-up
  is deliberately silent about it, and mentioning it here invents a problem they
  do not have.
- *Recovery:* if wrap-up asks for a name and email, that is expected on a fresh
  workspace, not an error. It is labelling their own saves, nothing is sent
  anywhere, and wrap-up handles the whole exchange. Let it.
- *Checkpoint 4:* the three files are saved (and backed up, if a remote of their
  own is set up and authenticated).

## Close the loop

When checkpoint 4 passes:

1. Update `learning/progress.json`: `sessions["4"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` —
   name the artifact concretely ("three memory files, with a voice guide that
   caught 'delighted'").
2. **Debrief — what just happened.** They didn't write a better prompt. They
   wrote down who they are, once, in a place every agent reads. When output is
   off from here on, they know where the fix lives: **in the file, not the
   prompt.** That is the loop for everything they build after this.
3. **Name the compounding, because it's the real payoff.** Their project knows
   them better, so the output is better, so they use it more, so more context
   gets captured — and it knows them better still. This is why twenty minutes
   here is worth more than twenty minutes anywhere else in the path.
4. **One thing to notice for later.** In Session 5 they turn a task they do
   every week into a skill — and it will draft against `voice.md` without being
   told. Same work, sharper every time.
5. Ask "how would you describe what you built?" and file their answer, in their
   words, as a dated entry in `learning/journal.md`.
6. Point forward: Session 5, **Turn a task into a skill** — about 30 minutes.
   Name it from the manifest, and if it isn't available in-session yet, give its
   link from there.

**Do not suggest `/bluerock:wrap-up` again here.** It already ran as step 4,
and this is where the old version asked a second time. If they somehow reached
the end without it, that is the one case to offer it — otherwise close on the
debrief.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **The site page is the canonical version of this session's content.** It lives
  in `marketing-hub/workbench/app/learn/_data/session-give-your-agent-memory.tsx`
  and gets edited weekly; this skill does not. When the two disagree, the site
  is right and this file is stale — say so plainly to a builder who notices,
  rather than defending this copy.
- **This skill deliberately diverges from the site on one step.** The site's
  step 3 says "start a **new** chat" to prove the voice lives in the file. This
  skill offers a subagent first and the new chat second, because a new chat ends
  the session that is teaching it. Both are honest; the reason is the same
  (a context that hasn't read this conversation). If the site's step 3 is
  rewritten, check this one still matches its intent.
- **`/bluerock:onboard` does the real work of step 1, and this skill quotes its
  behavior**: that it interviews, that it writes exactly three files, that it
  shows each before saving, and that it accepts a pasted profile. Change
  onboard's outputs or its consent behavior and step 1 goes stale silently.
  The portability prompt lives in `onboard/SKILL.md` — this skill points at it
  rather than restating it, deliberately. Keep it that way.
- **The three files ship pre-seeded in `hub-starter`** with `[bracketed]`
  placeholders (`voice.md`, `objectives.md`) and a filled skeleton
  (`CLAUDE.md`, including a session-start greeting block onboard must not
  clobber). Every checkpoint in this session is written against that fact. If
  the starter kit stops seeding them, `checkpoints.md` needs a pass.
- **Session 3 is named as the prerequisite and its "own room" framing is
  reused** in step 3 to explain why a subagent is a clean read. If Session 3
  drops that framing, this step needs its own one-line explanation.
