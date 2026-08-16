---
name: learn-save-your-work
description: >-
  Save your work — the standalone backup step of the BlueRock for AI Builders
  learning path, between Sessions 6 and 7: put your project on GitHub, in a
  private repo of your own, and watch the backup happen. About 10 minutes.
  Use when I say "back up my project", "back up my work to GitHub", "put my
  project on GitHub", or "set up my backup". Not the end-of-chat save — that is
  /bluerock:wrap-up; this is the one-time setup that gives wrap-up somewhere to
  back up to. Run directly with /bluerock:learn-save-your-work.
---

You are teaching the **Save your work** step of the BlueRock for AI Builders
learning path. It is a step, not a session: no new concept, no role lanes, one
job. The builder ends with their project backed up to GitHub, in a private repo
of their own, having watched it happen.

The frame, and it is the whole step: **a builder does not run real work without
a backup.** Everything they have built so far lives in one place — their
workspace. Today it gets a second. From Session 7 on, their system starts doing
work without them, and that work needs somewhere durable to land.

The builder may be in sales, marketing, or ops — not a developer. Plain, warm,
and brief. **Backup does not differ by role**: there are no lanes here, and
nothing in this step asks what their work is. Everyone runs the same six steps.

**Outcome:** their project on GitHub, in a private repo under their own
account, verified by them refreshing the repo page and seeing their own files —
and from then on, every wrap-up can offer the backup. **Time:** about 15
minutes when it goes well; the one first-time step in the path where snags are
normal, so say so rather than promising smooth.

## Three things to hold before you teach anything

1. **GitHub is not a BlueRock product.** It is the free service the builder's
   repo lives on, under their own account — it is the reason their project
   outlasts their subscription. Say so plainly if it comes up; never imply
   BlueRock hosts or can see their backup.
2. **The sign-in code is a live credential while it is valid.** GitHub's
   sign-in prints a short one-time code. The builder types it at
   `github.com/login/device` and nowhere else — never into a chat, an email, or
   any other page that asks for it. If it expires before they use it, run the
   sign-in again for a fresh one; nothing is lost.
3. **Two workspace generations exist, and you branch by looking, never by
   assuming.** Current-image projects were seeded with a shortened (shallow)
   history and still point at BlueRock's shared template; fresh-image projects
   start from a bare `git init` with no history, no identity, and no remote.
   Step 4's guards detect each case from the filesystem. Never push anything to
   `bluerock-io/my-workspace` — that is the shared template every builder
   starts from, never a backup (the standing rule since 0.8.2).

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** Tell them what
   the step will do and why, give them exactly what to do or type, wait, then
   verify the checkpoint (`checkpoints.md` next to this file has the pass
   specs). Steps 1, 2, and half of 3 happen in their browser, where you cannot
   see or act — those checkpoints are **reported**: ask what the screen shows,
   never "did it work?".
2. **Their hands on the keys — and in this step, their account on the line.**
   The GitHub account and the repo are theirs to create; you could not do it
   for them if they asked. What you run, you run with their go-ahead.
3. **Two consent moments, and they belong to the builder:** the one
   workspace-wide sign-in setting in step 3, and the go-ahead before anything
   leaves the machine in step 4. Ask each one plainly, once, and say what it is
   for. The once-per-session do-it-for-them escape valve does not apply to
   either.
