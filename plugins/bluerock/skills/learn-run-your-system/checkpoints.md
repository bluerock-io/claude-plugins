# Session 8 — checkpoint verification spec

The capstone verifies differently from every other session, and the difference is
the point: **it mostly checks things that already exist** rather than things the
builder makes today. Two of the five checkpoints are fully inspectable (1 and 5),
two are conversational (2 and 4), and one is **explicitly unverifiable** (3).

**Checkpoint 3 cannot be verified, and this spec says so rather than
pretending.** A skill cannot confirm that a human presented to another human. It
does not block completion. See the honest-recording rule under it.

Run inspection commands quietly. `<project>` is the project's absolute path.

## Checkpoint 1 — the system read back from the real project

- **Inspectable, and it's the work of the step.** Actually run the inventory
  before saying anything about what they built:
  - `ls <project>` and read `CLAUDE.md`, `voice.md`, `objectives.md` — filled or
    still seeded? How many avoid-rules? Is `objectives.md` ranked?
  - `ls <project>/.claude/skills/` — split shipped (`meeting-recap`, `capture`,
    `research`) from **theirs**.
  - `ls <project>/.claude/agents/` — split shipped (`scribe`, `daily-brew`,
    `researcher`, `signal-scanner`, `composer`, `meeting-prep`) from **theirs**.
  - `ls <project>/notes/ <project>/briefs/ <project>/my-work/` and **count the
    files** — the number they haven't been watching.
  - `git -C <project> log --oneline | wc -l`, and the first commit's date.
  - `learning/journal.md` — read it; their own words are the best material here.
- **Pass spec:** you have named back, **specifically**, what is actually there.
  Generic summary of the curriculum is a fail — "you built memory, skills, agents,
  and routines" is the sentence this checkpoint exists to prevent.
- **Get the seeded-versus-theirs split right.** Crediting a builder with
  `scribe` or `meeting-recap` as their own work is the one error in this session
  that actually stings, and it undermines everything the inventory is for. When in
  doubt, check whether the file is unchanged from the starter kit.
- **A thin inventory still passes.** It is a true reading, and it makes step 4
  sharper. Say it kindly, don't inflate it.

## Checkpoint 2 — the three-sentence workflow statement

- **Conversational:** three sentences — what runs, what it produces, what they
  stopped doing by hand.
- **The third sentence is the checkpoint.** "It saves me time" is not it. Something
  concrete they no longer do: reconstructing the week from scrollback, rewriting
  drafts to sound like them, assembling the status by hand. Push once for
  specificity.
- **If the third sentence won't come**, that is a real finding rather than a
  failure: the workflow runs but isn't load-bearing yet. Record it, pass the
  checkpoint on an honest statement, and carry it into step 4 — it is often the
  best gap in the session.
- **Said out loud once.** If it doesn't survive speech, it isn't tight enough yet.

## Checkpoint 3 — the live walk (unverifiable by design)

- **There is no evidence you can inspect.** No file lands. The audience is a
  person. Do not invent a pass.
- **Record exactly what happened**, and only one of these:
  - *They presented (or recorded), and reported back.* Take their word, note it,
    and mine the gaps with them while it's fresh — where they hedged, the one
    question that stung.
  - *They chose not to.* Equally honest. Record it as declined and move to
    step 4, where you take the audience's part.
- **Never record "will do it later" as a pass.** If they intend to do it after
  the session, note it as an intention, not an outcome, and pass the session on
  the other four checkpoints.
- **This checkpoint never blocks completion.** The session reaches `complete`
  without it, on checkpoints 1, 2, 4, and 5. If a future decision makes the
  capstone presentation-gated, that changes what "complete" means for the whole
  path and is a product call, not a spec tweak.

## Checkpoint 4 — the gap, named in one sentence

- **Conversational, and this is the capstone's actual payoff.** They can name the
  next thing their project needs and say why.
- **Pass spec:** specific enough to start on. "Improve my skills" fails. "Add a
  check for whether the follow-up already went out" passes. "Write the ops version
  of my status skill" passes.
- **If they skipped step 3, you take the audience's part** — the questions are in
  the skill's step 4, and they work off checkpoint 1's inventory: what would they
  least like to explain, what's still by hand, what did they build and never run
  again. Do not shortcut this to a suggestion of your own. **A gap they named is
  the thing they'll actually build; a gap you named is advice.**
- One is enough. Resist collecting a backlog.

## Checkpoint 5 — closed out for real

- **Inspectable, fully**, and it's the session's hard evidence:
  - `session-log.md` at the project root has a dated entry for today;
  - `git -C <project> log -1` shows the wrap-up commit;
  - `design/dashboard-data.js` was refreshed by the wrap-up.
- **The builder runs it themselves.** wrap-up has a confirm gate; confirming is
  theirs, and running it for them removes the one habit this session exists to
  hand over.
- **A blocked push still passes** on the local commit and the log entry. Say the
  sync needs fixing; don't teach git here.
- **If nothing pushed, they probably haven't confirmed yet** — that's the common
  case, not a failure. If the push was rejected, have them pull (their routine may
  have pushed since) and run wrap-up again.
- **The continuation prompt is part of the checkpoint:** confirm they have it and
  know what it's for. It is the artifact that makes the *next* session cheap, and
  it's the last thing the path teaches.

## Marking progress

After each verified checkpoint N:
`sessions["8"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 5, `{ "status": "complete", "completed": "<today>", "artifact":
"<their workflow statement's subject>, presented and closed out" }` (or "…,
closed out" if they declined the walk — keep the artifact honest too).

**This is the checkpoint that completes the path.** Write valid JSON; never delete
history. Never mark a checkpoint you didn't verify — and in this session,
checkpoint 3 is the one you are explicitly allowed not to verify, provided you
record which way it went.
