# M2 Phase 03 — CI/CD Handoff Checklist

> Autonomous run wrote the GitHub Actions workflow and the VPS-side sudoers drop-in. Two classes of work remain for the IAM dev: (1) GitHub Environments + Secrets, (2) SSH key pairing between Actions and the VPS `deploy` user.

## 1. GitHub Environments

Create two environments in the repo (Settings → Environments):

| Environment | Required reviewers | Notes |
|-------------|-------------------|-------|
| `production` | **Yes — 1 reviewer** (IAM dev or designate) per D-04 | Gate on manual approval before deploys to prod |
| `staging` | None | Fully automated on push to `staging` branch |

## 2. GitHub Actions Secrets (scoped per environment)

Each environment gets its own copy of the same three secret names. This is how `${{ secrets.SSH_PRIVATE_KEY }}` resolves to different values for prod vs staging.

| Secret | Environment | Value | Notes |
|--------|-------------|-------|-------|
| `SSH_PRIVATE_KEY` | `production` | ed25519 private key for `deploy@<vps>` authorized for prod | Generate per environment; DO NOT reuse between prod and staging |
| `VPS_HOST` | `production` | Public IP or hostname of the prod VPS | Example: `vps.interactivemove.nl` or a bare IP |
| `VPS_USER` | `production` | `deploy` | Matches the user `bootstrap.sh` created |
| `SSH_PRIVATE_KEY` | `staging` | separate ed25519 private key | Separate keypair |
| `VPS_HOST` | `staging` | same VPS (for now — single-box deployment) | |
| `VPS_USER` | `staging` | `deploy` | same system user; isolation is by env, port, and systemd unit |

**None of these must leak into repo files.** The workflow uses only `${{ secrets.* }}` interpolation.

## 3. SSH key pairing

For each environment:

1. Generate on your laptop: `ssh-keygen -t ed25519 -C "actions-prod@interactivemove.nl" -f ./actions_prod -N ""`.
2. Copy the PUBLIC key (`actions_prod.pub`) content into `/home/deploy/.ssh/authorized_keys` on the VPS.
3. Paste the PRIVATE key (`actions_prod`) into the `SSH_PRIVATE_KEY` secret of the matching GitHub Environment.
4. Delete the private key from your laptop.

Verify from a laptop that does NOT have the key:
```
ssh -i /dev/null deploy@<vps>   # should be refused
```
Verify from Actions: the first workflow run will fail with `Permission denied` if the key pairing is off.

## 4. VPS side — already handled by bootstrap.sh

`bootstrap.sh` (Phase 02) now installs `/etc/sudoers.d/iam-deploy` during `install_sudoers_deploy()`. If bootstrap was run before this checklist existed, pull the repo on the VPS and run:

```
sudo install -m 440 -o root -g root \
  /path/to/repo/config/sudoers.d/iam-deploy \
  /etc/sudoers.d/iam-deploy
sudo visudo -cf /etc/sudoers.d/iam-deploy
```

## 5. First deploy — dry-run on staging

1. Push a no-op commit to the `staging` branch.
2. Watch the workflow — job `deploy-staging` should:
   - Check out the repo
   - Build `/tmp/iam-deploy-<sha>.tar.gz` excluding `.git`, `node_modules`, `.planning`, `.github`, `.claude`, `.kiro`
   - scp the tarball to `deploy@<staging_host>:/tmp/`
   - Run `sudo -u iam /usr/local/bin/iam-deploy staging <sha>` over SSH
   - Health-check `https://iam.abbamarkt.nl/` (5 attempts, 3s apart)
3. If health check fails, `iam-deploy` rolls the symlink back and the workflow exits non-zero.

## 6. Rollback procedure

Two options, both human-initiated:

1. **Re-run an older successful workflow run.** Actions UI → select the previous `deploy-*` run that succeeded → **Re-run all jobs**. This redeploys that same commit atomically.
2. **VPS-side symlink flip.** SSH in as `deploy`, run `ls /var/www/iam/releases/` to see the retained releases, then:
   ```
   sudo -u iam ln -sfn /var/www/iam/releases/<target> /var/www/iam/current
   sudo systemctl restart iam-api
   ```

## 7. Open questions for the planning session

- Confirm target repo slug: workflow triggers on `main`/`staging` in THIS repo. If Phase 05 migrates to `oopuo-ship/iam-website`, the workflow file needs no changes (both refs are relative to the repo) but the SSH Secrets must be re-created in the new repo.
- Confirm whether prod deploys should also run a post-deploy `/api/chat` smoke POST. Current health check only hits `/` for speed; a chat POST would need a dummy body and might hit the rate limiter during rapid deploys.