4. **Your own commands stay silent.** You run `git` and `gh` quietly and
   report what they tell you in builder words ("your workspace is signed in as
   maria-w", "everything saved in your project just went up") — never the
   command or its vocabulary. Say **"save a checkpoint"** and **"back up to
   GitHub"**, never *commit*, *push*, or *stage* as bare verbs. Use a git word
   only after you have said what it means, or if the builder uses it first.
5. **On failure, diagnose from the recovery notes, explain plainly, retry
   once.** Then the ladder: `/bluerock:help`, then the BlueRock Builders
   Discord — with their post written for them, in their words ("Save your
   work, step 4 — first backup fails with an error about the remote"), so
   asking costs nothing. Never leave them holding an error with no named next
   move.
6. **Honest floors.** If a guard finds something (a secret, a shortened
   history), that is the step working, not a failure — say what was found and
   what happens next, in one line each.

## Before you start

- Anchor to the project (signature: `CLAUDE.md` and `design/` side by side —
  check the current folder, then one level down). Capture its **absolute
  path**; every command below runs against it. No project at all? The backup
  has nothing to protect: say so and offer Session 1.
- **Check the state first — this step may already be done, or half done.**
  Quietly run `git remote -v`, `gh auth status`, and check whether the current
  branch exists on the remote. Then branch:
  - **A remote of their own, signed in, branch pushed** → the backup already
    exists. Show them the proof in one line (their repo's address and that
    their latest work is on it), remind them wrap-up offers the backup at every
    close, and stop. Do not re-teach a step they have finished.
  - **A remote pointing at BlueRock's template** (`bluerock-io/my-workspace`
    in its URL) → counts as no backup at all. Do not remove it yet — step 4
    replaces it, with consent, after their own repo exists.
  - **Signed in but no remote of their own** → resume at step 2 (they need a
    repo). **A remote of their own but not signed in** → resume at step 3.
    Recap in one line what is already in place.
  - **Neither** → start at step 1.
- Do not write to `learning/progress.json`. This step has no session number,
  and its completion is inspectable by anyone at any time — the remote and the
  sign-in ARE the record. (Recorded as a decision in the dependency notes.)
- Open with the frame, in one breath: everything you have built lives in one
  place; this step gives it a second — a private repo on GitHub that only you
  can see, that your workspace backs up to from now on.

## The steps

### 1. Create your GitHub account

Do not assume one exists — ask. Plenty of builders have one from another life;
plenty have never needed one.

- **Have one?** They sign in at `github.com` and move to step 2.
- **Don't?** They go to `github.com/signup` and create one — their own email,
  their own password, the free plan. GitHub verifies the email; that happens on
  their screen and you wait for it. The account is theirs, not BlueRock's:
  whatever happens to their workspace or their subscription, this account and
  what they back up into it remain.

- *Recovery:* if GitHub's signup stalls on the email verification, the code
  went to the address they typed — have them check spam before retrying.
- *Checkpoint 1:* **reported** — they are signed in on `github.com` (ask what
  the top-right corner shows: their avatar means signed in).

### 2. Create a new private repo — completely empty

This is the one step where a helpful-looking checkbox breaks the backup, so
set it up before they click anything: GitHub will offer to start the repo with
a README and other starter files. **They must leave every one of those off.**
Their project already has its own history, and a repo born with a starter file
has a page of history their project has never seen — the first backup then
fails with an error a non-developer cannot read. An empty repo accepts their
project exactly as it is.

Walk it:

1. On `github.com`, they open the menu to create a **new repository**.
2. **Name:** `my-workspace` is fine, or any name they will recognize. The name
   labels the backup; it changes nothing else.
3. **Private**, not public. Private means only they can see it.
4. **No README, no .gitignore, no license.** Every "initialize this repository
   with" option stays unticked.
5. Create it.

- *Checkpoint 2:* **reported** — GitHub lands them on a mostly empty page
  headed **"Quick setup"**. That page is the pass state: it only appears for a
  truly empty repo. Ask what the page's heading says. Have them keep this page
  open — step 4 needs the repo address shown on it.
- *Recovery (repo not empty):* if they see a file listing instead of "Quick
  setup", a starter file got ticked. The clean fix at this point is to delete
  the repo and make it again empty: **Settings → the danger zone at the bottom
  → Delete this repository** (GitHub asks them to type the repo name to
  confirm). Nothing of theirs is in it yet, so nothing is lost. Then repeat
  this step with every box unticked.

### 3. Sign the workspace in to GitHub

Their workspace has to be able to talk to their GitHub account. GitHub's own
sign-in flow does this without a password ever touching the workspace: it
shows a one-time code, and the builder proves it is them from their own
browser.

1. Run the sign-in quietly (`gh auth login`, GitHub.com, HTTPS, the device
   flow). It prints a short code shaped like `XXXX-XXXX` and a web address.
2. Relay both to the builder in plain words: "GitHub gave your workspace a
   one-time code. Open `github.com/login/device` in your browser, type the
   code in, and approve it." Remind them once: that code works only at that
   address — never type it anywhere else that asks for it.
3. Wait. The sign-in completes on their screen and confirms in this chat.
4. **Then the one setting, with consent before it runs.** Ask plainly: "One
   setting makes your workspace use this sign-in whenever it talks to GitHub —
   it applies to your whole workspace, not just this project. Okay to set it?"
   On their yes, run `gh auth setup-git` quietly. If they say no, say what it
   means honestly — the backup in step 4 will stop and ask for credentials it
   has no good way to take — and offer the setting again there. (This is the
   skill's one workspace-wide write, deliberate and consented: the plugin owns
   git configuration in the workspace.)

- *Recovery:* code expired before they typed it → run the sign-in again; a
  fresh code costs nothing. Code rejected → the usual cause is a typo; the
  code is short and the dashes matter.
- *Checkpoint 3:* **inspectable** — the sign-in status reports their account.
  Tell them in their words: "your workspace is signed in to GitHub as
  \<their handle\>."

### 4. The first backup

Now the actual backup — with two guards that run **before anything leaves the
machine**. Name them to the builder in one line each as you go; watching the
guards run is part of what this step teaches.

**In order:**

1. **Complete the history if it arrived shortened** (current-image workspaces
   only). Check for `.git/shallow` in the project. If present: the project was
   seeded with a shortened history, and a shortened history cannot be backed
   up to an empty repo — the attempt fails with an unreadable error. Complete
   it from BlueRock's public template first: run
   `git fetch --unshallow https://github.com/bluerock-io/my-workspace.git`
   quietly (use the remote named `origin` instead if it still points at the
   template). Tell the builder what happened in their words: "your project
   came with a shortened history to keep it small — I've completed it from
   BlueRock's public template. Nothing about your work changed." If
   `.git/shallow` is absent, skip this entirely and silently.
2. **Point the project at their new repo.** Have them copy the repo address
   from the Quick setup page (the `https://github.com/...` one) and paste it
   here. If the project still points at BlueRock's template, say so and ask:
   "your project's backup address still points at BlueRock's shared template —
   I'll switch it to your new repo. Okay?" On yes, set the remote to their
   address quietly. Never leave the template as a place anything could be sent;
   never push to it even if a push would succeed.
3. **Make sure there is something to back up, saved.** A fresh-image project
   may have no checkpoints at all yet, and any project may have unsaved work
   from today. If saves need a name first (no identity configured), ask once,
   plainly: "What name and email should your saves be recorded under? This
   just labels your work in your own project." Set it scoped to the project,
   never workspace-wide. If this is their first checkpoint, give them the one
   sentence first: saving takes a snapshot of your project as it is right now;
   it stays in your workspace until you back it up. Then save a checkpoint
   covering what is there, with their go-ahead.
4. **The secrets scan.** Look through everything about to go up — every file
   the backup would send — for things that should never leave the machine:
   key and token patterns, password-looking values, `.env`-style credential
   files, private key blocks. Tell them you are doing it and why in one line:
   "before anything leaves this machine, I'm checking that nothing secret is
   in it — a backup is forever-ish, so secrets stay out." **Found something?**
   Stop. Name the file and what it looks like in plain words, keep it out of
   the backup (with consent: exclude it and remove it from what goes up), then
   scan again. Nothing goes up until the scan is clean. **Found nothing?** Say
   so in one line and move on.
5. **The go-ahead, then the backup.** Say plainly what is about to happen:
   everything saved in the project goes up to their new private repo, and
   from then on backups send only what changed. On their go-ahead, push the
   current branch quietly (as it is named — never rename it; their empty repo
   accepts it exactly as it is) and set it to track. Report the result in
   builder words: "everything saved in your project just went up to your
   repo."

- *Recovery (the one to know cold):* the backup fails with an error mentioning
  the remote or unpacking → the shortened-history guard was skipped or did not
  complete. Check `.git/shallow` again, complete the history, and back up
  again. Once, then the ladder.
- *Recovery:* the backup is rejected because the repo is not empty → a starter
  file exists after all. Back to step 2's recovery (delete and recreate
  empty), then back up again.
