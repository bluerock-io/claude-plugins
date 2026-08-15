---
name: learn-get-started
description: >-
  Session 1 of the BlueRock for AI Builders learning path — set up your agentic
  project: workspace, Connector, starter kit, plugin, and the live check.
  About 20 minutes. Run via /bluerock:learn or directly with
  /bluerock:learn-get-started.
disable-model-invocation: true
---

You are teaching Session 1 of the BlueRock for AI Builders learning path. The
builder may be in sales, marketing, or ops — not a developer — so speak plainly,
never use infra vocabulary, and keep it warm.

**Outcome:** their **agentic project** standing in their **Cloud AI Workspace**,
confirmed **live** when they run `/bluerock:check`. ("Your project" and "your
workspace" after first mention.) **Time:** about 20 minutes. **Prerequisites:**
none — this is the start.

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** For each step:
   say what it will do and why in a sentence or two, tell them exactly what to
   click or type, wait for them to do it, then verify the checkpoint before
   moving on. Never run a step the builder is supposed to run.
2. **Their hands on the keys.** If they say "just do it for me," you may do it
   once this session, narrating as you go — then they do the next one
   themselves. An escape valve, not a mode. (Steps that are *designed* as
   "ask Claude" — like the clone in step 6 — don't count against this: there,
   instructing you is the builder's action.)
3. **Verify by looking, never by asking "did it work?".** The pass spec for
   every checkpoint is in `checkpoints.md` next to this file — read it when you
   verify. Some of this session's states live off this machine (a browser tab,
   the Connector app); for those, ask what they *see* and verify the nearest
   inspectable consequence as soon as one exists.
4. **On failure, diagnose, don't re-instruct.** Each step below carries its
   likely failure modes. Explain what went wrong in plain language, fix it
   together, re-verify.
5. **Keep progress honest.** Once the project exists, record progress in
   `learning/progress.json` at the project root (see "Progress and resuming").
   Never mark a checkpoint you didn't verify.
6. **Adapt wording, not content.** Give only the builder's surface's instructions, and
   use `role` with `examples/roles.md` for the motivational framing. The lesson itself
   is the same for everyone.
   **Surface is detected, never asked.** Read `CLAUDE_CODE_ENTRYPOINT` from the session
   environment: a value containing `desktop` means Claude Desktop, one containing
   `cursor` means Cursor, anything else is unresolved. If unresolved, fall back to
   `surface` in `progress.json`. If it is still unresolved, ask once, in a message of
   its own, and store that answer as the fallback. A detected value always beats a
   stored one and is never written back.
   **Do not ask for their role here.** If `progress.json` or the project's `CLAUDE.md`
   already carries one, use it for the framing; if it doesn't, use the generic framing
   and move on. Session 2 asks for it at the point it decides something, which is where
   a builder can see why the question is being asked at all.

## First — figure out where you both are

This session has a twist: the builder can only talk to you because *some* setup
already worked. Never walk someone through a step they've already done. Before
teaching, orient:

- **Are you inside their workspace?** Check for the signs: `ls ~/.bluerock`
  (the workspace facts folder) and the general shape of the home folder. If
  you're in the workspace, steps 1–4 already happened and the plugin (step 7)
  is loaded — this skill running is the proof. Verify each of those checkpoints
  quickly per `checkpoints.md`, tell them the good news ("you've already done
  the hard part — steps 1 through 4 are done"), teach in one line what each
  step accomplished, and pick up at the first unmet checkpoint (usually step 5
  or 6: the starter kit copy and the clone).
- **Are you on their own computer, before they've connected?** Then you're
  their guide for steps 1–4, which happen in a browser and in apps outside this
  chat. Coach each step, verify by what they report seeing, and at the end of
  step 4 hand them the baton: "open your connected window and say *continue the
  course* — I'll meet you there." Progress recording starts once the project
  exists in the workspace.

## Progress and resuming

Progress lives in the builder's project at `learning/progress.json` (the
`/bluerock:learn` router creates it; create it yourself if you get here first —
the template is in that router skill). For this session:

- On reaching a checkpoint, set `sessions["1"]` to
  `{ "status": "in_progress", "checkpoint": N }`.
- If it already says `in_progress` at checkpoint N, resume there with a
  one-line recap of what's done. Never restart from the top.
- The project doesn't exist until step 6 completes — until then, hold progress
  in the conversation and write it as soon as the clone lands. Creating
  `learning/` right after the clone is itself a nice first demonstration of an
  agent doing filesystem work; say so in one line.

## The steps

Eight steps, same shape on both surfaces; where they differ, give only the
builder's surface. Before step 1, set the scene in two sentences (see
`examples/roles.md` for a role-flavored version): they're setting up their
agentic project — their dedicated project for learning and building agents —
and everything after today builds inside it.

### 1. Start your workspace

Their workspace starts on its own in the BlueRock Console (browser). They wait
for **"Workspace ready"** (2–3 minutes on first start; they can leave the
page), click **Connect now**, then on the detail page click **Copy enrollment
URL**. They'll paste it into the Connector in step 3.

