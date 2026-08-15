# Session 4 — checkpoint verification spec

Everything in this session lands in files, so every checkpoint is inspectable.
Run inspection commands quietly; the builder sees conclusions, not plumbing.

**The trap in this session: all three files already exist.** A fresh
`hub-starter` clone ships `CLAUDE.md`, `voice.md`, and `objectives.md`. The last
two are seeded with `[bracketed]` placeholders; `CLAUDE.md` ships as a filled
skeleton with named empty sections. So **file existence proves nothing here** —
every checkpoint below reads content. `<project>` is the project's absolute
path.

## Checkpoint 1 — three memory files, filled with their real context

- **Inspectable:** all three exist at the project root, and each one carries
  real content in place of the seed:
  - `voice.md` — the seeded headings (`## Tone`, `## Words and moves I avoid`,
    `## Phrasings that sound like me`) now hold sentences instead of
    `[e.g., ...]` placeholders. **The fastest check is for the placeholders:**
    a `[` at the start of a line under those headings means that section is
    still seed.
  - `objectives.md` — `## This quarter` names real goals, not `[Goal 1 —
    specific enough...]`.
  - `CLAUDE.md` — the **Who I am** section describes a real person and role.
    It also still has its session-start greeting block: onboard is told to fill
    seeded sections in place and keep everything else, so **a missing greeting
    block means onboard overwrote the file** rather than filling it. Flag that
    and restore it from the starter kit before passing.
- **Also check location.** A `CLAUDE.md` or `voice.md` sitting in the *home*
  folder rather than the project is the known failure: onboard wrote to a bare
  relative path. Move them into the project before passing.
- A partially-filled set fails honestly: name which file is still seed and have
  them re-run onboard with more to go on. Do not fill it in for them — invented
  context sets the ceiling for every session after this one.
- **Reconcile `role` here** if it is unset: read `CLAUDE.md`'s "Who I am," map
  it to `sales` / `marketing` / `operations`, confirm in one line, store it in
  `progress.json`. Never a second copy of the field.

## Checkpoint 2 — voice.md sharpened with a real rule and a real quote

- **Inspectable:** compared with checkpoint 1's state, `voice.md` has gained
  **both**:
  1. a concrete entry in the avoid-list — a specific word, opener, or move
     (`"delighted"`, `"I hope this finds you well"`, exclamation points), not a
     category like "corporate language";
  2. at least one quoted phrasing under the phrasings heading that reads like
     something a person actually wrote, not a generic sample.
- **The judgment call, stated plainly:** you are checking specificity, not
  quality. "No jargon" is too vague to pass. `No "circle back"` passes. If you
  can't tell whether a phrasing is really theirs, ask "is that a line you've
  actually written?" — one question, and take the answer.
- Half of it fails: if they added an avoid-rule but no phrasing (the common
  case), say which half is missing and get it before passing.

## Checkpoint 3 — a clean draft, traced back to the file

- **Observed in-conversation, and the source matters more than the draft.** The
  two-line draft must come from a context that has **not** read this
  conversation — either a subagent dispatched from here, or a brand-new chat
  the builder ran it in. A draft written directly in this conversation
  **cannot pass this checkpoint**: this chat holds their interview answers and
  writing samples, so it would sound like them whether or not `voice.md` works.
  That is the whole point of the step; do not let it slide to be agreeable.
- **Pass spec:** a two-line draft exists, it contains none of the words on
  their avoid-list, and the builder can point at the line in `voice.md` that
  shaped it. Their pointing is part of the checkpoint — the connection is the
  lesson.
- **A draft that fails the voice test is not a failed checkpoint yet.** It is
  the intended teaching moment: the fix is in the file, not the prompt. Have
  them add the words it reached for, re-run, and pass on the second draft. A
  builder who watched one edit change the output has learned more than one who
  passed first try.
- If they went to a new chat, mark `{ "status": "in_progress", "checkpoint": 2 }`
  **before** they leave, so the session resumes cleanly if they don't come
  straight back.

## Checkpoint 4 — saved

**The save runs through wrap-up** (step 4), not through a separate ask. Verify
the result, never the mechanism — and keep the builder-facing words to "saved"
and "backed up."

- **Inspectable:** `git -C <project> log -1 --stat` shows a recent commit
  touching the three files, or `git -C <project> status --short` shows them no
  longer modified. Either is fine. Run it quietly; the builder sees the
  conclusion, not the plumbing.
- **No remote is a full pass, and say nothing about it.** A local save is the
  finished state on newer workspaces. Do not mention pushing, backup, or GitHub
  — wrap-up is deliberately silent here, and raising it invents a problem the
  builder does not have.
- **A blocked push still passes.** If the save landed locally but the backup
  failed on credentials, pass on the local save, say plainly that the files are
  safe and the backup can be set up later, and don't teach git here.
- **An identity prompt is not a failure.** A fresh workspace has no git identity
  configured, so wrap-up asks for a name and email to label the save. That is
  the expected first-save exchange. Let wrap-up run it; never pre-empt it with
  `git config` of your own, and never let the save fail first to surface it.
- If nothing was saved at all, that fails — but offer the one-line fix
  ("wrap up my session") rather than sending them away.

## Marking progress

After each verified checkpoint N:
`sessions["4"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 4, `{ "status": "complete", "completed": "<today>", "artifact":
"three memory files, with a voice guide that caught '<their avoid word>'" }`.
Write valid JSON; never delete history. Never mark a checkpoint you didn't
verify — honest state beats a green dashboard.