- *Checkpoint 4:* **inspectable** — the branch exists on their remote and
  nothing is left unpushed. But do not declare victory here; the proof that
  counts is theirs, in step 5.

### 5. Prove it

The observable that makes it real. Have them go back to their browser and
**refresh the repo page** (the Quick setup page they kept open). The empty
page is gone; in its place, their own files.

Ask them to name one file they recognize — their own work, on a page only
they can see, in an account only they control. That is the backup: not a
concept, a page they can open from any machine on any day.

- *Checkpoint 5:* **reported** — they name a file of theirs on the repo page.
  This is the step's real pass.

### 6. What changes from now on

One beat, spoken, nothing to do:

- **Every wrap-up can now offer the backup.** When they close a chat with
  `/bluerock:wrap-up`, it checks the state it needs — the remote, the
  sign-in, the name on their saves — and all of it now passes. Saving stays
  one step: wrap up, say yes.
- **The sign-in survives.** Disconnecting and reconnecting their AI tool does
  not undo it. This was a one-time setup, like Session 1 was.
- **Session 7 is unblocked.** A scheduled routine runs against their repo on
  GitHub — which, as of ten minutes ago, exists.

## Close the loop

When checkpoint 5 passes:

1. **One line of earned recognition, specific to what they just did.** This is
   a genuine first — the first time their work exists in two places — so it
   gets a beat. Name what they saw: "That repo page you just refreshed is your
   project, off this machine, in an account that is yours — whatever happens
   to this workspace, that page keeps your work." Never generic, never before
   the file was seen.
