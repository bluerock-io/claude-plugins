# Session 6 — checkpoint verification spec

Five checkpoints across two parts. Part one verifies files the builder **reads**;
part two verifies a team they **composed**.

**Checkpoints 3, 4, and 5 verify SHAPE, not content.** It's their job, their
roles, their team — there is no correct answer to assert. Check that roles have
named handoffs, that specs exist with scoped tools and a fallback, and that the
dispatch actually handed off. Whether the team is *good* is theirs to judge, and
step 5's editor read is where they judge it.

**This is the session most likely to be finished across two days.** Write
progress after every checkpoint, not at the end. The natural break is between
checkpoints 2 and 3.

Run inspection commands quietly; the builder sees conclusions, not plumbing.
`<project>` is the project's absolute path.

## Checkpoint 1 — the seeded team ran end to end

- **Inspectable:** `my-work/account-research/<company>/` exists under the project
  and contains the team's output — `profile.md` (researcher), `signals.md`
  (signal-scanner), and the dossier (composer). All three files, non-empty.
- **The three files are the point, not just the dossier.** They are the physical
  evidence of the pipeline the builder is about to read about. If the dossier
  exists but `profile.md` doesn't, something ran differently than taught — find
  out what before moving to step 2, because step 2's lesson assumes the handoff
  happened.
- **Thin sections pass.** A company with a small web footprint produces a thin
  profile, and the team is written to flag gaps rather than invent. `[not found]`
  markers in the output are the floor working, not a failure. Say so.
- If nothing ran because the builder typed `/bluerock:research`, that's the known
  naming bug: `research` is a project skill and fires bare as `/research`.
  Redirect in one line.

## Checkpoint 2 — they can point at the tools lines and the handoff

- **Conversational, and it's the load-bearing check of part one.** Ask for each,
  and wait:
  1. **Why the three tools lines differ** — `researcher` and `signal-scanner`
     have `WebSearch, WebFetch` because gathering is their job; `composer` has
     `Read, Write, Glob` and no web because it synthesizes what's already
     sourced. They don't need the exact tool names; they need the *reason*.
  2. **The one line where the handoff happens** — signal-scanner's Job opening:
     read `profile.md` first.
- **Pass spec:** they can explain that signal-scanner never saw the researcher's
  work, and picks it up from the file. That sentence is the whole session's
  mechanism, and step 5's signature failure is diagnosable only by someone who
  holds it.
- If they can't get there, walk it again before part two. Part two will produce a
  team that doesn't hand off, and they won't know why.
- Optional but valuable: ask what the composer reads beyond the two files
  (`voice.md`, `objectives.md`). It's where Session 4 pays off visibly.

## Checkpoint 3 — two or three roles, each with a named handoff

- **Conversational:** two or three roles written down, each with a one-line job,
  and — the part that matters — **what each hands to the next.**
- **Pass spec, and hold this line:** if role one's output isn't role two's input,
  they have two unrelated agents rather than a team. Ask "what does role two read
  that role one wrote?" and get a real answer. A vague "then it uses that" is not
  yet a handoff; push once for the artifact.
- **A two-role team is a full pass.** Three is not better. The gatherer/maker
  split is the honest minimum and the shape scales.
- **If the job doesn't split, that's a finding, not a failure.** Either it
  finishes in one pass (it's a skill — Session 5 covered it) or it's a whole
  workflow rather than a job. Help them pick a smaller job; don't force a split
  to reach a checkpoint.
- Reusing a seeded agent for a role passes. A team of `researcher` plus one new
  agent they wrote is a real team.

## Checkpoint 4 — each role exists as a scoped agent file

- **Inspectable:** for each role, a file in `<project>/.claude/agents/<name>.md`
  with:
  1. **frontmatter** carrying `name`, `description`, and a `tools` line;
  2. **tools scoped to the job** — the least-privilege check, and the only place
     to be firm: a role that doesn't gather does not get `WebSearch` /
     `WebFetch`. If a maker came back with web tools, say why it matters and have
     them trim it. This is the operations lesson of the session and it is worth
     one round of insistence.
  3. **a fallback for missing inputs** — some instruction covering what to do
     when what it expected to read isn't there. Any honest form passes.
  4. **the handoff named**, for every role after the first: the spec says which
     file to read. Catch a missing handoff line **here**, because step 5 fails
     confusingly without it.
- **Assert nothing about the identity or procedure text.** That's theirs.
- **Reused seeded agents need no new file.** Note which roles are reused and
  verify only the new ones.
- **Saved:** `git -C <project> log -1 --stat` shows the new agent files. Run it
  quietly — the builder sees the conclusion ("your new agents are saved"), not
  the command. **Verify the result, never the mechanism**, and say "saved," never
  *committed*: a workspace with no remote is the normal finished state, so a save
  that never leaves the workspace is a pass, and pushing, backup, and GitHub stay
  unmentioned unless they ask. If this is their first save of the session and
  Claude asks what name and email to record it under, that is expected on a fresh
  workspace, not an error — say so and let them answer.

## Checkpoint 5 — the team ran on a real job and handed off

- **Observed in-conversation plus inspectable output.** Three parts:
  1. the roles ran **in order**, with the second picking up from what the first
     produced;
  2. the output exists as files where their specs said to write them;
  3. the builder read the results and can name what they'd change — the editor
     read is part of the checkpoint, not a nicety.
- **The handoff is the checkpoint.** If the second specialist produced good
  work but started from scratch — re-gathering rather than reading role one's
  file — that **fails**, even though there's output. Its spec is missing the
  "read `<file>` first" line. Fix and re-dispatch. Passing this on plausible
  output teaches nothing, and it is the exact failure the session exists to make
  legible.
- **"A result I would use" is theirs to judge, and a no is still a pass** — as
  long as they can say what to sharpen. Then have them sharpen one spec and save
  a checkpoint; that edit is the loop.
- **A real job, not a toy.** Same standard as Session 5: made-up input makes the
  editor read fake too.

## Marking progress

After each verified checkpoint N:
`sessions["6"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 5, `{ "status": "complete", "completed": "<today>", "artifact":
"<their team>, dispatched on <the real job>" }`. Write valid JSON; never delete
history. Never mark a checkpoint you didn't verify — honest state beats a green
dashboard.
