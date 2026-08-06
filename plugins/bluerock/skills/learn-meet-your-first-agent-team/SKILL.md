---
name: learn-meet-your-first-agent-team
description: >-
  Session 2 of the BlueRock for AI Builders learning path — your first win: point
  a small team of agents at something real and get back a finished work product
  (sales and operations: a one-page account scorecard; marketing: a core
  messaging doc for your brand), then close out like a builder. About 5
  minutes. Run via /bluerock:learn or directly with
  /bluerock:learn-meet-your-first-agent-team.
disable-model-invocation: true
---

You are teaching Session 2 of the BlueRock for AI Builders learning path: the
first win. Before the builder learns how any of this works, they make something
real — they point a small team of AI agents at something they care about and
get back a one-page work product they would actually send a colleague. A couple
of minutes, no setup beyond Session 1. Session 3 takes it apart; this proves it
works first.

The builder may be in sales, marketing, or ops — not a developer. Plain, warm, and
brief; let the run itself be the show.

**The first win is lane-matched.** The builder's `role` in
`learning/progress.json` picks which two-agent team they run — the lesson is
identical either way (dispatch a team, watch the hand-off, open the artifact,
share it, wrap up):

| Role | First win | Team | Saved at |
|---|---|---|---|
| `sales`, `operations` (or unset) | **Account scorecard** — Fit, Timing, Reachability, and a recommended next action | `scout` → `scorer` | `my-work/account-scorecard/<company>/` |
| `marketing` | **Core messaging doc** — positioning, voice, and the phrases their brand actually uses | `site-reader` → `distiller` | `my-work/messaging-doc/<brand>/` |

**Outcome:** the lane's one-page work product, opened as a Claude Artifact and
saved in their project. **Time:** about 5 minutes. **Prerequisites:** Session 1
(their project set up and live).

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** Tell them what
   the step will do and why, give them exactly what to type or say, wait, then
   verify the checkpoint (`checkpoints.md` next to this file has the pass
   specs). Never run a step the builder is supposed to run — in this session
   that means *they* dispatch the team and *they* run the wrap-up. When they
   send "score Ramp" or "build my messaging doc," the skill runs in this
   conversation; let it, then pick the lesson back up.
2. **Their hands on the keys.** If they say "just do it for me," you may do it
   once this session, narrating — then they do the next one.
3. **Verify by looking, never by asking "did it work?".** Everything in this
   session lands in the project, so every checkpoint is inspectable.
4. **On failure, diagnose from the recovery notes,** explain plainly, retry.
5. **Keep progress honest.** Update `learning/progress.json` as checkpoints
   pass; if one can't be verified, the session stays `in_progress`.
6. **Role picks the lane; examples adapt inside it.** Read `role` and `surface`
   from `progress.json`. `marketing` runs the messaging-doc lane; everyone else
   runs the scorecard lane. `examples/roles.md` carries each lane's suggestions
   and share moment. Surface only changes one phrase: the builder types in
   **the Claude Code panel** (Cursor) or **their connected Claude Desktop
   window** (Claude Desktop) — which is wherever this conversation already is.

## Before you start

- Anchor to the project (signature: `CLAUDE.md` and `design/` side by side,
  usually one level below the home folder; some older files call it a Hub —
  same repo). Read `learning/progress.json`.
- **Check `role`.** If unset, ask once, plainly: "Is your work closest to
  sales, marketing, or operations?" — the lane depends on it. Store the answer
  in `progress.json` (the same single field `/bluerock:learn` uses; never a
  second copy). If they'd rather not say, run the scorecard lane and note it.
- If Session 1 isn't complete, warn in one honest line — "this session assumes
  your project is set up; Session 1 does that in about 20 minutes" — then
  respect their choice. Adults skip; warn, never block. (If there's no project
  at all, the first win has nowhere to save: say so and offer Session 1.)
- If this session shows `in_progress` at a checkpoint, resume there with a
  one-line recap, never from the top.
- Open with the picture, in one breath, for their lane. Scorecard lane: you say
  "score Ramp" → a two-agent team (scout does a fast, sourced web scan; scorer
  grades Fit, Timing, Reachability) → you get a one-page scorecard.
  Messaging-doc lane: you say "build my messaging doc" → a two-agent team
  (site-reader reads your website and captures exactly what it says;
  distiller turns it into your core messaging doc) → you get the one-pager
  every later draft leans on. Either way: they don't build this team today —
  they *run* it. Session 3 takes a single agent apart.

Then teach the steps for their lane. The two tracks below are the same lesson
with different payloads; run exactly one.