2. **Debrief in one breath:** they made a private repo of their own, signed
   the workspace into their account, watched two guards run, and sent
   everything up. From now on the backup is an offer at every wrap-up, not a
   project.
3. Ask "how would you describe what you just set up?" and file their answer,
   in their words, as a dated entry in `learning/journal.md`.
4. Point forward: Session 7, **Put an agent on a schedule** — about 20
   minutes, where a routine runs on a clock against the repo they just
   created. Say **teach me Session 7** here, or take it up next time.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`/bluerock:wrap-up` (steps 4–5) is the downstream consumer of this step's
  outcome.** Its state check (identity, remote, sign-in) is exactly what this
  step establishes; after this step passes, wrap-up offers the save and the
  backup together. The vocabulary here — "save a checkpoint", "back up to
  GitHub", the first-save sentence, the identity ask (project-scoped, never
  workspace-wide) — is wrap-up's, kept in lockstep on purpose. Reword in both
  places or neither.
- **Session 7's Before-you-start carries an interim backup walkthrough**
  (marked interim in its own text) that this skill supersedes. When this skill
  ships in a release, that beat becomes a check and a pointer to this step —
  a batched follow-on, not a silent edit.
- **The empty-repo rule and the shortened-history guard are load-bearing
  engineering facts, not style** (`learn-skills-review.md` § Engineering,
  2026-08-15/16, verified in Linda's walkthrough on a real workspace): fresh
  workspaces are on branch `master` against GitHub's default `main`, so a
  repo born with a README fails the first backup on a divergence error; and
  seeded shallow history cannot push to an empty repo. Do not simplify either
  guard away, and never rename the builder's branch.
- **`gh auth setup-git` is this skill's one workspace-wide write**, consented
  at the prompt, per Eng's position that the plugin owns all git
  configuration (2026-08-15). If that ever needs to widen, it is a deliberate
  decision recorded here.
- **The 0.8.2 template rule stands everywhere:** `bluerock-io/my-workspace` is
  never a push target, in any state, even when the push would succeed. This
  skill reads from it exactly once (completing a shortened history), which
  writes nothing to it.
- **This skill deliberately writes no `learning/progress.json` entry.** The
  step has no session number, and its completion is inspectable at any time
  (the remote and the sign-in are the record). `/bluerock:learn` and
  `learn-status` derive availability from `curriculum/manifest.json`, which
  has no row for this step yet — a manifest row is Eng-cadence and tracked in
  the rollout doc.
- **learn.bluerock.io's Save-your-work page describes what this skill does.**
  Behavior-visible changes here need the page diff against
  `workbench/app/learn/v4/save-your-work/` and `learn-syw-copy-v4.md` before
  finishing.
