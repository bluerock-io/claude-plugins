---
name: scorecard
description: >-
  Account Scorecard — point a small agent team at a company and get a fast,
  one-page scorecard (Fit, Timing, Reachability + a recommended next action). Use
  when I say "score <company>", "size up <company>", "should I go after
  <company>", "scorecard for <company>", or paste a company name and ask whether
  it's worth pursuing. Runs scout → scorer and writes the scorecard to
  my-work/account-scorecard/. Fast by design — the quick read, not a deep dossier.
---

Run the Account Scorecard team on a target company and produce the scorecard — a fast,
shareable one-pager. You orchestrate two agents; they do the work. This is the quick
read: keep it tight, aim for a couple of minutes, not a deep research run.

## First — anchor to the Hub

The scorecard, its working folder, and the `voice.md` / `objectives.md` the run reads
all live in the builder's Hub (the repo they cloned from the Starter). In an SSH/cloud
container the session usually starts in the **home folder**, with the Hub one level
down, named by the builder (`maria-hub`, `alex-hub` — don't assume a fixed name).
Identify it by signature, not name: run `ls`; see `CLAUDE.md` and `design/` side by
side? You're in the Hub. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the
**absolute path** with `pwd`, and use that full path throughout. Can't find it? Ask
where they cloned their Hub.

## Setup

1. **Get the target.** A company name (plus any hint — sector, region, domain — to
   disambiguate). If it's genuinely ambiguous, ask one question before spending the run.
2. **Make the working folder.** Slugify the name → `my-work/account-scorecard/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.

## Run the team, in order

3. **Dispatch `scout`** with the company (+ hint) and the working folder. It writes a
   quick, sourced `scan.md` (what they do, size/stage, recent signal). It's bounded to a
   handful of fetches — let it be fast. Wait for it.
4. **Dispatch `scorer`** with the same folder. It reads `scan.md` (plus `voice.md` /
   `objectives.md` from the Hub root if present), writes `scorecard.md`, and renders the
   one-page scorecard artifact.

## Finish

5. The **scorecard artifact** is the payoff — a clean, one-page view (company header,
   Fit / Timing / Reachability rated High/Med/Low with rationales, the "why now" line,
   and the recommended next action). The `scorecard.md` is the source of record the
   builder keeps and can push to their repo. If artifact publishing isn't available in
   my environment, don't block — the markdown is saved; say so and give the path.
6. **Report:** the scorecard path, the headline verdict (the strongest dimension and the
   why-now line), and the artifact (or the fallback note). Don't reprint the whole thing.

## Why this is the fast one

The Account Scorecard is deliberately lighter than a full dossier: two agents, a bounded
scan, a one-page output. It's the "is this worth my time, and what do I do next" read.
For the deep, multi-section dossier, that's the Account Research team (`researcher →
signal-scanner → composer`) the builder has in their own Hub.
