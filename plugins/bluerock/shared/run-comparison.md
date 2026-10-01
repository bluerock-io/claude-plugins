# Comparing a run with an earlier one — the shared rule

Not a skill. The contract every use case follows when its value is **what changed since the
last run**: finding the earlier run, pairing what is in it with what is in this one, and
writing the comparison down. `/bluerock:battlecard-refresh` is the first reader. The pipeline
inspection use case is the second, and it reuses this file and the `change-reader` agent
rather than inventing a second comparison. (Product decision, 2026-10-01.)

**Why one file.** Two use cases that each write their own "what changed" will disagree about
what a change is: one counts a reworded sentence, the other misses a deal that disappeared.
A builder who runs both learns that "changed" means nothing. One definition, one agent, one
output shape.

## 1. Find the earlier run — by its contents, never by its name

Runs live in dated folders under `my-work/<use-case>/<YYYY-MM-DD>-<slug>/` and are never
overwritten. Builders rename folders, move them, and paste files in by hand, so:

1. List `my-work/<use-case>/`. A folder is a run if it holds **the use case's output file**
   (for battlecards, `battlecard.md`), whatever the folder is called.
2. If that finds nothing, search the project one level deeper for the output file by name
   (`find <project>/my-work -maxdepth 3 -name battlecard.md`). A run found outside its usual
   folder is still a run; say where it was found.
3. **Date a run by what it says, not by its folder name:** the date line inside the output
   file or `inputs.md` first, the folder's date prefix second, the file's modified time last,
   and say which one was used when it was not the first.
4. More than one candidate: propose the most recent and name the others in one line. The
   builder can pick an older one (comparing against the quarter-start run is legitimate).
5. **None found: say so plainly and route to the use case that makes the first run.** A
   comparison with nothing to compare against is not a comparison, and never fake one by
   treating this run as both sides.

## 2. Pair what was there with what is there now

The dispatching skill tells `change-reader` what an **entity** is (a competitor, a deal, an
account) and what identifies one (a name plus domain, a deal ID). Pair on the identifier,
never on position or wording. An entity in only one run is **New** or **Not re-found**
(below), never silently dropped.

## 3. The five kinds of change — the only five

Every comparison line is exactly one of these. The words are load-bearing: the artifacts
render them by name.

| Kind | Means | Needs |
|---|---|---|
| **New** | In this run, not in the earlier one | A source in this run, dated when the thing is dated |
| **Changed** | In both, and the fact is different | The earlier value with where it came from, the new value with its source |
| **Gone** | Was true, and this run shows it is no longer true | **Positive evidence it ended** (retired, removed, closed, repriced away). Absence is not evidence |
| **Not re-found** | In the earlier run, and this run neither confirmed nor contradicted it | Nothing. It is a gap, said plainly, and it is never shown as Gone |
| **Unchanged** | In both, same fact | This run re-confirmed it. Unchanged is a finding, not filler |

Rules that hold across every use case:

- **Rewording is not a change.** Two runs describing the same fact in different words are
  Unchanged. A change is a different fact, a different number, a different status.
- **A change needs evidence from this run.** Never infer a change from the calendar ("it's
  been three months, pricing has probably moved").
- **Earlier claims keep their markers.** A `[their claim]` or `[unverified]` from the earlier
  run stays marked when it is carried forward; re-confirming it from an independent source is
  what lifts the marker, and that is itself a Changed line.
- **Material first.** Each entity's lines are ordered by how much they change what the
  builder would do: a fact that breaks an earlier talking point, a price, a status change on
  something they rely on, then the rest.
- **No change at all is said in one line:** `No material change since <date>.` That is the
  result, and it is a good one.
- **Old baselines are named.** When the earlier run is more than a quarter old, the
  comparison says so at the top; the further back, the more of it is a rebuild.

## 4. The output — `changes.md`

`change-reader` writes `changes.md` in the current run's working folder:

```markdown
# Changes since <earlier run date> · <this run date>

**Compared:** <earlier run path> → <this run path>
**Baseline age:** <N days> <and, past a quarter: "older than a quarter; treat as a rebuild">

## <Entity>
**Summary:** <one line: the most material change, or "No material change since <date>.">

| Kind | What | Before (earlier run) | Now (this run) | Evidence |
|---|---|---|---|---|
| Changed | <field or claim> | <earlier value> · <file § section> | <new value> | <source, dated> |
| ...

**Carried, unchanged:** <count>, listed in one line each beneath the table
**Not re-found:** <list, or "none">
```

One section per entity, in the order the earlier run listed them, then any **New** entities
at the end.

## Who reads this

- `agents/change-reader.md` implements it.
- `skills/battlecard-refresh/SKILL.md` dispatches it with entity = competitor.
- The pipeline inspection use case will dispatch it with entity = deal. When it lands, add
  it here.
- Changing the five kinds, or the `changes.md` headings, changes what both artifacts render.
  Update every reader in the same pass.
