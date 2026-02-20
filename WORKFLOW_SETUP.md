# 🐳 Docker Hub CI/CD Workflow - Setup Complete

## Overview

A complete GitHub Actions workflow has been created to automatically build and push your JobPsych AI Docker image to Docker Hub on every push to the main branch.

## What Was Created

### 1. **GitHub Actions Workflow** 
📄 File: [.github/workflows/docker-build.yml](.github/workflows/docker-build.yml)

**Features:**
- ✅ Automatic builds on push to main branch
- ✅ Multi-platform builds (amd64 & arm64)
- ✅ GitHub Actions cache for faster builds
- ✅ Automatic tagging (latest, branch, SHA)
- ✅ Docker Hub metadata sync
- ✅ Manual workflow trigger option
- ✅ Pull request builds (without push)

### 2. **Docker Setup Guide**
📄 File: [DOCKER_SETUP.md](DOCKER_SETUP.md)

Complete guide including:
- Docker Hub token creation
- GitHub Secrets configuration
- Troubleshooting steps
- Best practices

### 3. **Updated README**
📄 File: [README.md](README.md)

Added:
- Workflow status badges
- Docker Hub pre-built image pull instructions
- Multiple run options

## Quick Setup (2 Steps)

### Step 1: Create Docker Hub Personal Access Token
1. Go to [Docker Hub Security Settings](https://hub.docker.com/settings/security)
2. Click **New Access Token**
3. Name it: `github-actions`
4. Copy the token

### Step 2: Add GitHub Secrets
1. Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Add two secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_TOKEN`: The token from Step 1

## Workflow Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| **Push to main** | Any code change | Build & Push ✅ |
| **Pull Request** | PR to main | Build only (no push) |
| **Manual** | Workflow dispatch | Build & Push (if enabled) |
| **File changes** | Modified: dockerfile, pyproject.toml, uv.lock, app/**, main.py | Trigger build |

## Image Tags

Your images will be tagged automatically:

```
muhammadrafiq/jobpsych-ai:latest      ← main branch (always)
muhammadrafiq/jobpsych-ai:main        ← branch name
muhammadrafiq/jobpsych-ai:sha-abc123  ← git commit SHA
muhammadrafiq/jobpsych-ai:v1.0.0      ← git version tags (optional)
```

## Using Pre-built Images

Once the workflow runs successfully, pull images directly:

```bash
# Latest version
docker pull muhammadrafiq/jobpsych-ai:latest

# Run with docker-compose
docker-compose up

# Run standalone
docker run -p 8000:8000 --env-file .env muhammadrafiq/jobpsych-ai:latest
```

## Monitoring Builds

1. Go to **Actions** tab in GitHub
2. Click **Docker Build and Push**
3. View real-time build logs

## Workflow Configuration Details

```yaml
Build Context:     Repository root
Dockerfile:        ./dockerfile
Registries:        Docker Hub
Platforms:         linux/amd64, linux/arm64
Cache Strategy:    GitHub Actions cache
Push Condition:    main branch + successful build
```

## Security Best Practices

✅ **Already Implemented:**
- Secrets stored securely in GitHub
- Least privilege permissions
- Token-based authentication
- No credentials in logs

📋 **Recommended Actions:**
1. Rotate Docker Hub token periodically
2. Enable Docker Hub vulnerability scanning
3. Monitor builds in GitHub Actions
4. Use semantic versioning for releases

## Troubleshooting

### Workflow shows "Invalid credentials"
→ Verify secrets are correctly set: `DOCKER_USERNAME` and `DOCKER_TOKEN`

### Build fails with "Dockerfile not found"
→ Ensure `dockerfile` (lowercase) exists in repository root

### Image not appearing in Docker Hub
→ Check GitHub Actions logs under Actions tab for error details

### Need to rebuild without pushing
→ Use workflow dispatch with `push_image: false`

## Advanced Usage

### Manual Workflow Trigger
```bash
# Go to: Actions → Docker Build and Push → Run workflow → Select push_image
```

### Push Specific Version
In GitHub, create a release with tag `v1.0.0`:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```
This automatically creates image: `muhammadrafiq/jobpsych-ai:1.0.0`

## Files Modified/Created

| File | Status | Purpose |
|------|--------|---------|
| `.github/workflows/docker-build.yml` | ✨ Created | CI/CD workflow |
| `DOCKER_SETUP.md` | ✨ Created | Setup instructions |
| `README.md` | 📝 Updated | Added badges & Docker Hub option |

## Next Steps

1. ✅ Push changes to main branch
2. 🔐 Add GitHub Secrets (DOCKER_USERNAME, DOCKER_TOKEN)
3. 📋 Verify first build in Actions tab
4. 🐳 Pull pre-built image: `docker pull muhammadrafiq/jobpsych-ai:latest`
5. 🚀 Run with: `docker-compose up`

## Support

For detailed setup help, see: [DOCKER_SETUP.md](DOCKER_SETUP.md)

---

**Status:** ✅ Workflow Ready  
**Last Updated:** February 20, 2026
