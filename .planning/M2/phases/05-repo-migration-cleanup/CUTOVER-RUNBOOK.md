# M2-05 Cutover Runbook

> Step-by-step human procedure to migrate the site from `clubeedg-ship-it/iam-website` to `oopuo-ship/iam-website` with zero downtime. Do NOT execute this during Phase 05 — it's the handoff document. Worker produced the clean starting state; this runbook drives the cutover.

**Target downtime:** 0 seconds. VPS doesn't know or care which remote it pulled from.

---

## 0. Prerequisites

- [ ] All four phase PRs (M2-01 → M2-04) are merged to `main` on `clubeedg-ship-it/iam-website`.
- [ ] Prod is live on the VPS with the full Phase 01–04 stack running (chat proxy hardened, HubSpot backend route live, Actions deploys green on staging + prod).
- [ ] OpenRouter key has been rotated per Phase 01 `HISTORY-SCAN.md`.
- [ ] All `REPLACE_ME_*` env values on the VPS are set (OpenRouter keys, HubSpot portal/guid, letsencrypt email). Confirm with `sudo grep REPLACE_ME /etc/iam-api/env /etc/iam-api-staging/env` → empty.
- [ ] IAM dev has a fresh SSH key they're willing to pair with the new repo's Actions (recommended — rotate during cutover).

## 1. Create the new GitHub account + repos

Performed by the human (guardrail absolute: worker MUST NOT create these).

- [ ] Sign in or create `oopuo-ship` personal GitHub account.
- [ ] Create `oopuo-ship/iam-website` — **public**, **empty** (no README, no LICENSE, no .gitignore — the clean tree already has them).
- [ ] Create `oopuo-ship/iam-website-internal` — **private**, **empty**. This receives `.planning/`, `.claude/`, `CLAUDE.md`, `LOVABLE-BRIEF.md`, `ACTION-PLAN.md`, `MEDIA-GALLERY.md`, `website-adjustments.xlsx` as a separate backup.

## 2. Resolve the LICENSE placeholder

- [ ] Edit `LICENSE` at repo root on branch `m2/phase-05` (current content: `REPLACE_ME_LICENSE_CHOICE`).
- [ ] Replace with chosen license text (proprietary / MIT / Apache-2.0 / BSD-3-Clause).
- [ ] Commit with `chore(M2-05): set LICENSE to <choice>`.

## 3. Run `tools/prepare-clean-repo.sh` locally

On your laptop:

```
export AUTHOR_NAME='oopuo-ship'
export AUTHOR_EMAIL='<oopuo-ship account email>'
cd /path/to/iam-m2-worker   # the worker's worktree (must be on m2/phase-05 after step 2)
git checkout m2/phase-05
./tools/prepare-clean-repo.sh /tmp/iam-website-clean
```

Expected output tail:
```
[prepare-clean] initial commit: <sha>
[prepare-clean] file count : <N>
[prepare-clean] commit count: 1
[prepare-clean] gitleaks clean            # if gitleaks installed; otherwise "skipping"
[prepare-clean] DONE.
```

Sanity checks to run by hand:

```
cd /tmp/iam-website-clean
git log --oneline               # single line, single commit, authored by oopuo-ship
git ls-files | grep -E 'CLAUDE|LOVABLE|ACTION-PLAN|MEDIA-GALLERY|\.planning|\.claude|\.kiro'
# ^ must be empty

grep -rE 'Co-Authored-By:|@anthropic\.com|gsd-|kiro-|kiro:|Claude Code' . \
  --exclude-dir=node_modules --exclude-dir=.git | grep -v '^Binary'
# ^ must be empty (no AI fingerprints in tracked content)
```

If any of these fail, abort — do NOT push. Adjust `prepare-clean-repo.sh`'s exclude list, reopen Phase 05, fix, retry.

## 4. Push clean state to `oopuo-ship/iam-website`

```
cd /tmp/iam-website-clean
git remote add origin git@github.com:oopuo-ship/iam-website.git
git push -u origin main
```

## 5. Mirror the internal workflow tree to `iam-website-internal`

```
cp -R /path/to/iam-m2-worker /tmp/iam-website-internal-src
cd /tmp/iam-website-internal-src
rm -rf .git
git init --initial-branch=main
git config user.name  "$AUTHOR_NAME"
git config user.email "$AUTHOR_EMAIL"
git add -A
git commit -m "internal workflow snapshot @ M2 cutover" --no-verify
git remote add origin git@github.com:oopuo-ship/iam-website-internal.git
git push -u origin main
```

This repo holds the planning trail, spec docs, and internal instruction files. Private, reference-only.

## 6. Configure the new public repo from day one (D-12, D-13)

In `oopuo-ship/iam-website` (Settings):

- [ ] **Branch protection on `main`:**
  - Require a pull request before merging: ON, 1 approving review
  - Require status checks to pass: ON, select `gitleaks / scan` once it has run once
  - Require branches to be up to date before merging: ON
  - Do not allow bypassing: ON
  - Restrict deletions, no force-push (ON by default on protected branches)
- [ ] **Environments:**
  - `production` — required reviewer (IAM dev or designate)
  - `staging` — no required reviewer
