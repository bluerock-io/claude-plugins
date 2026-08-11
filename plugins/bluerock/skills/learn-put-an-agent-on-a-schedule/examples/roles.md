# Session 7 — role example blocks

The lesson is identical for everyone: pick a job that repeats on a clock, write
the two-sentence instruction, check the fallback, create the routine, fire it by
hand. Role changes which job and cadence to suggest.

Read `role` from `learning/progress.json` (`sales`, `marketing`, `operations`);
if unset, use the neutral block.

**`daily-brew` on weekday mornings is the right default for every role**, and it's
what the shipped command schedules. The alternatives below are for a builder whose
real repeated dispatch is something else — which is the better outcome when they
have one, because they'll actually read the output.

## sales

- **Default:** `daily-brew` every weekday at 7am. A sales day that starts with
  yesterday's commitments closed is the clearest version of this session's promise.
- **Alternative jobs that genuinely repeat on a clock:** a Monday morning pipeline
  brief; pre-call prep for the day's calendar; a Friday summary of what moved and
  what stalled.
- **Cadence note:** weekdays, not daily. A brief that lands Saturday at 7am is the
  first thing they'll resent, and it's the exact case the step 5 read-back catches.
- **Destination to suggest:** `briefs/<today's date>.md`.
- **The "stays ad hoc" case:** account research. It repeats often but only when a
  new account appears, so it stays a manual dispatch. Good example to name — it
  makes the on-a-clock test concrete.

## marketing

- **Default:** `daily-brew` every weekday at 7am.
- **Alternative jobs that genuinely repeat on a clock:** a **weekly competitive
  sweep** — the classic, and it composes with the team they shipped in Session 6;
  a Monday content-calendar check; a monthly performance-recap draft.
- **Cadence note:** the weekly sweep wants a day and time they'll actually read
  it — Monday morning beats Friday afternoon. And weekly means the destination
  needs a dated filename, or each run overwrites the last.
- **Destination to suggest:** `my-work/sweeps/<date>.md` for the sweep,
  `briefs/<today's date>.md` for the brief.
- **The "stays ad hoc" case:** drafting a campaign asset. It repeats, but on
  campaigns, not on a clock.

## operations

- **Default:** `daily-brew` every weekday at 7am.
- **Alternative jobs that genuinely repeat on a clock:** a Monday status roll-up
  from the week's filed notes; a monthly report draft; a weekly check that
  recurring work actually got done.
- **Cadence note:** ops builders tend to want monthly as well as daily, and
  monthly is where the dated-filename discipline matters most — a monthly job that
  overwrites its own file loses eleven months of record.
- **Destination to suggest:** `briefs/<today's date>.md`, or
  `reports/<year>-<month>.md` for the monthly.
- **The "stays ad hoc" case:** incident or escalation summaries. They're
  triggered by events, so they stay manual — and this is usually the role that
  spots the distinction fastest. (Revenue and marketing ops: same block, adapt in
  one line.)

## neutral (role unset)

- **Default:** `daily-brew` every weekday at 7am, exactly as the shipped command
  reads.
- **Alternative jobs:** anything they already dispatch at roughly the same time
  each day or week.
- **Cadence note:** weekdays is almost always the right first choice. Ask what
  they want to be true when they sit down.
- **Destination to suggest:** `briefs/<today's date>.md`.
- **The "stays ad hoc" case:** anything they dispatch *because something
  happened*. If the trigger is an event rather than a time, it stays manual — and
  recognizing that is half of what this session teaches.
