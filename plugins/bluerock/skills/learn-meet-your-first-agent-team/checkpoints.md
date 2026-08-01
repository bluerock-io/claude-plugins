# Session 2 — checkpoint verification spec

Everything in this session happens in this conversation and lands in the
project, so every checkpoint is inspectable. Run inspection commands quietly;
the builder sees conclusions, not plumbing. `<slug>` below is the slugified
company name the scorecard run used.

## Checkpoint 1 — a real company named

- **Evidence is conversational:** the builder has named one specific, real
  company in this chat. That statement is the checkpoint — no file to check.
  If they're stalling on the choice, offer the role-matched suggestions; don't
  pick for them.

## Checkpoint 2 — the team dispatched and running

- **Observed in-conversation:** the scorecard run started (the builder sent
  "score <company>" or `/bluerock:scorecard <company>` and the run visibly
  began).
- **Inspectable:** the working folder `my-work/account-scorecard/<slug>/`
  exists in the project once the run is under way.
- If the builder asked *you* to run it instead, that's the once-per-session
  escape valve — narrate if you use it, and note they dispatch the next run.

## Checkpoint 3 — both specialists finished

- **Inspectable:** `my-work/account-scorecard/<slug>/` contains `scan.md`
  (scout's output) and `scorecard.md` (scorer's output), both non-empty, and
  `scorecard.md` carries the three graded dimensions (Fit, Timing,
  Reachability) plus a recommended next action.
- A thin-but-honest scorecard passes (small web footprint is a fact, not a
  failure). A missing file fails: diagnose which specialist stopped and why
  before rerunning.

## Checkpoint 4 — scorecard opened and saved

- **Inspectable:** the folder and `scorecard.md` from checkpoint 3, plus the
  artifact (or, if artifact publishing isn't available in this environment,
  the saved path shown to the builder — that degrades honestly and still
  passes).
- Do not mark this passed on the artifact alone; the saved source in the
  project is the durable half.

## Checkpoint 5 — session closed out

- **Inspectable:** `session-log.md` at the project root has a dated entry for
  today covering this session, and `design/dashboard-data.js` was refreshed by
  the wrap-up (its content reflects this session's run).
- The builder runs the wrap-up themselves; you observe it in-conversation and
  then verify the files. If they skipped the git commit step inside wrap-up,
  that's fine — the checkpoint is the log and dashboard refresh, not the push.

## Marking progress

After each verified checkpoint N:
`sessions["2"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 5, `{ "status": "complete", "completed": "<today>", "artifact":
"account scorecard on <company>" }`. Write valid JSON; never delete history.
Never mark a checkpoint you didn't verify — honest state beats a green
dashboard.