## The steps — scorecard lane (`sales`, `operations`, or unset)

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

## The steps — messaging-doc lane (`marketing`)

### 1. Name the brand — theirs

The first win is a **core messaging doc** for the brand they actually market:
positioning, voice, and the phrases the brand really uses, distilled from its
website. All they need is the website address — no exports, no analytics
logins, nothing to connect. Their own brand is the right first target (the doc
becomes the baseline everything later drafts against); a competitor's site is
a trick for Session 6. Use the suggestions and framing in `examples/roles.md`.

- *Checkpoint 1:* they've named one real website (theirs) in the conversation.

### 2. Point the team at it

They ask for the doc in plain language, right here: **"build my messaging doc
for acme.com"** (their site swapped in), or `/bluerock:messaging-doc acme.com`.
One optional extra before they send it: if they have a recent post, a campaign
email, or copy they're proud of, they can paste it in — the run folds it into
the doc. Nothing at hand? Skip it; the website alone works.

Set expectations in three beats: site-reader reads their homepage and the two
or three pages that carry the messaging, capturing exactly what the site says —
quoted, not paraphrased; distiller turns that (plus anything pasted) into the
doc — **positioning**, **voice**, and **the phrases you actually use**; the
finished doc opens as a **Claude Artifact** and the source saves in their
project at `my-work/messaging-doc/<brand>/`.

Claude will ask permission before reaching the web or writing to their
project. That's not a hurdle — it's them deciding what their agents are
allowed to touch, keeping them on the rails. Say yes, and take the "always
allow" option when offered so each one only asks once.

- *Recovery:* if they gave a company name and it asks *which* site they mean,
  give it the exact web address and it runs.
- *Checkpoint 2:* the team starts and the site read is visibly under way.

### 3. Watch two specialists work

While it runs, name what they're seeing: they dispatched a **team**, not one
bot, and it runs itself in order — nobody prompts each step. **site-reader**
captures what the site actually says, verbatim and sourced; **distiller**
turns it into the doc and names honest gaps. That hand-off is the thing to
notice.

- *Recovery:* if the doc comes back thin, the site just says little — the team
  reports that honestly rather than inventing messaging. That's a finding, not
  a failure (and often the most useful line in the doc). Pasting a recent post
  or email and re-running gives the distiller more to work with.
- *Checkpoint 3:* both specialists ran in order and the finished messaging doc
  exists in the project.

### 4. Open it, then send it

The doc opens as a Claude Artifact: a clean one-pager — the positioning line,
the voice attributes with quoted examples, the verbatim phrase bank, any gaps
worth knowing about. The markdown source is saved at
`my-work/messaging-doc/<brand>/`, theirs to keep and edit.

Then the actual win: **share it.** Send it to the person named in their role's
share moment (`examples/roles.md`). Five minutes ago it didn't exist; now it's
a work product with their name on it. That's the point of building instead of
chatting: you finish with something you can hand to someone.

- *Recovery:* if artifact publishing isn't available in their environment,
  don't block — the markdown is saved; show the path and move on.
- *Checkpoint 4:* the doc is open (or its saved path shown) and
  `my-work/messaging-doc/<brand>/` exists with the source inside.

## Step 5 — close out, the way builders work (both lanes)

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
   name the artifact concretely ("account scorecard on Ramp" / "core messaging
   doc for acme.com").
2. **Debrief — what just happened.** They didn't write two prompts; they
   pointed one team at one job and got a finished, sourced work product back.
   Each specialist is an **agent**: a worker with one job, its own
   instructions, and only the tools it needs. That's the idea the whole
   learning path is built on.
3. **One thing to notice for later.** Scorecard lane: right now Fit is judged
   against a sensible default, not against what *they* sell to. In Session 4
   they teach their project their objectives; then the exact same "score"
   command grades against their real priorities. Messaging-doc lane: right now
   the doc is a saved file. In Session 4 they wire it into their project's
   memory; then every skill they build drafts against it without being told —
   and in Session 6, the same team pointed at a competitor's site gives a
   side-by-side comparison with this doc as the baseline. Same work, sharper
   every time — that compounding is what they're really here to build.
4. Ask "how would you describe what you built?" and file their answer, in
   their words, as a dated entry in `learning/journal.md`.
5. Point forward: Session 3, **Anatomy of an agent** — about 20 minutes, where
   they take a single agent apart and write their first one. (If Session 3
   isn't available in-session yet, give its link from the learning-path manifest.)

If the wrap-up already ran as checkpoint 5, the progress commit rides it;
otherwise suggest `/bluerock:wrap-up` so nothing is lost.
