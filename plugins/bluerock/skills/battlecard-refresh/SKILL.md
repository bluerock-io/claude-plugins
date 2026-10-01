---
name: battlecard-refresh
description: >-
  Battlecard Refresh — take the battlecards you already have and bring them up to date
  against what changed, instead of starting over: every earlier claim re-checked, the kill
  points that stopped being true retired, what's new added, and a "what changed" view up
  front. Use when I say "refresh my battlecards", "update the battlecard on <competitor>",
  "what changed with <competitor>", "are my battlecards still right", "anything new from
  <A> and <B> since last time", or before a deal against a competitor I've carded before.
  Needs a previous Competitor Battlecards run in my-work/competitive-intel/. Runs
  competitor-scanner (once per competitor, concurrently) → change-reader → analyst, and
  writes a new dated run beside the old one.
---

Run a **Battlecard Refresh**: take a builder's earlier battlecards and bring them up to date.
You orchestrate the agents; they do the work. This is what makes it a refresh rather than a
rerun: the fresh scans are compared with the earlier ones by `change-reader`, and the analyst
edits the earlier cards rather than writing new ones. A builder who has been using a card
sees the three lines that moved, not a new card to reread.

**What it replaces:** going back through every competitor's site, pricing page, and changelog
to check whether last quarter's battlecards are still true, then editing them by hand.
**Time saved:** about 45 minutes by hand, estimated and not yet timed.

## First — anchor to the project

