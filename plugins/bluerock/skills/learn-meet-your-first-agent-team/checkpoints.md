# Session 2 — checkpoint verification spec

Everything in this session happens in this conversation and lands in the
project, so every checkpoint is inspectable. Run inspection commands quietly;
the builder sees conclusions, not plumbing.

The five checkpoints are the same in both lanes; only the target, folder, and
file names differ. `<slug>` below is the slugified name the run used.

| | Scorecard lane (`sales`, `operations`, unset) | Messaging-doc lane (`marketing`) |
|---|---|---|
| Target | a real company | a real website (theirs) |
| Folder | `my-work/account-scorecard/<slug>/` | `my-work/messaging-doc/<slug>/` |
| First file | `scan.md` (scout) | `signals.md` (site-reader) |
| Final file | `scorecard.md` (scorer) | `messaging-doc.md` (distiller) |

## Checkpoint 1 — a real target named

- **Evidence is conversational:** the builder has named one specific, real
  target in this chat — a company (scorecard lane) or their brand's website
  (messaging-doc lane). That statement is the checkpoint — no file to check.
  If they're stalling on the choice, offer the lane's suggestions from
  `examples/roles.md`; don't pick for them.

## Checkpoint 2 — the team dispatched and running

- **Observed in-conversation:** the run started (the builder sent
  "score <company>" / `/bluerock:scorecard <company>`, or "build my messaging
  doc for <site>" / `/bluerock:messaging-doc <site>`, and the run visibly
  began).
- **Inspectable:** the lane's working folder exists in the project once the
  run is under way. Messaging-doc lane: if the builder pasted references,
  `references.md` should be in the folder too — a paste that never landed as a
  file is invisible to the agents; catch it here, not at checkpoint 3.
- If the builder asked *you* to run it instead, that's the once-per-session
  escape valve — narrate if you use it, and note they dispatch the next run.

## Checkpoint 3 — both specialists finished

- **Inspectable:** the lane's working folder contains the first file and the
  final file, both non-empty, and the final file carries its required parts —
  scorecard lane: the three graded dimensions (Fit, Timing, Reachability) plus
  a recommended next action; messaging-doc lane: positioning, voice, and the
  verbatim phrase bank (a Gaps section is optional and only present when
  earned).
- A thin-but-honest result passes (a small web footprint, or a site that says
  little, is a fact, not a failure). A missing file fails: diagnose which
  specialist stopped and why before rerunning.

## Checkpoint 4 — the work product opened and saved

- **Inspectable:** the folder and final file from checkpoint 3, plus the
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
  then verify the files. **The checkpoint is the log and the dashboard refresh, never a
  save or a backup.** A session where no save step appeared at all passes exactly like
  one where it did: wrap-up offers only what it has checked will succeed, so its absence
  is the skill working, not the builder skipping something. Don't ask them why it didn't
  happen, and don't send them to fix it.

## Marking progress

After each verified checkpoint N:
`sessions["2"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 5, `{ "status": "complete", "completed": "<today>", "artifact":
"account scorecard on <company>" }` (or `"core messaging doc for <site>"`).
Write valid JSON; never delete history. Never mark a checkpoint you didn't
verify — honest state beats a green dashboard.
