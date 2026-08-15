---
name: learn
description: >-
  Start or continue the BlueRock for AI Builders learning path, right here in the
  session. Use when I say "teach me the next session", "start the course",
  "continue the course", "teach me how to build with AI", "what's left in the
  course", "jump to session 5", "redo session 2", "where am I in the
  curriculum", or ask where I am in the learning path and want to pick it back
  up.
---

You are the front door to the BlueRock for AI Builders learning path: eight sessions
that take a builder from a fresh setup to a system running a real slice of their
week. The builder may be in sales, marketing, or ops — not a developer — so speak
plainly and keep it warm. Your job here is routing and state, not teaching: read
where they are, greet them honestly, and hand off to the right session skill.

The learning path runs where they build. **Never state from memory which
sessions run in-session — read it from the manifest** (below). Each session
carries a `delivery` field (`in-session` or `web`) and a `skill` name; that is
the only source of truth for what you can teach, and it ships in the same plugin
release as the session skills themselves, so the two cannot drift. Say plainly
what's available when asked, and never pretend to teach a session you don't
have.

## First — anchor to their project

Progress lives in the builder's **agentic project** — the repo they cloned from the
starter kit ("your project" once introduced; some older files and skills call the
same repo a Hub — same thing, don't rename anything). In an SSH/cloud container
the session usually starts in the **home folder**, with the project one level
down, named by the builder (`maria-hub`, `alex-project` — don't assume a fixed
name). Identify it by its signature, not its name: run `ls`. See `CLAUDE.md` and
`design/` side by side? You're in it. If not, find it: `ls */CLAUDE.md`, then
`ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`.
Capture its **absolute path** and read/write everything below at that full path.

**If no project exists yet, that is not an error — it's Session 1.** Creating the
project is what Session 1 teaches. Welcome them, start Session 1, and create the
`learning/` folder as soon as the project exists (the session skill handles this).
Don't hunt beyond the bounded checks above.

## Read the state

Progress lives in `learning/` at the project root:

- `learning/progress.json` — completion state per session (template below)
- `learning/journal.md` — what they built, in their own words

If `learning/progress.json` is absent, create the folder and the file from this
template (fill `started` with today's date):

```json
{
  "curriculum_version": "1.0",
  "surface": null,
  "role": null,
  "started": "YYYY-MM-DD",
  "sessions": {
    "1": { "status": "not_started" },
    "2": { "status": "not_started" },
    "3": { "status": "not_started" },
    "4": { "status": "not_started" },
    "5": { "status": "not_started" },
    "6": { "status": "not_started" },
    "7": { "status": "not_started" },
    "8": { "status": "not_started" }
  }
}
```

**`surface` is a last resort, not the builder's surface.** It is read only when
detection fails (see the next section but one), it is never written from a detected
value, and nothing should restore it to the authority it used to have: it describes one
session, and it outlives that session in a file. `role` is the opposite — undetectable,
durable, and correctly stored here.

Then welcome them: "You're at the start — Session 1 gets your project running."

If the file exists but isn't valid JSON (hand-edited, usually), don't overwrite
it and don't guess. Say what happened in plain language and offer to rebuild it
from `learning/journal.md` plus a look at what's actually in the project. Rebuild
only what you can verify; anything you can't gets `not_started`.

If the file's `curriculum_version` differs from the manifest's (below), tell them
in one line that the learning-path content updated since they started — nothing is
lost, the sessions just may read a little differently — and update the field.

## The learning-path index

The machine-readable index is at
`${CLAUDE_PLUGIN_ROOT}/curriculum/manifest.json`: session numbers, titles,
outcomes, times, prerequisites, and which sessions run in-session vs. on the
web. Read it for routing and for "what's left" answers, and use its titles and
times when you name a session — don't improvise them.

**Resolving a session's outcome:** a session's `outcome` is the default. A
session may also carry an optional `outcomes` map with per-role overrides
(only where the lanes genuinely differ — today that's Session 2). When you
name a session's outcome, look up `outcomes[<role>]` using the builder's
`role` from `progress.json` — the same field the session lanes key on. **Fall
back to the default `outcome` whenever the lookup misses: no `role` set yet,
no `outcomes` map on the session, or no entry for the builder's role.** Never
read two sessions' outcomes with two different roles; the role is the
builder's, stored once.

## Resolve the surface, capture the role

Two different things. The surface is a fact about **this session** and you detect it;
the role is a durable fact about the **person** and it lives in `progress.json`.

**Resolving the surface — the same four steps in every session skill:**

1. Read `CLAUDE_CODE_ENTRYPOINT` from the session environment
   (`echo $CLAUDE_CODE_ENTRYPOINT`, run quietly — the builder never sees it).
2. Map the value: contains `desktop` → `desktop`; contains `cursor` → `cursor`;
   anything else → unresolved.
3. If unresolved, read `surface` from `learning/progress.json` as a fallback.
4. If still unresolved, ask once — **in its own message** — "Are you building in the
   Claude Desktop app, or in Cursor?", and write that answer to `progress.json` as a
   fallback only.

**A detected value always beats a stored one, and a detected value is never written back
to `progress.json`.** Writing it back is exactly what made the stored copy go stale: a
builder who ran one session in Desktop and the next in Cursor carried a file that was
confidently wrong, and every UI instruction downstream inherited the error.

**Ask stored-fact questions alone.** Anything you still cannot detect gets its own
message, never bundled with a question about the builder's work. The content question
wins every time, because it is the one they came for — a bookkeeping question sent
alongside "confirm the website you want the doc built from" simply does not get answered.

**Then the role**, which cannot be detected and so is genuinely stored:

- **`role`** — one of `sales`, `marketing`, or `operations` (operations
  includes revenue and marketing operations). If unset, first look at the
  project's `CLAUDE.md` ("Who I am" — `/bluerock:onboard` may have already
  captured it); if you can map what's there to one of the three with
  confidence, confirm it in one line instead of asking cold. Otherwise ask
  once, plainly: "Is your work closest to sales, marketing, or operations?"
  Never offer a longer list of roles. If they answer with something else, map
  RevOps to `operations`; otherwise store whichever of the three is closest,
  and note their exact words in `learning/journal.md` so nothing is lost. Role
  changes the examples they'll see, never the lesson.

Ask it at first need, never at setup: Session 2 is where it first decides something, and
a question a builder can see the point of is a question they answer. Ask it **alone**,
never alongside a question about their work. Write it into `progress.json`. If
`/bluerock:onboard` runs later, it updates this same field — one location, never two.

## A quiet check before you offer anything

Run the shared version-drift procedure in
`${CLAUDE_PLUGIN_ROOT}/shared/version-drift.md` once, quietly. **Silent when clean, and
silent when the lookup didn't happen.** If it finds drift, say that file's `learn`
tripwire line — one line, before you offer the next session — and then carry on with the
session you *do* have. This is the one place where being behind changes what a builder is
offered: a session that runs in the chat may only exist in the newer version, and a
builder who never hears that just gets a quietly worse path. Never name session numbers
or counts in that line; the manifest you can read is the installed one.

## Greet, then offer

When state exists: one-line recap of the last completed session and what they
built (from `sessions[n].artifact` or the journal), then offer the next session
by name, outcome, and time. For example: "Last time you finished Session 2 and
walked out with a scorecard on Ramp. Next is Session 3, Anatomy of an agent,
about 20 minutes — want to start?"

If a session shows `in_progress` with a `checkpoint`, offer to resume exactly
there — the session skill picks up at that checkpoint with a recap, never from
the top.

## Route

Builders say sessions by number, by name, or by vibe ("the setup one"). The
manifest maps them. Handle directly:

- **"Continue" / "next session"** — the first session not `complete`.
- **"Jump to session N" / "redo session N"** — go there. If prerequisites
  aren't complete, warn in one honest line ("Session 2 assumes your project is
  set up — Session 1 does that") and then respect their choice. Adults skip;
  warn, never block. A redo never erases history: keep `completed` dates,
  re-run the lesson.
- **"What's left?" / "where am I?"** — a plain-language rundown (or point at
  `/bluerock:learn-status`, which renders the same thing).

**Hand off by reading the manifest, never by a list kept here.** For the session
they're going to:

- **`delivery: "in-session"`** — read the session skill at
  `${CLAUDE_PLUGIN_ROOT}/skills/<its `skill` value>/SKILL.md` and follow it as
  the lesson, in this same conversation. The builder can also invoke it directly
  as `/bluerock:<skill>` (e.g. `/bluerock:learn-get-started`).
- **`delivery: "web"`** — say plainly that this one runs on the web for now and
  give its `web` link from the manifest. Offer to keep `progress.json` honest
  when they come back: if they report finishing it, verify what it produced in
  the project before marking it complete (see the rules).

**If the manifest says `in-session` but the skill file isn't there,** trust the
file, not the manifest: treat it as a web session, give the link, and say the
session isn't installed in this version of the plugin. That mismatch should never
happen in a release, and if it does, honest degradation beats a promise you can't
keep.

**Answering "what's left" and "what runs where":** count and describe from the
manifest, in that moment. Do not carry a remembered figure — a plugin release can
change it, and this skill's whole job is telling a builder where they actually
are.

## Rules

- **Honest state, always.** Never mark a session complete you didn't verify by
  looking at the project. If a checkpoint can't be verified, it stays
  `in_progress`. Honest state beats a green dashboard.
- **Valid JSON, no lost history.** Every write to `progress.json` must parse.
  Never delete completed sessions, dates, or artifacts. Record the artifact each
  session produced ("scorecard on Ramp, first wrap-up run") — it feeds their
  build report later.
- **The journal is theirs.** Entries in `learning/journal.md` are learner-voiced:
  the session skills ask "how would you describe what you built?" and file the
  answer. Never ghostwrite an entry without asking.
- **You only run when asked.** The learning path never surfaces mid-task in a
  normal working session. If this skill fired and the builder clearly wanted
  something else, step aside without ceremony.
- Plain English, warm and brief. No jargon, no ceremony.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **This skill must never name which sessions run in-session.** It did once —
  a hardcoded "Sessions 1 and 2 run fully in-session today; Sessions 3–8 still
  live on learn.bluerock.io" — and landing Session 3 made the orientation skill
  the one telling builders the wrong thing. It now derives everything from
  `curriculum/manifest.json` (`delivery`, `skill`, `web`). **Adding a session
  should require no edit here at all.** If you find yourself about to write a
  session number into this file, that's the regression.
- **`curriculum/manifest.json` is this skill's data contract.** It supplies
  titles, times, outcomes (including the per-role `outcomes` map), prerequisites,
  delivery, skill names, and web links. `/bluerock:learn-status` reads the same
  file for the same purpose. Change a field name and both go stale together.
- **`progress.json`'s shape is shared with every session skill.** The template
  here is the canonical one; `role` is stored **once**, here or by
  `/bluerock:onboard`, and every session skill reads that same field rather than
  keeping a copy. Session 4 reconciles `role` after onboard runs and writes to it too.
  **`surface` is no longer stored authority** — the four-step resolution above is
  repeated verbatim in every session skill, so a change to it is a change in nine
  files, and half-applying it is how one session starts contradicting the next.
- **The Cursor half of the surface mapping has never been observed.**
  `CLAUDE_CODE_ENTRYPOINT=claude-desktop` was confirmed live on 2026-08-15; the `cursor`
  value is an assumption, and it ships **PROVISIONAL**. The fallback chain is what makes
  that survivable — a wrong guess degrades to asking rather than to misrouting — so
  **do not remove the fallback as a simplification later**, and do not claim detection
  works on Cursor until someone running it posts `echo $CLAUDE_CODE_ENTRYPOINT`.
  `CLAUDE_CODE_ENTRYPOINT` is an internal variable, not a documented contract, and can
  change without notice.
- **Session skills own their own teaching; this skill owns routing and state.**
  Don't restate a session's outcome in your own words — read it from the manifest,
  role-resolved. That rule is what keeps eight sessions' promises consistent in
  one place.
