# ✅ Docker Hub Deployment Checklist

## Pre-Deployment Setup (Do This First)

### GitHub Secrets Configuration
- [ ] Go to GitHub repository
- [ ] Navigate to: **Settings** → **Secrets and variables** → **Actions**
- [ ] Click **New repository secret**
- [ ] Add Secret #1:
  - Name: `DOCKER_USERNAME`
  - Value: Your Docker Hub username (lowercase)
  - Click **Add secret**
- [ ] Add Secret #2:
  - Name: `DOCKER_TOKEN`
  - Value: Your Docker Hub Personal Access Token
  - Click **Add secret**

### Docker Hub Setup
- [ ] Have Docker Hub account (create if needed)
- [ ] Log in to [Docker Hub](https://hub.docker.com)
- [ ] Go to **Account Settings** → **Security**
- [ ] Click **New Access Token**
- [ ] Name it: `github-actions`
- [ ] Set permissions to **Read, Write**
- [ ] Copy token (save it for GitHub secrets)

### Repository Check
- [ ] `dockerfile` exists in root directory (lowercase)
- [ ] `pyproject.toml` exists with all dependencies
- [ ] `app/` directory contains application code
- [ ] `main.py` exists in root directory
- [ ] `.github/workflows/docker-build.yml` is committed
- [ ] Repository is pushed to main branch

---

## First Deployment

### Step 1: Commit Workflow Files
```bash
git add .github/workflows/docker-build.yml
git add DOCKER_SETUP.md WORKFLOW_SETUP.md DOCKER_QUICK_REF.md
git add PIPELINE_ARCHITECTURE.md DEPLOYMENT_SUMMARY.md
git commit -m "Add Docker Hub CI/CD workflow"
git push origin main
```
- [ ] Files committed and pushed

### Step 2: GitHub Secrets Already Added?
- [ ] DOCKER_USERNAME added
- [ ] DOCKER_TOKEN added
- [ ] Both verified correct

### Step 3: Monitor First Build
- [ ] Go to GitHub repository
- [ ] Click **Actions** tab
- [ ] Look for **Docker Build and Push** workflow
- [ ] Click the most recent run
- [ ] Watch for:
  - [ ] Checkout complete ✓
  - [ ] Docker Buildx setup ✓
  - [ ] Docker Hub login ✓
  - [ ] Build started ✓
  - [ ] Push to registry ✓
  - [ ] Workflow completed ✓

### Step 4: Verify Image on Docker Hub
- [ ] Log in to [Docker Hub](https://hub.docker.com)
- [ ] Go to **Repositories**
- [ ] Find `jobpsych-ai` repository
- [ ] Verify tags appear:
  - [ ] `latest` tag exists
  - [ ] `main` tag exists
  - [ ] `sha-xxxxx` tag exists
- [ ] Check image size and details

### Step 5: Test Pull Image
```bash
docker pull muhammadrafiq/jobpsych-ai:latest
```
- [ ] Image pulled successfully
- [ ] No errors in download

### Step 6: Test Run Container
```bash
docker run -p 8000:8000 --env-file .env muhammadrafiq/jobpsych-ai:latest
```
- [ ] Container starts without errors
- [ ] API accessible at `http://localhost:8000`
- [ ] Logs show application running

---

## Post-Deployment Verification

### Workflow Trigger Tests

**Test 1: Code Change Trigger**
```bash
# Make a small change to app/main.py
echo "# test" >> app/main.py
git add app/main.py
git commit -m "Test workflow trigger"
git push origin main
```
- [ ] Workflow automatically triggered
- [ ] Build completed successfully
- [ ] Image pushed to Docker Hub

**Test 2: Manual Trigger**
- [ ] Go to GitHub Actions tab
- [ ] Click **Docker Build and Push**
- [ ] Click **Run workflow**
- [ ] Select branch: `main`
- [ ] Set `push_image: true`
- [ ] Click **Run workflow**
- [ ] Verify build started

**Test 3: Pull Request Trigger**
```bash
# Create a test branch
git checkout -b test-pr
echo "# pr test" >> README.md
git add README.md
git commit -m "Test PR build"
git push origin test-pr
# Create PR on GitHub
```
- [ ] Workflow triggered on PR creation
- [ ] Build completed (without push)
- [ ] Image not pushed to Docker Hub (expected)
- [ ] Close PR (optional)

### Image Tagging Verification
- [ ] `latest` tag points to latest main push
- [ ] `main` tag exists
- [ ] `sha-xxxxx` tags created for commits
- [ ] Only successful builds produce images

### Performance Baseline
- [ ] Record first build time: **_____ minutes**
- [ ] Record cached build time: **_____ seconds**
- [ ] Compare performance metrics

---

## Ongoing Operations

### Regular Maintenance
- [ ] Check workflow runs monthly
- [ ] Monitor build times (should stay consistent)
- [ ] Review Docker Hub storage usage
- [ ] Delete old/unused images as needed
- [ ] Keep dependencies updated in pyproject.toml
- [ ] Rotate Docker Hub token annually

### Update Procedures

**When to trigger rebuilds:**
- [ ] Update dependencies in `pyproject.toml`
- [ ] Modify `dockerfile` or build config
- [ ] Major code changes in `app/`
- [ ] Update base Python version
- [ ] Security patches applied

**Commands:**
```bash
# All changes auto-trigger via push
git add .
git commit -m "Update dependencies or code"
git push origin main
```

### Monitoring Points
- [ ] GitHub Actions page showing recent runs
- [ ] Docker Hub showing latest image updates
- [ ] Build time trends (should be ~30sec with cache)
- [ ] Failed builds (should be none)
- [ ] Image size trends (watch for bloat)

---

## Troubleshooting Quick Links

### Build Failures
1. [ ] Check GitHub Actions logs
2. [ ] Verify `dockerfile` is valid
3. [ ] Check `pyproject.toml` syntax
4. [ ] Verify all dependencies available

### Docker Hub Issues
1. [ ] Verify secrets are correct
2. [ ] Check token hasn't expired
3. [ ] Confirm repository is public
4. [ ] Check Docker Hub storage quota

### Push Failures
1. [ ] Verify `DOCKER_TOKEN` has write permissions
2. [ ] Check token is current (not expired)
3. [ ] Ensure `DOCKER_USERNAME` is lowercase
4. [ ] Review GitHub Actions logs

### Local Testing
```bash
# Build locally to test Dockerfile
docker build -t jobpsych-ai:test .

# Run locally to test
docker run -p 8000:8000 --env-file .env jobpsych-ai:test

# Check size
docker images jobpsych-ai
```

---

## Documentation References

| Document | Purpose | When to Read |
|----------|---------|--------------|
| `DOCKER_SETUP.md` | Detailed setup guide | First time setup |
| `DOCKER_QUICK_REF.md` | Quick commands | Daily operations |
| `WORKFLOW_SETUP.md` | Complete workflow guide | Understanding workflow |
| `PIPELINE_ARCHITECTURE.md` | Visual architecture | Architecture review |
| `DEPLOYMENT_SUMMARY.md` | Complete summary | Onboarding new team members |

---

## Success Criteria - Final Verification

- [ ] Workflow runs on every main branch push
- [ ] Images appear on Docker Hub with correct tags
- [ ] PR builds work without pushing images
- [ ] Manual trigger works
- [ ] Images can be pulled and run
- [ ] All documentation in place
- [ ] Team trained on process

---

## Sign-Off

**DevOps Engineer:** ________________  
**Date:** ________________  
**Status:** ✅ **DEPLOYMENT COMPLETE AND VERIFIED**

---

## Quick Contacts

| Need Help With | Contact |
|---|---|
| GitHub Actions Issues | GitHub Support |
| Docker Hub Issues | Docker Support |
| Workflow Questions | See WORKFLOW_SETUP.md |
| Quick Commands | Use DOCKER_QUICK_REF.md |
| Architecture Questions | See PIPELINE_ARCHITECTURE.md |

---

**Next Steps:**
1. ✅ Add GitHub Secrets (DOCKER_USERNAME, DOCKER_TOKEN)
2. ✅ Push workflow to main branch
3. ✅ Monitor first build in Actions tab
4. ✅ Verify image on Docker Hub
5. ✅ Test image locally with docker run
6. ✅ Mark checklist items as complete
