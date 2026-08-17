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
and from then on, every wrap-up can offer the backup. **Time:** about 10
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

### 2. Sign the workspace in to GitHub

Their workspace has to be able to talk to their GitHub account. GitHub's own
sign-in does this without a password ever touching the workspace: it shows a
one-time code, and the builder proves it is them from their own browser.

**One thing to clear before it runs.** One of the questions the sign-in asks
sets git up for their whole workspace, not just this project, so get their okay
first — you will be answering that question on their behalf: "One of the
questions sets your workspace up to use this sign-in whenever it talks to
GitHub. It applies to the whole workspace, not just this project. Okay to say
yes to it?" If they decline, say honestly what it costs — the backup in step 4
will stop and ask for credentials it has no good way to take — and offer it
again there. (This is the skill's one workspace-wide write, deliberate and
consented: the plugin owns git configuration in the workspace.)

Then have them paste this line — their hands, not yours:

```
gh auth login
```

Answer the prompts on their behalf; every answer is fixed. **GitHub.com**,
**HTTPS**, yes to authenticating git (the one they just approved), and the
**browser** sign-in. In a workspace with no browser, "browser" resolves to a
one-time code, which is exactly what you want. If the plain form ever stalls
with nothing on screen, re-run it with every answer supplied so it has nothing
left to ask:

```
gh auth login --hostname github.com --git-protocol https --web --skip-ssh-key
```

GitHub prints a code shaped `XXXX-XXXX` and the address
`github.com/login/device`. Show them **both**, in plain words: "GitHub gave
your workspace a one-time code. Open `github.com/login/device` in your browser,
type the code in, and approve it." Remind them once: that code works only at
that address, so never type it anywhere else that asks for it. Never print the
token, and never read it back to them.

⚑ **PROVISIONAL (2026-08-17).** This path was walked live once and ran smoothly.
It replaces a procedure that shipped because `gh auth login` was documented to
hang when driven from a session (three attempts, 2026-08-16, including under a
pseudo-terminal). Clear this marker after one more clean run in a real
workspace; if it ever hangs again, the fallback below is the proven path.

