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

## Checkpoint 1 — workspace ready, Enrollment URL copied

- **Reported:** the Console shows "Workspace ready" and they clicked Copy
  enrollment URL. Ask what the workspace page shows.
- **Inspectable consequence:** none until checkpoint 3/4 (a connected session
  existing proves the workspace runs). If you are already running inside the
  workspace, this checkpoint passed by definition.

## Checkpoint 2 — Connector installed

- **Reported:** Desktop — the Connector app is open on "Set Up Connector."
  Cursor — the BlueRock Connector extension shows installed.
- **Inspectable consequence:** checkpoint 3's connection succeeding.

## Checkpoint 3 — signed in and connected

- **Reported:** Desktop — a success message in the Connector app's log after
  the browser sign-in. Cursor — a new Cursor window opened, attached to the
  workspace.
- **Inspectable:** if this session is running inside the workspace, pass. Signs
  you are: `ls ~/.bluerock` succeeds (workspace facts folder), and the home
  folder matches the workspace shape rather than a personal machine.

## Checkpoint 4 — a Claude session connected to the workspace

- **Inspectable:** this conversation running inside the workspace IS the
  evidence — same check as above (`ls ~/.bluerock`, home-folder shape). If this
  session is on the builder's own machine instead, this checkpoint cannot pass
  yet; hand off to the connected window ("say *continue the course* there").

## Checkpoint 5 — private starter kit copy on GitHub, URL copied

- **Reported:** they created the repo and copied its URL. The URL they paste in
  step 6 is the evidence — it should be `github.com/<their-account>/<their-name>`,
  not `bluerock-io/hub-starter`. If they paste the template's own URL, they
  skipped the copy: back to step 5.
- **Inspectable consequence:** after the clone, `git -C <project> remote -v`
  shows their repo, not the template.

## Checkpoint 6 — project cloned into the workspace

- **Inspectable, fully.** From the home folder: `ls */CLAUDE.md` finds the
  project; inside it, `CLAUDE.md` and `design/` sit side by side (the
  signature; `design/dashboard.html` present). `git -C <project> remote -v`
  points at the builder's own GitHub repo.
- On pass: create `learning/` and `progress.json` at the project root if they
  don't exist. Never overwrite an existing one.

## Checkpoint 7 — plugin installed and loading

- **Inspectable, trivially:** this skill came from the plugin, so the plugin is
  installed and loaded in this session. Pass and say so.
- Only if teaching from *outside* a plugin-loaded session (rare): reported —
  ask what appears when they type `/blue` in a new chat; the BlueRock commands
  listing is the evidence.

## Checkpoint 8 — /bluerock:check reports live

- **The builder runs the check; you observe it in-conversation.** Pass when the
  check's report lands with its all-clear (the locked word is **live**) and
  names the project folder.
- **Inspect the same signals yourself** rather than trusting the transcript
  from memory: project present with signature files, plugin loaded, `python3
  --version` and `git --version` succeed.
- If the check reports the project isn't there, that's checkpoint 6 failing,
  not 8 — go back rather than re-running the check hopefully.

## Marking progress

After each verified checkpoint N (once the project exists):
`sessions["1"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 8, `{ "status": "complete", "completed": "<today>", "artifact":
"<what they built, concretely>" }`. Write valid JSON; never delete history.
