# M2 Phase 03: CI/CD — Context

**Gathered:** 2026-04-21
**Status:** Blocked on Phase 02
**Depends on:** Phase 02 (VPS must exist with systemd + Nginx + Cloudflare before we can deploy to it)

<domain>
## Phase Boundary

Remove every manual deploy step. Every change arrives via `git push` and is reversible in seconds. Scope covers: a GitHub Actions workflow that deploys on push to `main` (prod) and `staging` (staging) branches, a VPS-side `iam-deploy` script that performs the atomic release, and a rollback procedure.

Out of scope: testing/linting workflows (can be added inline later), notifications (Slack/email), HubSpot backend routing (Phase 04), repo migration (Phase 05).
</domain>

<decisions>
## Implementation Decisions

### Actions workflow
- **D-01:** Single workflow file `.github/workflows/deploy.yml` with two jobs — `deploy-prod` triggered on push to `main`, `deploy-staging` triggered on push to `staging`. Shared composite action or matrix to avoid duplication.
- **D-02:** Job runs on `ubuntu-latest`. Steps: checkout → set up SSH agent from `SSH_PRIVATE_KEY` secret → run `ssh deploy@vps "sudo -u iam iam-deploy <sha>"` → health check via `curl` → report.
- **D-03:** Secrets stored in GitHub Actions Secrets: `SSH_PRIVATE_KEY` (per environment), `VPS_HOST`, `VPS_USER=deploy`. Zero secrets in repo. Use GitHub Environments (`production`, `staging`) for per-env secret scoping and required-reviewer protection on prod.
- **D-04:** Prod deploys require manual approval via Environment protection rules (one-reviewer); staging deploys are fully automatic.
- **D-05:** Health check after deploy: `curl -fsS https://$DOMAIN/` and `curl -fsS -X POST https://$DOMAIN/api/chat -H 'Content-Type: application/json' -d '{"messages":[{"role":"user","content":"ping"}]}'` with a 5s timeout. Failure triggers automatic rollback.

### VPS-side deploy script
- **D-06:** Script at `/usr/local/bin/iam-deploy` installed by `bootstrap.sh` (Phase 02). NOT stored in the repo — it lives only on the VPS, owned by `root:iam`, mode `0755`. The repo carries a `tools/iam-deploy.sh` template that bootstrap copies into place.
- **D-07:** Flow: accept a commit SHA as argument → `git fetch && git checkout $SHA` in a working tree at `/var/www/iam/work` → rsync into `/var/www/iam/releases/$(date +%Y-%m-%d-%H%M%S)-${SHA:0:7}/` → `npm ci --omit=dev` in the new release dir (or reuse the shared `node_modules` symlink) → atomic `ln -sfn <new_release> /var/www/iam/current` → `systemctl reload iam-api` → retain last 5 releases, prune older.
- **D-08:** Rollback: `iam-deploy --rollback` flips the `current` symlink to the previous release dir and reloads. Staging has the same mechanism independently.
- **D-09:** The deploy user has a narrowly-scoped sudoers entry: `deploy ALL=(iam) NOPASSWD: /usr/local/bin/iam-deploy *` and `deploy ALL=(root) NOPASSWD: /bin/systemctl reload iam-api, /bin/systemctl reload nginx`. No broad sudo.
- **D-10:** The script is idempotent — running the same SHA twice produces the same `current` symlink target (or detects no-op and exits).

### Zero-downtime
- **D-11:** Static files: symlink swap is atomic at the filesystem level; Nginx opens new files on next request.
- **D-12:** Node service: `systemctl reload` sends SIGHUP; the Express app should have a SIGHUP handler that finishes in-flight requests then restarts. If Express doesn't, use `systemctl restart` — downtime is under 1s for a single-process service, acceptable for a marketing site.

### Notifications
- **D-13:** Actions workflow posts a summary in the PR/commit check UI. No Slack/email in this phase — can be added as a follow-up if IAM dev wants it.

### agent discretion
- Whether to use `appleboy/ssh-action` or manual `ssh` in the workflow
- Release retention count (3 vs 5 vs 10)
- Whether to use a `shared/node_modules` symlink or reinstall per release
</decisions>

<specifics>
## Specific Ideas

- GitHub Actions runners connect to the VPS over the public internet; the VPS SSH port should be firewalled to known IPs (or Cloudflare Zero Trust tunnel if IAM dev wants to go further — deferred).
- The `deploy` user's SSH key should be ed25519, generated per-environment, never reused.
- Squash-merge is the preferred PR strategy on the new repo (Phase 05) so every deploy corresponds to one commit SHA.
</specifics>

<canonical_refs>
## Canonical References

- `.planning/M2/ROADMAP.md`
- `.planning/M2/phases/02-vps-deployment/CONTEXT.md` — the infrastructure this pipeline deploys to
- `deploy.sh` — current hand-run script, reference for the logic `iam-deploy` replicates
- Audit report — flagged `deploy.sh` in repo as exposing the repo URL; `iam-deploy` lives off-repo
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable
- `deploy.sh` at repo root has the working `git pull` + service restart sequence; port the logic, not the file.
- Commit SHA is available to Actions as `${{ github.sha }}` — use it as the release directory suffix.

### Patterns
- Release directory structure is defined in Phase 02: `/var/www/iam/releases/<timestamp>-<short-sha>/` + `current` symlink.
- Symlink swap with `ln -sfn <target> <link>` is atomic; clients never see a broken state.

### Integration points
- `bootstrap.sh` from Phase 02 must install the `iam-deploy` script template before this phase's workflow can succeed.
- `systemctl reload iam-api` is the final step; depends on Phase 02 systemd unit.
- Cloudflare caches static assets; after deploy, a surgical cache purge of `/` and HTML files may be needed if users see stale content. First-run observation, not a blocker.
</code_context>

<deferred>
## Deferred Ideas

- Blue/green deploy with two Node processes on different ports — overkill for single VPS, symlink swap is sufficient.
- Canary deploy with gradual traffic shift — unnecessary for a marketing site.
- Slack/email notifications — add if IAM dev requests.
- Test suite integration — no tests exist yet; adding would be a separate initiative.
- Database migrations — no DB in the architecture.
</deferred>

---

*Phase: M2-03-cicd*
*Context gathered: 2026-04-21*