Exactly as `/bluerock:competitive-intel` does, by signature, never by name: run `ls`; see
`CLAUDE.md` and `design/` side by side? You're in the project. If not, `ls */CLAUDE.md`, then
`ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in,
capture the **absolute path** with `pwd`, and use it throughout. Can't find it? Ask which
folder their project is in.

## Find the earlier run

Follow `${CLAUDE_PLUGIN_ROOT}/shared/run-comparison.md` § 1. For this use case, the output
file is `battlecard.md` and the folder is `my-work/competitive-intel/`. Earlier refreshes
live there too and count as runs, so a refresh can refresh a refresh.

- **One or more found:** propose the most recent in one line, with its date and the
  competitors it covers, and name any others: *"Refreshing your 2026-07-14 cards on Otter,
  Fireflies, and Fathom. (You also have a 2026-06-02 run.)"*
- **Older than a quarter:** say so before the intake, plainly: the refresh will re-check
  everything and much of it will read as new. Run it anyway if they want; it is still the
  faster route than a cold run, because their inputs carry over.
- **None found:** stop and say so. *"A refresh needs battlecards to refresh, and there aren't
  any in your project yet. Want me to build the first set with `/bluerock:competitive-intel`?
  Run this again in a week or two and it'll tell you what moved."* If they say they have
  battlecards somewhere else, ask where; a `battlecard.md` found by contents anywhere in
  `my-work/` is a run. A battlecard they wrote by hand in another format is not one this can
  compare against: route them to a first run.

## Intake — what changed on your side, not the whole form again

Read the earlier run's `inputs.md` (industry, competitors, differentiators, personas, notes).
Play it back as a short list and ask **one** question: *"Same as last time, or has anything
changed on your side: a competitor to add or drop, a new differentiator, a different person
in the room, a new note?"* A builder who says "same" goes straight to the run.

If something changed, take the change only, in their words, then confirm the updated list.
The cap is still 4 competitors per run. A competitor added now gets a full first card; one
dropped is listed as dropped and gets no card.

**The moment the builder approves**, set the expectation for the wait in one message of its
own: the scans run concurrently and take several minutes, so it's a good moment to switch
tasks. Then go quiet until the report.

## Set up the run

1. **Make the working folder:** `my-work/competitive-intel/<YYYY-MM-DD>-<slug>-refresh/`,
   beside the earlier run, never inside it. The earlier run is never edited or overwritten:
   it is the "before" in this comparison and possibly the next one.
2. **Write `inputs.md`** into the new folder: the confirmed intake, carried verbatim, plus
   two lines the earlier run did not have: `refreshed_from: <absolute path of earlier run>`
   with its date, and, if anything changed, `changed since <date>: <what>` in the builder's
   words. This is the record the next refresh reads.

## Run the agents

Ordinary subagents, no agent-teams tooling. Pass every path as an **absolute path** in the
dispatch prompt.

3. **Dispatch one `competitor-scanner` per competitor, all in a single message so they run
   concurrently.** Each gets its competitor, the industry, the new working folder, and, for a
   competitor carried from the earlier run, **the path to that competitor's earlier
   `scan-<slug>.md` and the earlier run's date**. That puts the scanner in refresh mode (its
   own file says what that means). A competitor added for this run gets a normal dispatch
   with no earlier scan. Wait for all of them.
4. **Dispatch `change-reader`** with: the earlier run's folder and date, the new folder,
   entity = competitor (identified by name and domain), facts in the earlier run =
   `battlecard.md` plus its `scan-*.md`, facts in this run = the new `scan-*.md`. It writes
   `changes.md` in the new folder.
5. **Dispatch `analyst`** with the new folder, the earlier `battlecard.md` path, and the
   `changes.md` path. That puts it in refresh mode. It writes the refreshed `battlecard.md`
   in the new folder: a **What changed** section first, then the cards with a status tag on
   every kill point, strength, and head-to-head row.

## Publish the artifact — you, not the agents

6. Read the refreshed `battlecard.md` and `changes.md` and **publish one Claude Artifact**
   yourself. If artifact publishing isn't available, don't block: the markdown is saved; say
   so and give the path.

### The artifact — design contract

**Start from the Competitor Battlecards contract and follow it exactly:**
`${CLAUDE_PLUGIN_ROOT}/skills/competitive-intel/SKILL.md` § "The artifact — design contract":
the same CSP rules, fonts, tokens in both themes, sticky masthead and tab strip, legend,
per-competitor panels with the same sections in the same order, print rules, and footer.
Read it from that file every run; do not work from memory of it. These are the only
differences:

- **Masthead title:** `<industry> · Battlecards, refreshed`. The meta line reads
  `<this date> · refreshed from <earlier date> (<N> days) · FOR: <personas> · <N> source
  domains`.
- **The first tab is "What changed",** visible on load, ahead of the competitor tabs and the
  field views. It replaces the "Since your last run" strip. Per competitor: the summary line
  from `changes.md`, then the material lines as rows, each with a kind chip (`New`,
  `Changed`, `Gone`, `Not re-found`), the before and now side by side, and the evidence in a
  mono source chip. Retired kill points listed by name beneath. A competitor with no
  material change gets its one line and nothing else. Close the tab with the counts: lines
  carried unchanged, updated, new, retired.
- **Kind chip colors:** New = accent, Changed = mine, Gone = kill, Not re-found = neutral.
  Unchanged lines are not rows on this tab; they are the count.
- **Status tags on the cards:** each kill point, strength line, and head-to-head row shows
  its tag as a small mono chip: `carried` neutral, `updated` mine, `new` accent, `retired`
  kill. A retired kill point renders with its text struck through and its one-line reason
  beneath, at reduced opacity, after the live kill points. It stays visible so the builder
  knows to stop using it.
- **Footer** adds `Refreshed from <earlier run path>` and ends `Built with BlueRock ·
  Battlecard Refresh · competitor-scanner + change-reader + analyst`.

**The scan test:** someone opening this before a call has eight seconds. The What changed
tab, its kind chips, and the retired lines must tell them what moved before they read a
sentence.

## Finish

7. **Report:** the new folder path; the one line that matters most (a retired kill point
   beats a new one: the builder may be saying something that is no longer true); and the
   artifact or the fallback note. Don't reprint the cards.
8. **Name the rhythm, once:** the next refresh compares against this one, so a regular run
   (before each quarter, or before a deal against a carded competitor) keeps the cards
   honest. If they want it on a schedule, Session 7, *Put an agent on a schedule*, shows
   how. Then stop. One beat, no more.

## Honesty rules this skill carries

- **Every rule from Competitor Battlecards holds:** sourced versus supplied never blur, a
  thin competitor gets a short honest card, no FUD, no disparagement.
- **A change needs evidence from this run.** Gone needs proof it ended; a fact the scan
  simply did not mention is Not re-found and is shown as a gap. The five kinds and their
  rules are in `shared/run-comparison.md`.
- **The earlier run is read-only.** Never edit or delete it, even to fix it.
- **"No material change" is a result.** Say it in one line and carry the card. Never pad a
  quiet quarter with rewording.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`shared/run-comparison.md` owns the five kinds of change** (New, Changed, Gone, Not
  re-found, Unchanged) and the `changes.md` shape. This skill's What changed tab renders
  them by name, and so will the pipeline inspection use case.
- **`agents/analyst.md` owns the card section names and the refresh status tags**
  (`carried`, `updated`, `new`, `retired`); the artifact renders them by name.
- **`skills/competitive-intel/SKILL.md` § the artifact** is the base design contract this
  skill extends. A change there changes this artifact too, which is intended.
- **`agents/competitor-scanner.md` § refresh** and **`agents/change-reader.md`** are
  dispatched with the inputs listed in steps 3 and 4. Rename an input in either and the
  dispatch here changes with it.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`, `level`,
  `time_saved`, and `team`.
- The working folder shape `my-work/competitive-intel/<YYYY-MM-DD>-<slug>-refresh/` keeps a
  refresh in the same history as the runs it refreshes; `/bluerock:competitive-intel` step 8
  finds a refresh's `battlecard.md` as its previous run the same way.
