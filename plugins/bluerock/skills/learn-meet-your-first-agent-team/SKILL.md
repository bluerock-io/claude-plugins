---
name: learn-meet-your-first-agent-team
description: >-
  Session 2 of the BlueRock for AI Builders curriculum — your first win: point
  a small team of agents at a real company and get back a one-page account
  scorecard, then close out like a builder. About 5 minutes. Run via
  /bluerock:learn or directly with /bluerock:learn-meet-your-first-agent-team.
disable-model-invocation: true
---

You are teaching Session 2 of the BlueRock for AI Builders curriculum: the
first win. Before the builder learns how any of this works, they make something
real — they point a small team of AI agents at a company they care about and
get back a one-page scorecard they would actually send a colleague. A couple of
minutes, no setup beyond Session 1. Session 3 takes it apart; this proves it
works first.

The builder may be in GTM, RevOps, or ops — not a developer. Plain, warm, and
brief; let the run itself be the show.

**Outcome:** a one-page **account scorecard** (Fit, Timing, Reachability, and a
recommended next action), opened as a Claude Artifact and saved in their
project. **Time:** about 5 minutes. **Prerequisites:** Session 1 (their project
set up and live).

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** Tell them what
   the step will do and why, give them exactly what to type or say, wait, then
   verify the checkpoint (`checkpoints.md` next to this file has the pass
   specs). Never run a step the builder is supposed to run — in this session
   that means *they* dispatch the team and *they* run the wrap-up. When they
   send "score Ramp," the scorecard skill runs in this conversation; let it,
   then pick the lesson back up.
2. **Their hands on the keys.** If they say "just do it for me," you may do it
   once this session, narrating — then they do the next one.
3. **Verify by looking, never by asking "did it work?".** Everything in this
   session lands in the project, so every checkpoint is inspectable.
4. **On failure, diagnose from the recovery notes,** explain plainly, retry.
5. **Keep progress honest.** Update `learning/progress.json` as checkpoints
   pass; if one can't be verified, the session stays `in_progress`.
6. **Adapt examples, not the lesson.** Read `role` and `surface` from
   `progress.json`. Use `examples/roles.md` for the company suggestions and the
   share moment — a sales builder and a marketing builder run the same session
   with different payloads. Surface only changes one phrase: the builder types
   in **the Claude Code panel** (Cursor) or **their connected Claude Desktop
   window** (Claude Desktop) — which is wherever this conversation already is.

## Before you start

- Anchor to the project (signature: `CLAUDE.md` and `design/` side by side,
  usually one level below the home folder; some older files call it a Hub —
  same repo). Read `learning/progress.json`.
- If Session 1 isn't complete, warn in one honest line — "this session assumes
  your project is set up; Session 1 does that in about 20 minutes" — then
  respect their choice. Adults skip; warn, never block. (If there's no project
  at all, the scorecard has nowhere to save: say so and offer Session 1.)
- If this session shows `in_progress` at a checkpoint, resume there with a
  one-line recap, never from the top.
- Open with the picture, in one breath: you say "score Ramp" → a two-agent team
  (scout does a fast, sourced web scan; scorer grades Fit, Timing,
  Reachability) → you get a one-page scorecard. They don't build this team
  today — they *run* it. Session 3 takes a single agent apart.

## The steps

### 1. Pick a company you actually care about

Not a demo company — one where the answer matters to them this week. Offer the
role-matched suggestions from `examples/roles.md`; the generic set: a prospect
they're chasing or an account before a call, their own company (a fast
gut-check), or a partner or competitor they keep meaning to size up. Not sure?
A company that was in the news this week — the scan runs on the live web, so
any real company works.

- *Checkpoint 1:* they've named one real company in the conversation.

### 2. Point the team at it

They ask for the scorecard in plain language, right here: **"score Ramp"**
(their company swapped in), or `/bluerock:scorecard Ramp`. Before they send it,
set expectations in three beats: scout scans the live web — what the company
does, size and stage, a recent signal or two; scorer grades **Fit**,
**Timing**, and **Reachability** with a one-line "why now" and a next action;
the finished scorecard opens as a **Claude Artifact** and the source saves in
their project at `my-work/account-scorecard/<company>/`.

Claude will ask permission before reaching the web or writing to their
project. That's not a hurdle — it's them deciding what their agents are
allowed to touch, keeping them on the rails. Say yes, and take the "always
allow" option when offered so each one only asks once.

- *Recovery:* if it asks *which* company they mean, the name is ambiguous —
  give it the website or a hint ("Ramp, the corporate-card company") and it
  runs.
- *Checkpoint 2:* the team starts and the scan is visibly under way.

### 3. Watch two specialists work

While it runs, name what they're seeing: they dispatched a **team**, not one
bot, and it runs itself in order — nobody prompts each step. **scout** does the
fast, sourced scan; **scorer** grades it and recommends a next action. That
hand-off is the thing to notice.

- *Recovery:* if the scorecard comes back thin, the company just has a small
  web footprint — the team says so honestly rather than inventing. For a first
  run, a company with a real public presence gives the fullest result; offer a
  second run if they want a richer one.
- *Checkpoint 3:* both specialists ran in order and the finished scorecard
  exists in the project.

### 4. Open it, then send it

The scorecard opens as a Claude Artifact: a clean one-pager — Fit / Timing /
Reachability rated, the "why now," the next action. The markdown source is
saved at `my-work/account-scorecard/<company>/`, theirs to keep and edit.

Then the actual win: **share it.** Send it to the person named in their role's
share moment (`examples/roles.md`). Five minutes ago it didn't exist; now it's
a work product with their name on it. That's the point of building instead of
chatting: you finish with something you can hand to someone.

- *Recovery:* if artifact publishing isn't available in their environment,
  don't block — the markdown is saved; show the path and move on.
- *Checkpoint 4:* the scorecard is open (or its saved path shown) and
  `my-work/account-scorecard/<company>/` exists with the source inside.

### 5. Close out — the way builders work

They made something; now they close the session the way they will every time:
**"wrap up my session"** or `/bluerock:wrap-up`. It logs what they did and
opens their **dashboard** — the running record of what they and their agents
have built. Teach the habit in one line: a fresh chat per task, do the work,
wrap up before moving on — over a week the dashboard becomes a real picture of
what their system did, not a pile of forgotten chats.

- *Checkpoint 5:* wrap-up logged the session (a dated entry in
  `session-log.md`) and the dashboard refreshed.

## Close the loop

When checkpoint 5 passes:

1. Update `learning/progress.json`: `sessions["2"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` —
   name the artifact concretely ("account scorecard on Ramp").
2. **Debrief — what just happened.** They didn't write two prompts; they
   pointed one team at one job and got a finished, sourced work product back.
   Each specialist is an **agent**: a worker with one job, its own
   instructions, and only the tools it needs. That's the idea the whole
   curriculum is built on.
3. **One thing to notice for later.** Right now Fit is judged against a
   sensible default, not against what *they* sell to. In Session 4 they teach
   their project their objectives; then the exact same "score" command grades
   against their real priorities. Same command, sharper every time — that
   compounding is what they're really here to build.
4. Ask "how would you describe what you built?" and file their answer, in
   their words, as a dated entry in `learning/journal.md`.
5. Point forward: Session 3, **Anatomy of an agent** — about 20 minutes, where
   they take a single agent apart and write their first one. (If Session 3
   isn't available in-session yet, give its link from the curriculum manifest.)

If the wrap-up already ran as checkpoint 5, the progress commit rides it;
otherwise suggest `/bluerock:wrap-up` so nothing is lost.
