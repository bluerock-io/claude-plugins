---
name: today
description: >-
  My living priorities for the day. Show, add, reorder, or check off what's
  in today.md. Use when I say "what's on today", "today", "add to today",
  "mark that done", "what's left", or "show my priorities".
---

`today.md` is my living priority list — daily-brew seeds it each morning, I
work against it, capture adds to it, and wrap-up tallies what closed. You keep
it current and show it back clearly.

## First — anchor to the project

`today.md` lives in the builder's project. Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an
SSH/cloud container the chat may start in the project itself or in the **home folder**
with the project one level down — both are normal.
Before reading or writing: run `ls`. See `CLAUDE.md` and `design/` side by side? You're
in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` into that folder, capture its
**absolute path** with `pwd`, and read/write `today.md` at that full path
(e.g. `/home/you/maria-hub/today.md`) — never a bare `today.md`, so you don't create a
stray one in the home folder. Can't find it at all? Ask the builder which folder their
project is in.

## The file

`today.md` at the project root. If it doesn't exist, create it from the shape
below — scannable and typed enough to count:

```
# Today — YYYY-MM-DD

## Focus
- [ ] Verb + named object        (open)
- [x] Verb + named object        (done)
- [>] Verb + named object        (carried from a prior day)

## Decisions waiting
- Who's waiting, on what, by when
```

## What I'll ask you to do

- **Show:** print Focus with state, open items first, then one line — how many open vs. done today.
- **Add:** append a new `[ ]` item to Focus (or a line under Decisions). Keep my wording; rank by leverage if I don't say where.
- **Check off:** flip `[ ]` → `[x]` for the item I name (match loosely on the text).
- **Carry over:** at the start of a new day, open items become `[>]` under the new date. daily-brew normally does this; do it if I ask.

## Rules

- One file, edit in place — never lose what I set.
- Keep it short: Focus is a top list, not a backlog dump.
- Plain English. Don't moralize about unfinished items.
