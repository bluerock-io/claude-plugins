---
name: crm-cleanup
description: >-
  CRM Cleanup and Enrichment — drop in a CSV export of accounts from your CRM and get back
  a cleaned file ready to re-import, plus a change log naming every edit and the source
  for every value added. Fixes formats, finds duplicates, and fills missing industry,
  employee count, and headquarters from public sources, capped per run. Use when I say
  "clean up my CRM export", "clean this account list", "fill in the missing industries",
  "enrich my accounts", "find duplicates in my CRM", "my CRM data is a mess", or drop a
  CRM export and ask to fix it. Runs a script for the exact work, record-enricher (one per
  batch of 8, concurrently) → record-auditor, and writes to my-work/crm-cleanup/.
---

Run the CRM Cleanup team on an accounts export and produce two things: a **cleaned CSV** the
builder imports back into their CRM themselves, and a **change log** naming every edit, with
a source for every value that was added. You orchestrate; a script does the exact work and the
agents do the lookups and the judgment calls.

**Why both halves:** duplicate and format checks are built into the major CRMs. Finding a
missing industry, employee count, or headquarters from public sources is the part a person
cannot do quickly, and it is most of this run. Cleanup goes first because it finds the gaps
enrichment fills.

**What it replaces:** looking up each incomplete account by hand, one tab at a time, and
fixing formats in a spreadsheet before an import.
**Time saved:** about 1.5 hours by hand per run, estimated and not yet timed.

**This use case never writes to a CRM.** It writes a file. The builder imports it.

## First, anchor to the project

The run folder and the export live in the builder's project. Two generations exist: the
project ships inside the workspace image (usually the folder `my-workspace`); projects made
before 2026-08 were cloned and carry whatever name the builder chose. **Assume neither;
identify it by its signature.** In an SSH or cloud container the chat may start in the project
itself or in the **home folder** with the project one level down; both are normal. Run `ls`;
see `CLAUDE.md` and `design/` side by side? You're in the project. If not: `ls */CLAUDE.md`,
then `ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in,
capture the **absolute path** with `pwd`, and use it throughout. Can't find it? Ask the builder
which folder their project is in.

The script ships with this skill. Call it by its full path, from anywhere:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/crm-cleanup/crm_csv.py" <command> ...
```

## The data in an export: say this once, before it is opened

A CRM export holds the builder's account data. Say plainly, in one or two sentences: the file
stays in their project; the lookups search the web for **company names and domains only**,
never owners, phone numbers, or any other column; and nothing is written to their CRM. Then
move on. Never paste the export's rows into the chat beyond the few names a playback needs.

## Intake: one question per step, short, then confirm

Ask one at a time. Skip what they already gave you: if the opening request named a file, say
what you're taking as given (`Export: accounts-2026-10-01.csv`) and pick up at the next step.
A previous run's `inputs.md` in `my-work/crm-cleanup/` pre-fills the same way: propose,
confirm, don't re-ask cold.

Use the question picker (`AskUserQuestion`) only where the answer is a choice between a few
options: steps 1 and 3. Everywhere else, ask in the message and let them type. Where the
picker isn't available, ask in the message.

1. **The export.** One explicit choice, once: *use the sample export* (a 46-row accounts
   export of well-known companies, with gaps, duplicates, and format errors planted on
   purpose; it needs no real data) · *use my own export*.
   - **Sample:** copy `${CLAUDE_PLUGIN_ROOT}/skills/crm-cleanup/sample-accounts-export.csv`
     to `my-work/crm-cleanup/sample-accounts-export.csv` in their project, so they can open
     it, and use that copy.
   - **Their own:** "Export your **accounts** (companies), not contacts, as a CSV, and put the
     file in your project: drag it into the file panel, or attach it here and I'll save it
     into your project. Include the record ID column." Accounts only, for now: a contacts
     export is people's personal data, and this version does not take one. If they give
     you contacts, say so and stop at this step.
2. **Read it and play back what the script found.** Make the run folder and run `profile`
   into it (step 6 has both), then say, briefly: the row count; **which column it took for
   each field** (`Company name → name, Website → domain, Billing State/Province → state…`);
   the columns it will pass through untouched. Ask whether the mapping is right. A wrong
   mapping is fixed with `--map field="Their Column"`; a field they want left alone entirely
   is unmapped with `--map field=` (empty), which means the script never touches that column.
   - **No record ID column:** say so plainly before going further: importing the file would
     create new records instead of updating theirs. Offer to stop so they can re-export with
     the ID, or to continue and import it themselves with care.