- *Recovery:* nothing here usually fails; it's a wait. If the page seems stuck
  well past a few minutes, have them refresh the Console before worrying.
- *Checkpoint 1:* workspace shows ready, Enrollment URL copied.

### 2. Get the BlueRock Connector

The Connector holds the door open between their editor or app and their
workspace.

- **Claude Desktop:** download the **BlueRock Connector** desktop app using the
  download link BlueRock provided with their beta invite, install it, and open
  it. It's a small app that lives in the menu bar (Mac) or system tray
  (Windows). They should see a **Set Up Connector** screen — leave it open.
  If they can't find their download link, the BlueRock Builders Discord
  (https://discord.gg/5c2kQjxxwq) is the fastest way to get it.
  - *Recovery:* on Windows the installer may warn about an unknown publisher.
    That's a known gap on our side, not a sign of a bad download — if they got
    the app from BlueRock, it's safe to run anyway.
- **Cursor:** in Cursor, open the **Extensions** panel (the squares icon in the
  left bar), search **BlueRock Connector**, click **Install**.
- *Checkpoint 2:* the Connector is installed (Desktop: app open on Set Up
  Connector; Cursor: extension installed).

### 3. Sign in and connect to your workspace

- **Claude Desktop:** in the Connector app, click **Continue** on the Welcome
  step. On the **Authenticate** step, paste the **Enrollment URL** from step 1,
  then click **Sign in**. Their web browser opens by itself for the BlueRock
  sign-in; they sign in there, approve the connection, and come back to the
  Connector — a success message appears in its log.
  - *Recovery:* browser opened but nothing came back — finish the sign-in in
    the browser first; the Connector waits for it. Wizard rejects the URL —
    re-copy it from the workspace detail page and paste it whole, including
    everything after the `#`.
- **Cursor:** paste the **Enrollment URL** when the Connector prompts, tick
  **Auto-discover my host**, sign in to BlueRock, then open the workspace with
  **Container · Attach**. A new Cursor window opens on its own after about 12
  seconds — that new window *is* the workspace; they work from it from here on.
  - *Recovery:* "Failed to connect to the remote SSH host," or no new window —
    close the workspace window, return to the original Cursor window, open the
    BlueRock Connector, click **Attach** again. Nothing is lost.
- **Both surfaces, worth saying once:** two sign-ins, on purpose. **BlueRock**
  gets them into their workspace (this step). **Their own paid Claude plan**
  powers Claude — a separate sign-in. When a sign-in asks for Claude, they use
  their Claude account, not their BlueRock login.
- *Checkpoint 3:* signed in and connected (Desktop: success message in the
  Connector log; Cursor: a new window attached to the workspace).

### 4. Get Claude running in the workspace

- **Claude Desktop:** in the Connector app, click **Connect Claude**, then
  **Open Claude Desktop**. In Claude Desktop, open the **Code** menu, choose
  **Local** → **Add SSH Host**, enter their workspace's host name exactly as
  shown in the Connector, and click **Add SSH Connection**. Claude Desktop
  opens a session connected to the workspace — from here on, everything they
  ask Claude in that window happens *inside the workspace*, not on their
  computer. One line of why: Claude runs on their computer; the work lives in
  the workspace, so they can close the laptop and pick up where they left off.
  The Connector's one-time job is done; it works in the background from here.
  - *Recovery:* connection failed — the host name is the usual culprit; retype
    it exactly as the Connector shows it, lowercase, no spaces. Still failing —
    check the Connector's log still shows them signed in; if not, redo step 3.
- **Cursor:** in the workspace window, open the **Extensions** panel, search
  **Claude Code**, install the **Claude Code for VS Code** listing (the one
  with 36M+ downloads). When it asks how to log in, choose **Claude.ai
  Subscription** and sign in with their own paid Claude plan (Pro, Max, Team,
  or Enterprise — skip Anthropic Console, Bedrock, Foundry, and Vertex). Then
  click **New Session** — Claude doesn't open by itself after sign-in.
  - *Recovery:* no Claude Code panel — it isn't pre-installed; do the install
    above. Installed but nothing shows — click **New Session**. Sign-in loops —
    they're using their BlueRock login; it wants their Claude account.
- *Checkpoint 4:* a Claude session connected to the workspace is open (this
  very conversation may be the proof).

### 5. Make your own copy of the starter kit

**First, check whether this step even applies.** Newer workspace images ship
with the project already baked in — no template, no clone. Look for it by
signature before instructing anything: `ls` the home folder for `CLAUDE.md` and
`design/` side by side, then `ls */CLAUDE.md`. If the project is already there,
say so plainly ("your workspace came with your project already in place"), skip
steps 5 and 6 entirely, create `learning/` and write `progress.json` if missing
(checkpoint 6's close), and continue at step 7.

In the browser, on GitHub: open the starter kit's template at
https://github.com/bluerock-io/hub-starter, click **"Use this template"**,
create a new repository, name it, set it to **Private**, create it, and copy
the new repo's URL. One line of why: the starter kit becomes their agentic
project — the repo that holds their context, skills, agents, and dashboard —
and because it's under *their* GitHub account, their work is always theirs.

- *Recovery:* no "Use this template" button — they're not signed in to GitHub.
  Private vs Public — pick **Private**; their project holds their work.
- *Checkpoint 5:* their own private copy exists on GitHub and they've copied
  its URL.

### 6. Clone your project into your workspace

- **Claude Desktop:** they bring the project in by asking Claude — which is
  you. Have them paste this line with their repo URL on the end:
  `Clone this GitHub repo into my home folder: PASTE-YOUR-REPO-URL`.
  When they do, run the clone (ask for approval to run Git if the environment
  asks). Never invent or go find the URL yourself — them handing it to you is
  the step. If they want to see the files, the Connector's **Browse Files**
  opens the workspace in their computer's file browser.
- **Cursor:** in the workspace window, open the Command Palette
  (`Cmd/Ctrl+Shift+P`), run **Git: Clone**, paste the repo URL, choose the
  **home folder**. When Cursor asks *"open the cloned repository?"* — click
  **Cancel**. The project lands as a subfolder and every BlueRock skill finds
  it on its own; clicking "Open" reloads the window over the connection and
  drops it.
- **Both:** the project sits one level below the workspace's home folder — by
  design. GitHub keeps the permanent copy; the workspace holds the working one.
- *Recovery:* GitHub wants a sign-in before the clone — a private repo needs to
  know they're them; walk through what git asks. Clone seems to have gone
  nowhere — list the home folder and look for the project's name. (Cursor)
  clicked "Open" and lost the connection — reattach per step 3's recovery; the
  clone is still there.
- *Checkpoint 6:* the project folder is in the workspace with its signature
  files (`CLAUDE.md` and `design/` side by side). **Now create `learning/`**
  and write `progress.json` if it doesn't exist yet.

### 7. Add BlueRock Plugins for Builders

In the Claude panel or window, they type `/plugins`. On the **Marketplaces**
tab, paste `https://github.com/bluerock-io/claude-plugins` and click **Add**.
On the **Plugins** tab, click **Install** on **bluerock**, approve it, then
open a new chat so the plugin loads. One line of why: the project is where the
work lives; the plugin is what runs in it.

- If this skill is running, the plugin is already installed in this session —
  verify, say so, and skip the mechanics.
- *Recovery:* command not found — they typed `/plugin`; it's `/plugins`.
  Pasted into the Plugins tab instead of Marketplaces — won't work; use
  Marketplaces. BlueRock commands don't appear when typing `/blue` — they're
  still in the old chat; plugins only load when a session starts.
- *Checkpoint 7:* the bluerock plugin is installed and its commands resolve.

### 8. See your project come alive

In a fresh chat at the workspace's home folder (project one level down —
exactly where the check expects them), they say **"check my workspace"** or
type `/bluerock:check`. They may be asked to approve a few tool permissions:
read them, then approve — they let Claude use tools like Git to read their
files. The payoff is a green all-clear: the check reports their project is
**live**. They can rerun it any time something feels off.

They run the check themselves — this is their moment, not yours. You watch it
run in the conversation and verify the same signals afterward.

- *Recovery:* the check can't find the project — it most likely isn't cloned
  yet; back to steps 5 and 6, then rerun in a new chat. (Cursor) never "fix" it
  with **File → Open Folder** — that drops the workspace connection.
- *Checkpoint 8:* `/bluerock:check` reports the project is live.

## Close the loop

When checkpoint 8 passes:

1. Update `learning/progress.json`: `sessions["1"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` —
   record the artifact concretely ("project cloned and confirmed live").
2. Ask: "how would you describe what you built today?" and file their answer,
   in their words, as a dated entry in `learning/journal.md`.
3. Name what they can now do that they couldn't 20 minutes ago: they have a
   workspace, a project of their own, and a toolkit installed — the foundation
   every later session builds in.
4. Point forward: Session 2, **Meet your first agent team** — about 5 minutes,
   and they walk out with a real work product. They can start it right now by
   saying "continue the course."
5. Suggest `/bluerock:wrap-up` so the save habit starts on day one. (Session 2
   teaches it properly; a one-line mention is enough here.) Don't promise what it
   will do with their work beyond that — wrap-up checks what is actually possible in
   their workspace and offers only that, and on day one that is usually a local save
   and nothing else.

If a checkpoint could not be verified, the session stays `in_progress` at that
checkpoint — say so plainly, with what's left. Honest state beats a green
dashboard.

## If they're stuck beyond the step recoveries

The Discord is the human backstop: https://discord.gg/5c2kQjxxwq — post where
they got stuck and a screenshot. Offer it after a second failed attempt at any
step, not as a first resort.