- *Recovery (the sign-in hangs with no output):* do not wait it out. Drive
  GitHub's device endpoint directly — the procedure that shipped in 0.9.3, kept
  here because it is verified. Request the code with `curl -s -X POST
  https://github.com/login/device/code -H "Accept: application/json" -d
  "client_id=178c6fc778ccc68e1d6a" -d "scope=repo read:org"`, show the builder
  only the `user_code` and the address, then poll
  `https://github.com/login/oauth/access_token` (same client id, the
  `device_code`, `grant_type=urn:ietf:params:oauth:grant-type:device_code`, at
  GitHub's stated interval) and pipe the token straight into
  `gh auth login --with-token` so it is never printed. **One poller, one
  consumer — this cost a real failure on 2026-08-16:** the token is issued
  exactly once, so never check progress by calling the endpoint separately from
  the poller; a second caller consumes the issuance and leaves the poller stuck
  on `authorization_pending` forever, with `gh` still signed out and no error
  anywhere. A did-it-work check reads the poller's own result, never re-polls.
- *Recovery:* code expired before they typed it → run the sign-in again; a
  fresh code costs nothing. Code rejected → the usual cause is a typo; the code
  is short and the dashes matter.

- *Checkpoint 2:* **inspectable** — the sign-in status reports their account.
  Tell them in their words: "your workspace is signed in to GitHub as
  \<their handle\>." Say the breadth out loud, once, with the revoke path:
  this sign-in covers their repositories, not just the backup repo, and they
  can see or revoke it any time on github.com under **Settings → Applications
  → Authorized OAuth Apps** — the entry is **GitHub CLI**, and its own menu is
  where revoking lives (never "Revoke all", which would also revoke their
  other apps).

### 3. Create your private repo — from right here

Now that the workspace is signed in, the repo gets made from this chat. No
browser form, and no checkbox to get wrong.

Have them paste this, with a name they will recognize:

```
gh repo create my-workspace --private
```

One line of why, in their terms: this is the backup home their project will
send its saves to, and private means only they can see it.

**Why this is the safer route, worth knowing but not worth explaining to them:**
made this way the repo is born **empty**, which is what the backup needs. The
web form offers to start a repo with a README and other starter files, and a
repo born with one has a page of history their project has never seen — the
first backup then fails with an error a non-developer cannot read. Creating it
from here removes that failure instead of warning about it.

- *Checkpoint 3:* **inspectable** — `gh` prints the new repo's address on
  success. Read it back to them once; step 4 sends their work to it, and step 5
  is where they open it. If they would rather see it now, that address opens in
  any browser.
- *Recovery (the name is taken):* they already have a repo by that name. Any
  name works — have them run it again with a different one.
- *Recovery (they made it on github.com instead):* fine, as long as it is
  **empty**. An empty repo lands them on a mostly blank page headed **"Quick
  setup"**; that page only appears for a truly empty repo. If they see a file
  listing instead, a starter file got ticked — delete the repo
  (**Settings → the danger zone at the bottom → Delete this repository**;
  GitHub asks them to type the repo name to confirm) and make it again from
  here. Nothing of theirs is in it yet, so nothing is lost.

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
2. **Point the project at their new repo.** The address is the one `gh` printed
   in step 3 — no hunting for it, and nothing to copy from a browser. (If they
   made the repo on github.com instead, take the `https://github.com/...`
   address from its Quick setup page.) If the project still points at
   BlueRock's template, say so and ask:
   "your project's backup address still points at BlueRock's shared template —
   I'll switch it to your new repo. Okay?" On yes, set the remote to their
   address quietly. Never leave the template as a place anything could be sent;
   never push to it even if a push would succeed.
3. **Make sure there is something to back up, saved.** A fresh-image project
   may have no checkpoints at all yet, and any project may have unsaved work
   from today. If saves need a name first (no identity configured), say the
   separating sentence BEFORE the ask, because the ask lands right after a
   successful sign-in and reads as a failure without it (a real builder hit
   exactly this, 2026-08-16): "Signing in proved to GitHub that you're allowed
   in. The name on each save is written separately — it was never set by the
   sign-in." Then ask once, plainly: "What name and email should your saves be
   recorded under? This just labels your work in your own project." The email
   is a real choice with one consequence worth naming: an address verified on
   their GitHub account links every save to their profile; anything else shows
   as a plain unlinked name. If they'd rather keep a personal address out of
   the repo's history, GitHub's forwarding form always links:
   `<id>+<login>@users.noreply.github.com` (get the id quietly with
   `gh api user --jq .id` — but never call `gh api user/emails`: this sign-in's
   scope doesn't cover it, it 404s, and gh prints a scope-refresh instruction
   that reads as an error). Set the identity scoped to the project, never
   workspace-wide.
   **The email is the one that can stop the backup, so get it right here rather
   than at the push** (walked 2026-08-17): GitHub refuses commits that would
   expose an address its owner keeps private, and the refusal arrives at the
   sync in step 4, not here. The forwarding form above never trips it, which is
   why it is the one to offer first. If they would rather use their real
   address, it has to be one GitHub will let them share — that is a setting on
   their account (**Settings → Emails**), and the honest trade is one line:
   the forwarding form keeps their address out of every saved change, while a
   real address is visible to anyone who can see the repo. If this is their first checkpoint, give them the one
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

The observable that makes it real. Give them the repo address from step 3 and
have them **open it in their browser** (or refresh it, if they still have it
open). Where the repo was empty a moment ago, their own files are now listed.

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
  2026-08-15/16, verified in a walkthrough on a real workspace): fresh
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
  its v4 page (content repo, private) and its copy doc before
  finishing.
