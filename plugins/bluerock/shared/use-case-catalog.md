# The use cases — the shared rule for offering one

Not a skill. Three skills read this file so that what a builder is offered, and the order
it comes in, live in one place: `/bluerock:check` shows the list, `/bluerock:onboard` names
where it is, `/bluerock:wrap-up` picks one. They differ in slice, not in source. (Product
decision, 2026-09-09: a findable list, not a recommender.)

**Why this exists.** Seven use cases shipped and nothing in-session told a builder they
existed. The first draft of a fix was a selection algorithm written into `help`, by one
session, on no research: match the role, prefer an artifact, prefer one not yet run. It was
cut. Recommendation logic gets invented if it is not designed, in whichever surface is
convenient; this file is the design, and the three skills quote it rather than growing their
own. The same drift, one level down, is why the manifest carries `tier` at all.

## The source, and the one predicate

`${CLAUDE_PLUGIN_ROOT}/curriculum/manifest.json` → `library`. It ships in the same release
as the skills, so it cannot drift. **Never name a use case from memory.** A remembered one
the builder does not have is worse than admitting uncertainty, because they will type it
and it will fail.

A record may be offered as a thing to run when **all three** hold:

1. **`tier` is `use-case`.** That field answers exactly one question, may a surface offer
   this, and it is the only field that does. `team-member` records are never offered alone,
   `held` records are never offered, `system` and `utility` are housekeeping and
   conveniences, `concept` is reading.
2. **`ships_from` is `toolkit` and the file is there:** `${CLAUDE_PLUGIN_ROOT}/skills/<id>/SKILL.md`
   exists. Read what ships, not the tier alone. If the manifest names a use case and the
   file is absent, trust the file and leave it out. That mismatch should never reach a
   release, and honest omission beats a command that fails.
3. **Anything with `ships_from: project`** lives in the builder's own `.claude/` and is
   theirs. Check the project before naming one, and never present it as a slash command;
   the project's files are the source of truth. (Three of the manifest's `team-member`
   agents ship this way, and none of them is a use case.)

## The order

`recommended_after` on each use-case record is an **authored adjacency list, not a model.**
It encodes one chain, the order the catalog page on learn.bluerock.io uses, so the page and
the session read the same order (one order, two readers). The record with
`recommended_after: []` is first; every other record names the one it follows. Walk the
chain to list them. Do not sort by anything else, and never rank by role, popularity, or
recency: none of those signals exists here, and the population is seven.

## Each line a builder reads

- The use case's **`title`**, exactly as written, then its command with the full prefix,
  `/bluerock:<id>`. The title names the deliverable, and the deliverable is what a builder
  is choosing.
- The **`one_liner`** when there is room for a sentence, or when they ask what one does.
  Read it; do not paraphrase.
- The **agent team**, from `team`, when naming who does the work: "a two-agent team, scout
  and scorer." The noun is *agent team*.
- **Never a time figure before a run.** `time_saved` and `time_saved_minutes` are inputs to
  the tally `wrap-up` shows *after* a run, not copy before one. An estimate shown before a
  builder runs something is a promise; the same estimate shown after they ran it is a
  report. (Decision 2026-09-09.)
- **Never "catalog" or "index" as a word the builder reads.** Those are our names for the
  list. A builder sees use cases, or what they can run.
- **Nothing unbuilt.** If it is not in the manifest with its file present, it does not
  exist to the builder.

## What this builder has already run

`.bluerock/runs.json` in the builder's project holds one atom per run with an `agent`
field. Every use case's `team` is disjoint from every other's, so an atom attributes to at
most one use case: match `agent` against each use case's `team` members, its `id`, its
`title`, or `/bluerock:<id>`. Atoms that match nothing are the builder's own skills and
agents; leave them out of anything use-case-specific. **One run of a use case is one group
of atoms sharing `sessionId` and target.** A team may log one atom per member or one per
run; count the run, not the members.

## The concept behind what they ran

Each use-case record carries **`concept`**, the id of a `concept` record, which in turn
names the session that teaches it (`used_in_sessions`). Six of the seven dispatch an agent
team, so the honest pointer for most of them is the same concept, and the session that
teaches it assumes earlier ones. **The rule:** point at the concept that explains what they
just used; walk that session's `prerequisites` back through `learning/progress.json`, and
if any is not `complete`, offer the **earliest unmet one** instead, framed as where the
explanation starts. If the concept's own session is already `complete`, say nothing; they
have the depth.

**Framing, and it is load-bearing:** the sessions are depth available when the builder
wants it, never progress against eight. No "3 of 8," no progress bar, no count of sessions
left. (Decision 2026-08-30: Sessions 3 to 8 are reference depth, not a syllabus. Reaffirmed
2026-09-09.)

## Who depends on this file's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/check/SKILL.md`** (the Next block's three states), **`skills/onboard/SKILL.md`**
  (its closing line), and **`skills/wrap-up/SKILL.md`** (step 2's tally and step 6's Next
  up) read this file. Reword the rule here and all three move together, which is the reason
  this file exists.
- **`.github/scripts/check_release_hygiene.py`** guards the fields this file reads on every
  use-case record: `title`, `concept`, `recommended_after`, `team`, `time_saved_minutes`.
  It also checks that `recommended_after` forms one chain and that `concept` names a
  `concept` record.
- **The catalog page on learn.bluerock.io** reads the same titles and the same order from
  `learn-site` `app/learn/_data/use-cases.ts`. If the page's order or a title changes,
  `recommended_after` or `title` changes here in the same week, and the decision that moves
  it is logged.
