# Session 3 — checkpoint verification spec

Everything in this session lands in files in the project, so every checkpoint is
inspectable. Run inspection commands quietly; the builder sees conclusions, not
plumbing. `<project>` is the project's absolute path; `<today>` is today's date
in the builder's timezone, which is the same date scribe computed.

**This session has the cleanest verification in the path** — step 2's checkpoint
is a git diff. Use it rather than reading the file and forming an impression.

## Checkpoint 1 — scribe filed today's notes

- **Inspectable:** `notes/<today>.md` exists in the project and holds what they
  told scribe, sorted under the template's headings. Since 2026-08-17 the input
  is **their own day**, so there is no fixed expected content — check the SHAPE
  instead: whatever they said happened lands under **Meetings**, anything they
  committed to under **Decisions / commitments**, and anything unresolved under
  **Open threads**. A one-line day sorts into one section and still passes.
- **Also confirm the sorting, not just the file.** Everything dumped under
  Brain dump means scribe filed but didn't parse — worth a re-run with clearer
  input, because step 3 depends on parsing working.
- **A file that already existed and gained a section passes.** scribe appends
  when the day's file is there; that is correct behavior, not a partial pass.
- If the file landed in the *home* folder rather than the project, that's the
  known relative-path failure. Move it into the project and say what happened
  in one line.

## Checkpoint 2 — the Wins line added, and nothing else moved

- **Inspectable, exactly:** `git -C <project> diff -- .claude/agents/scribe.md`.
  Pass requires **both**:
  1. the diff **adds** a Wins entry to the section list inside **step 3 of the
     Job** — a line naming Wins and what it holds;
  2. the diff is **small** — that one addition, give or take whitespace.
- **The second condition is a real pass criterion, not a nicety.** A large
  diff means Claude rewrote the spec instead of adding to it, which is the
  session's most common failure and the reason the approval habit is being
  taught. Say so plainly, have them revert (`git -C <project> checkout --
  .claude/agents/scribe.md`) and ask again with "just add the Wins line, leave
  everything else exactly as it was." Do not pass a large diff because the Wins
  line is technically in there.
- **If they already committed the change,** the working-tree diff is empty and
  that is not a failure: use `git -C <project> log -1 -p -- .claude/agents/scribe.md`
  and apply the same two conditions to that patch.
- **If the project has no git history at all** (rare, and it means the clone in
  Session 1 went sideways), fall back to reading `scribe.md`: the Wins entry
  present inside the Job's step 3 list, and the Identity / Context / Tools /
  Output sections all still intact and unrewritten. Note that you verified the
  weaker way.
- **A Wins section in the wrong place fails.** Added at the end of the file, or
  as its own top-level heading, it won't reach the sorting behavior step 3
  tests. Catch it here rather than letting step 3 fail confusingly.
- **The conversational half of this step has no separate checkpoint**, but don't
  skip it: they should have `scribe.md` open and have heard the five parts named
  against what they watched. If they can point at Identity, Job, Context, Tools,
  and Output in the real file, the session has landed. If they can't, walk it
  again before moving on — step 3 will pass either way, so this is the only
  place it gets caught.

## Checkpoint 3 — their real day, with Wins populated

- **Inspectable:** `notes/<today>.md` has a **Wins** section with something in
  it. Step 1 already established that the content is theirs, so this checkpoint
  is now about the section they added in step 2 doing its job.
- **An empty Wins section is the failure to catch.** It means they didn't give
  it a win — re-run asking for one explicitly, rather than assuming the edit
  is broken.
- **If Wins stayed empty after they did give a win,** the cause is step 2's edit,
  not this step: check the Wins entry sits inside the Job's step 3 list. Fix
  there and re-run; don't keep re-prompting.
- Their content may be thin — one line about one call is a pass. This checkpoint
  is about the loop closing, not about the quality of their notes.

## Marking progress

After each verified checkpoint N:
`sessions["3"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 3, `{ "status": "complete", "completed": "<today>", "artifact":
"scribe with a Wins section they added, filing their real day" }`. Write valid
JSON; never delete history. Never mark a checkpoint you didn't verify — honest
state beats a green dashboard.
