# Session 1 — checkpoint verification spec

How to verify each checkpoint by looking. Two kinds of evidence here:

- **Inspectable** — a state you can check from this session with a command.
  Always prefer it; it is the only evidence that can mark a checkpoint passed
  on its own.
- **Reported** — a state that lives off this machine (a browser tab, the
  Connector app, the Console). You can't inspect it, so ask what the builder
  *sees* (never "did it work?") and treat the description as provisional:
  the checkpoint truly passes when its nearest inspectable consequence appears
  downstream. Note which checkpoint that is.

Run inspection commands quietly; the builder should see conclusions, not
plumbing.

**Three checkpoints, both surfaces.** The tracks reach them through a different
number of steps — two on Claude Desktop, three on Cursor — but they pass the
same three states, so a builder who switches surfaces mid-session is not
re-numbered. Realigned to the live page 2026-08-18, when the starter-kit copy,
the clone, and the plugin install left this session; the old checkpoints 5, 6,
and 7 verified those and are gone with them.

## Checkpoint 1 — the Connector is set up

- **Reported:** Desktop — the Connector app shows a success message in its log
  after the browser sign-in, so it is signed in to BlueRock and knows their
  workspace. Cursor — the BlueRock Connector extension shows installed in the
  Extensions panel.
- **Inspectable consequence:** checkpoint 2. A connection cannot exist without
  this, so a session running inside the workspace passes this by definition.

## Checkpoint 2 — the AI tool is connected to the workspace

- **Inspectable:** this conversation running inside the workspace IS the
  evidence. Signs you are: `ls ~/.bluerock` succeeds (the workspace facts
  folder), and the home folder matches the workspace shape rather than a
  personal machine.
- **Reported, as the builder's own confirmation:** Desktop — the header shows
  the **BlueRock Sandbox** host and the `my-workspace` folder. Cursor — a second
  Cursor window is attached to the workspace with a Claude Code panel open.
- If this session is on the builder's own machine instead, this checkpoint
  cannot pass yet; hand off to the connected window ("say *continue the course*
  there").
- On pass, once you are inside the workspace: create `learning/` and
  `progress.json` at the project root if they don't exist. Never overwrite an
  existing one.

## Checkpoint 3 — /bluerock:check reports live

- **The builder runs the check; you observe it in-conversation.** Pass when the
  check's report lands with its all-clear (the locked word is **live**) and
  names the project folder.
- **Inspect the same signals yourself** rather than trusting the transcript
  from memory: the project is present with its signature files (`CLAUDE.md` and
  `design/` side by side), and `python3 --version` and `git --version` succeed.
- **Never use a partial slash command as a substitute test.** `/blue` and
  `/bluerock` both return `Unknown command` in Claude Desktop, which told a real
  builder three times that she had failed. The only proof is `/bluerock:check`
  itself.
- If the check can't find the project, the builder is in the wrong window —
  that is checkpoint 2 failing, not 3. Reconnect (Cursor: reattach from the
  Connector) and run the check again rather than re-running it hopefully.

## Marking progress

After each verified checkpoint N (once you are inside the workspace):
`sessions["1"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 3, `{ "status": "complete", "completed": "<today>", "artifact":
"<what they set up, concretely>" }`. Write valid JSON; never delete history.
