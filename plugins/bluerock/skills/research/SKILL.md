---
name: research
description: >-
  Account Research — point an agent team at a target company and get a sourced
  dossier. Use when I say "research <company>", "account research on <company>",
  "build a dossier on <company>", "what's the angle on <company>", or paste a
  company name/domain and ask for research. Runs researcher → signal-scanner →
  composer and writes the dossier to my-work/account-research/.
---

Run the Account Research team on a target company and produce the dossier — the
shareable artifact. You orchestrate three agents; they do the work.

## First — anchor to the Hub

The dossier, its working folder, and the `voice.md` / `objectives.md` the run reads all
live in the builder's Hub — the repo they cloned from the starter. In an SSH/cloud
container the session usually starts in the **home folder**, with the Hub one level
down. The builder named it when they cloned (`maria-hub`, `alex-hub` — don't assume a
fixed name like `hub-starter`); identify it by its signature, not its name. Before you
start: run `ls`. See `CLAUDE.md` and `design/` side by side? You're in the Hub. If not,
find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` into that folder, capture its
**absolute path** with `pwd`, and use that full path for the working folder and the
files you read (e.g. `/home/you/maria-hub/my-work/…`). Can't find it? Ask the builder
where they cloned their Hub. Working outside it means the dossier lands where they can't
find it and the voice tuning silently skips.

## Setup

1. **Get the target.** A company name (and any hint — sector, region, or domain —
   to disambiguate). If it's ambiguous and you can't tell which company, ask one
   question before spending a run.
2. **Make the working folder.** Slugify the name → `my-work/account-research/<slug>/`.
   Create it. Everything for this run lives here; `my-work/` is builder-owned and
   never overwritten.

## Run the team, in order

3. **Dispatch `researcher`** with the company (+ hint) and the working folder.
   It writes `profile.md` (who they are, sourced). Wait for it.
4. **Dispatch `signal-scanner`** with the same folder. It reads `profile.md` and
   writes `signals.md` (recent, dated, sourced signals). Wait for it.
5. **Dispatch `composer`** with the folder. It reads `profile.md` + `signals.md`,
   plus `voice.md` + `objectives.md` from the project root if present, and writes
   the dossier `<slug>.md` (overview → signals → strategic angles, in my voice).

## Finish

6. **Report:** the dossier path, the one-line best angle the composer surfaced, and
   offer to open it. Don't reprint the whole dossier.

## Rules

- **One company per run.** Don't let a run sprawl across companies.
- **Honest sourcing.** This is public-web research (the agents use WebSearch /
  WebFetch), not a paid data feed — the dossier cites sources and marks gaps. Say
  so if a section came back thin; never present guesses as findings.
- **Tune to me.** If `voice.md` / `objectives.md` exist, the dossier should sound
  like me and rank angles by what I actually care about. If they don't, run anyway
  and suggest running `/bluerock:onboard` to make the next one sharper.
- If `researcher` or `signal-scanner` returns almost nothing (private company, no
  public footprint), tell me plainly rather than padding the dossier.
