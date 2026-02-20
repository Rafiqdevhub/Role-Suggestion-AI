# 🐳 Docker Workflow Quick Reference

## First Time Setup (5 minutes)

```bash
# 1. Create Docker Hub Personal Access Token
# → https://hub.docker.com/settings/security
# → Click "New Access Token", name it "github-actions"

# 2. Add GitHub Secrets
# → https://github.com/YOUR_USERNAME/jobpsych-ai/settings/secrets/actions
# → Add: DOCKER_USERNAME (your Docker Hub username)
# → Add: DOCKER_TOKEN (the token from step 1)

# 3. Push to trigger first build
git push origin main

# 4. Monitor build
# → https://github.com/YOUR_USERNAME/jobpsych-ai/actions
```

## Usage

### Pull pre-built image
```bash
docker pull muhammadrafiq/jobpsych-ai:latest
docker run -p 8000:8000 --env-file .env muhammadrafiq/jobpsych-ai:latest
```

### Start with compose
```bash
docker-compose up
```

### Manual build
```bash
docker build -t jobpsych-ai .
docker run -p 8000:8000 --env-file .env jobpsych-ai
```

## Available Tags

| Tag | Source | Use Case |
|-----|--------|----------|
| `latest` | main branch | Current stable |
| `main` | main branch | Development |
| `sha-abc123` | Git commit | Specific version |
| `v1.0.0` | Git release tag | Release version |

## Workflow Triggers

| Action | Result |
|--------|--------|
| Push to `main` | Build & Push to Docker Hub ✅ |
| Open PR | Build only (no push) |
| Edit dockerfile, pyproject.toml, uv.lock, app/**, main.py | Trigger build |
| Workflow dispatch | Manual build & push |

## Common Commands

```bash
# View logs
docker logs -f <container_id>

# Stop container
docker stop <container_id>

# Remove image
docker rmi muhammadrafiq/jobpsych-ai

# Login to Docker Hub
docker login

# Check image size
docker images | grep jobpsych-ai
```

## Troubleshooting

```bash
# Local build test
docker build -t jobpsych-ai:test .
docker run -p 8000:8000 --env-file .env jobpsych-ai:test

# Check secrets are set
# → https://github.com/YOUR_USERNAME/jobpsych-ai/settings/secrets/actions

# View workflow logs
# → https://github.com/YOUR_USERNAME/jobpsych-ai/actions
```

## Documentation

- 📖 Detailed Setup: [DOCKER_SETUP.md](DOCKER_SETUP.md)
- 📋 Full Workflow Guide: [WORKFLOW_SETUP.md](WORKFLOW_SETUP.md)
- 🐳 Docker Hub Profile: https://hub.docker.com/r/muhammadrafiq/jobpsych-ai

---

**Tip:** After first push, monitors builds at:
```
https://github.com/YOUR_USERNAME/jobpsych-ai/actions/workflows/docker-build.yml
```