3. **Which rows.** Only when the export has a create-date column, and genuinely a choice:
   *the whole file (a monthly pass)* · *only records created since a date (the weekly pass on
   new records)* · *since my last run (only when a previous run exists; offer it first then)*.
   A date scope still checks the whole file for duplicates, because a new record can duplicate
   an old one.
4. **Anything to leave alone.** "A field your team fills by hand, accounts not to touch, a
   value that looks wrong but isn't. Optional; say 'nothing' if there isn't anything." A field
   to leave alone becomes `--map field=`. Everything else goes into `inputs.md` verbatim for
   the auditor.
5. **Confirm before we run.** Re-run `profile` with the final options and play back its
   counts as a short list, **with the cap stated as a limit, not a footnote**:
   - format fixes: <n>
   - duplicates: <n> same-domain, <n> to check
   - rows missing industry, size, or headquarters: <flagged>
   - **enrichment cap: 24 rows per run, up to 3 lookups each. This run looks up <selected>;
     <queued> wait for the next run (newest records first).**
   Then: "Good to go, or anything to change?"

**The moment the builder approves**, set the expectation for the wait in one message: the
lookups run in parallel and take several minutes, so this is a good moment to switch tasks.
Then go quiet until the report.

## Set up the run

6. **The working folder:** `my-work/crm-cleanup/<YYYY-MM-DD>-<slug>/`, where the slug names
   the export (`sample-accounts`, `hubspot-accounts`). Dated on purpose: runs accumulate and
   are never overwritten. Run the profile into it:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/crm-cleanup/crm_csv.py" profile "<export path>" \
     --run "<absolute run folder>" [--since YYYY-MM-DD] [--map field="Column" ...]
   ```

   It writes `profile.json` and prints a summary. `{"ok": false}` means it stopped on purpose
   (no name or domain column, repeated record IDs, an empty file): tell the builder what it
   said, in plain words, and what would fix it.
7. **Write `inputs.md`** in the run folder: the export path, the confirmed column mapping, the
   scope, the builder's notes **verbatim**, and the profile's counts including the cap line.
   It is the record of what shaped the run and what the next run pre-fills from.

## Run the agents

Dispatch as ordinary subagents. Do not use agent-teams tooling; this runs identically in
every client.

8. **One `record-enricher` per batch, all in a single message so they run concurrently.**
   `profile.json` already holds the batches (`enrich_batches`, 8 rows each, at most 3: the
   cap). Each enricher gets the **absolute path** of `profile.json`, its batch number, and the
   run folder's absolute path, in the dispatch prompt itself. Each writes
   `enrich-batch-<n>.md`. Wait for all of them. If the profile found nothing to enrich, skip
   to step 10 with an empty `decisions.json` (`{"fills": [], "conflicts": [], "unresolved":
   [], "duplicates": [], "coverage": ""}`), and still dispatch the auditor first when there
   are duplicate candidates to rule on.
   - **The cap and the lookup bound are promises the change log repeats.** Never dispatch a
     batch the profile did not make, never raise the bound to chase a thin result.
9. **Dispatch `record-auditor`** with the run folder's absolute path. It reads `inputs.md`,
   `profile.json`, and every batch, with **no web tools and no new research**, and writes
   `decisions.json`.
10. **Build the file:**

    ```bash
    python3 "${CLAUDE_PLUGIN_ROOT}/skills/crm-cleanup/crm_csv.py" apply --run "<absolute run folder>"
    ```

    It writes `<export name>-cleaned.csv`, `change-log.md`, `change-log.html`, and
    `applied.json`, then re-reads the cleaned file and checks it against the original: the
    same header, the same rows in the same order, and no changed cell missing from the change
    log. If that check fails, it keeps nothing and says why: report it to the builder and
    stop. Never hand-edit the cleaned CSV to get past it.

## Publish the artifact

11. **Publish `change-log.html` as a Claude Artifact**, as written: the script rendered it
    from the same data as the CSV, so it cannot disagree with the file. Do not regenerate it
    by hand. If artifact publishing isn't available, don't block: say the change log is saved
    and give both paths.

    What the builder sees, so you can point at it: a masthead with the file name, the row
    counts, and **the enrichment cap on its own line**; counters for each section; chips that
    show one section at a time; then **Needs your call** (first, in the warm color: the only
    section that asks them to decide anything), **Duplicates to merge**, **Filled from public
    sources** (every value with its source link), **Format fixes**, **Could not resolve**, and
    **Queued for the next run**. It prints with every section showing.

## Finish

12. **Report**, briefly: the cleaned file's path and the change log's path; the one line that
    matters (how many empty cells were filled on how many rows, and how many items need their
    call); and **the cap line exactly as the change log states it**, including how many rows
    are queued. Don't reprint the change log.
13. **Needs your call.** If there are items, offer once: "Tell me which of these to apply, by
    row, and I'll rebuild the file with them." Write only the items they name to
    `corrections.json` in the run folder (`[{"row_id", "field", "value", "source_url"}]`,
    values from the change log's proposed value), and run `apply` again with
    `--corrections "<run folder>/corrections.json"`. The script applies only items that were
    listed as needing their call; anything else it refuses. Report what changed.
14. **Importing.** One short paragraph, no promises about screens: import the cleaned file as
    an **update to existing records, matched on the record ID**; merge the listed duplicates
    with the CRM's own merge tool first, because the file never deletes a row. Suggest they
    import a few rows first if they have never imported before.
15. **The rhythm, and the queue.** Weekly: run it on records created since the last run.
    Monthly: the whole file. When rows were queued, running again **on the cleaned file**
    looks them up first.
16. **Offer the depth, after the run, never before.** One beat: *"Want to see how this
    worked? A script did the exact part (formats, duplicates, the cap, writing the file) and
    two agents did the rest: one looked companies up, a few sources at a time, and one decided
    what of it belonged in your file. The connecting-your-data session explains working
    safely with exports like this one. Say 'teach me how this works'."*

## Honesty rules this skill carries

- **Every added value has a source, and the script refuses one that doesn't.** The change log
  shows the link beside the value.
- **Empty cells are filled; existing values are never overwritten by a lookup.** A difference
  is shown to the builder, who decides. Only `--corrections` changes an existing value, and
  only for items they named.
- **The cap is stated because it is a real limit.** 24 rows per run, 3 lookups each, newest
  records first. The intake states it, the change log states it, the artifact states it, the
  report states it.
- **A complete row is not looked up, so a wrong value in it is not caught.** The change log
  says so, with the count.
- **Annual revenue is never filled.** Public figures for private companies are estimates.
- **A row that can't be pinned to one company is named and skipped, never guessed.**
- **A name match alone never merges anything.** It is a possible duplicate for the builder to
  check.
- **The file never deletes or merges rows.** Merging is the CRM's job, with its history.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`crm_csv.py` owns the change log's section names** (Needs your call, Duplicates to merge,
  Filled from public sources, Format fixes, Could not resolve, Queued for the next run) and
  **the cap line**; step 11 describes them by name. It also owns the cap (`ENRICH_CAP = 24`),
  the lookup bound it states (`LOOKUPS_PER_ROW = 3`), and the batch size (`BATCH_SIZE = 8`).
  **The cap and the bound are stated in four places**: the script, this skill's step 5 and
  honesty rules, `agents/record-enricher.md`, and `curriculum/manifest.json`'s `one_liner`.
  Change one and change all four, or the builder is told something false.
- **`agents/record-enricher.md` owns the batch section names** (Found, Checked, Not found,
  Could not resolve, Coverage note) and the filename `enrich-batch-<n>.md`;
  `agents/record-auditor.md` reads them by name.
- **`agents/record-auditor.md` owns the `decisions.json` shape**; `crm_csv.py apply` reads it.
  Change the field names in one and the other drops decisions.
- **`evals/crm-cleanup/`** (repo root, not shipped) holds the sample's answer key and
  `grade.py`. A change to the sample file changes the key in the same pass.
- **`curriculum/manifest.json`** carries `title`, `one_liner`, `artifact`, `time_saved`, `team`,
  and `level`; keep them in step with the opening lines here.
- The working folder shape `my-work/crm-cleanup/<YYYY-MM-DD>-<slug>/` is what "since my last
  run" reads; `/bluerock:wrap-up` logs runs against the agent-team label **CRM Cleanup** with
  members `record-enricher` + `record-auditor`.