- [ ] **Secrets (scoped per environment):**
  - `SSH_PRIVATE_KEY` (NEW pair — generate here, add public to `deploy@<vps>:~/.ssh/authorized_keys`, keep old working until cutover switch in step 8)
  - `VPS_HOST` (same VPS hostname/IP as old repo)
  - `VPS_USER=deploy`
- [ ] **Actions → General:** allow only `oopuo-ship/` actions and specific trusted marketplace actions (`actions/checkout`, `gitleaks/gitleaks-action`).

## 7. Smoke the pipeline against staging

- [ ] Push a trivial commit to a `staging` branch in `oopuo-ship/iam-website` (e.g. fix a typo in README).
- [ ] Watch the `Deploy` workflow run `deploy-staging` job:
  - checks out, tars, scp to VPS, runs `sudo -u iam /usr/local/bin/iam-deploy staging <sha>`, curl health check passes.
- [ ] Hit `https://iam.abbamarkt.nl/` in a browser. Verify it loads the new commit.

If this is green, the new repo is ready for prod.

If not, debug against staging only. Do NOT proceed until staging deploy is 100% green from the new repo.

## 8. Flip prod to the new repo

- [ ] In `oopuo-ship/iam-website`: merge `staging` → `main` (or push directly to main; your call). **Production environment reviewer approves.**
- [ ] Watch `deploy-prod`. VPS updates prod under `/var/www/iam/current` via `iam-deploy prod <sha>` — atomic symlink flip. Health check green.
- [ ] Hit `https://interactivemove.nl/` twice — once via Cloudflare (should see `server: cloudflare`), once directly (bypass) if you have raw VPS access.
- [ ] `sudo journalctl -u iam-api -n 50 --no-pager` — confirm `chat_proxy_listening` log after restart.
- [ ] Submit one test message via `/api/chat` with your real browser. Confirm 200 + response.
- [ ] Submit one test contact form with name `CUTOVER-TEST`. Confirm `{ok:true}` + HubSpot record + email at `klantcontact@interactivemove.nl`. Delete the test record.

## 9. Archive the old repo

Wait **30 days** of green operation on the new repo before doing step 9.b.

- [ ] 9.a (day of cutover): In `clubeedg-ship-it/iam-website` Settings → **Archive repository**. Confirm the banner shows "This repository has been archived". Update the old repo's README to point at `oopuo-ship/iam-website`.
- [ ] 9.b (+30 days): If no rollback has been needed, delete the old repo. Belt-and-suspenders against lingering secrets in git history (D-04 rationale).

## 10. Rollback (only if cutover fails post-merge)

If prod breaks after step 8:

1. **Fastest path — stay on the new repo, roll the deploy back.** `iam-deploy` keeps the last 5 releases; flip the symlink:
   ```
   ssh deploy@<vps>
   ls /var/www/iam/releases/
   sudo -u iam ln -sfn /var/www/iam/releases/<previous> /var/www/iam/current
   sudo systemctl restart iam-api
   ```
2. **Slower — point deploy back at the old repo.** In GitHub UI, restore `clubeedg-ship-it/iam-website` from archive. Rotate the SSH_PRIVATE_KEY back to the old-repo's. Trigger a manual deploy from the old repo's `main` to resync the VPS.

Option 1 is always preferred. The old repo remains as a safety net but shouldn't be the first response.

## 11. Post-cutover housekeeping

- [ ] Update external references: anywhere documentation says `clubeedg-ship-it/iam-website`, change to `oopuo-ship/iam-website`. Start with `bootstrap.sh`'s `REPO_URL` placeholder (set it before running bootstrap on a NEW VPS post-cutover; existing VPS doesn't need this).
- [ ] Confirm Cloudflare dashboard unchanged (it doesn't know about GitHub).
- [ ] Confirm HubSpot form notifications still arrive.
- [ ] Delete any OpenRouter API keys still hanging around that pre-date the cutover.

---

## Checklist — hard sequence with gates

```
Gate A  : all M2-01..04 PRs merged + prod green
 ↓
1. Create oopuo-ship + repos        (HUMAN)
2. Resolve LICENSE placeholder      (HUMAN)
3. Run prepare-clean-repo.sh        (HUMAN, local)
 ↓
Gate B  : clean tree passes every sanity check in §3
 ↓
4. Push clean state to new repo     (HUMAN)
5. Mirror internal tree             (HUMAN)
6. Configure new repo               (HUMAN)
 ↓
Gate C  : Actions secrets + environments + branch protection all set
 ↓
7. Staging deploy smoke             (HUMAN + Actions)
 ↓
Gate D  : staging deploy green end-to-end from new repo
 ↓
8. Prod deploy + verification       (HUMAN + Actions)
 ↓
Gate E  : prod green, chat + contact form both verified live
 ↓
9.a Archive old repo                (HUMAN, same day)
9.b Delete old repo                 (HUMAN, +30 days)
```

No step is reversible without going to the rollback procedure in §10. Gate D is the last chance to abort cheaply — if staging doesn't deploy green from the new repo, stop, debug, do not touch prod.
