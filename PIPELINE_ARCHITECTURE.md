# 🔄 Docker Build Pipeline - Architecture

## CI/CD Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     GitHub Repository                            │
│                                                                   │
│  main branch                PR                Manual Trigger      │
│      │                      │                       │             │
│      └──────────┬───────────┴───────────┬──────────┘             │
│                 │                       │                         │
│         ┌───────▼─────────────────┐    │                        │
│         │  GitHub Actions         │    │                        │
│         │  docker-build.yml       │    │                        │
│         └───────┬───────────────┬─┘    │                        │
│                 │               │      │                        │
│          Build Image      Build Only   │ (no push)             │
│                 │               │      │                        │
│         ┌───────▼──────────┐    └──────┘                        │
│         │ Build & Push     │                                    │
│         │ Multi-platform   │                                    │
│         │ (amd64, arm64)   │                                    │
│         └────────┬─────────┘                                    │
│                  │                                              │
│         ┌────────▼──────────────┐                              │
│         │   Docker Hub Registry │                              │
│         │  muhammadrafiq/       │                              │
│         │  jobpsych-ai          │                              │
│         └────────┬──────────────┘                              │
│                  │                                              │
│    ┌─────────────┼─────────────┐                               │
│    │             │             │                               │
│ :latest       :main         :sha-xxx                           │
│    │             │             │                               │
│    └─────────────┼─────────────┘                               │
│                  │                                              │
└──────────────────┼──────────────────────────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │  Deployment/Usage │
         │                   │
         │ docker pull       │
         │ docker-compose    │
         │ docker run        │
         └───────────────────┘
```

## Build Steps (Inside GitHub Actions)

```
1. Checkout Code
   └─ Gets latest code from repository

2. Setup Docker Buildx
   └─ Enables multi-platform builds

3. Login to Docker Hub
   └─ Uses: DOCKER_USERNAME, DOCKER_TOKEN (from secrets)

4. Extract Metadata
   └─ Generates tags:
      • latest (main only)
      • branch name
      • git commit SHA
      • semantic version (if available)

5. Build & Push Docker Image
   └─ Platforms:
      • linux/amd64
      • linux/arm64
   
   └─ Caching:
      • GitHub Actions cache
      • Layer caching for faster builds

6. Update Docker Hub Description
   └─ Syncs README.md with Docker Hub profile

7. Output Image Digest
   └─ Logs image SHA for reference
```

## Detailed Build Timeline

```
GitHub Push to main
        │
        ▼
┌──────────────────────────────────┐
│ GitHub Actions Triggered         │
│ Workflow: Docker Build and Push  │
│ Status: Queued...                │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Setup Build Environment          │
│ • Checkout repository code       │
│ • Install Docker Buildx          │
│ Time: ~10 seconds                │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Authenticate to Docker Hub       │
│ • Verify DOCKER_USERNAME secret  │
│ • Verify DOCKER_TOKEN secret     │
│ Time: ~2 seconds                 │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Generate Image Metadata          │
│ • Tag: latest                    │
│ • Tag: main                      │
│ • Tag: sha-abc123def456          │
│ Time: ~1 second                  │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Build Docker Image               │
│ • Platform: linux/amd64          │
│ • Platform: linux/arm64          │
│ • Use cache when possible        │
│ Time: ~2-5 minutes (first time), │
│       ~30 seconds (with cache)   │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Push to Docker Hub               │
│ • Upload amd64 image             │
│ • Upload arm64 image             │
│ • Create manifest list           │
│ Time: ~1-3 minutes               │
└──────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────┐
│ Synced to Docker Hub             │
│ • Description updated            │
│ • Readme synchronized            │
│ Time: ~10 seconds                │
└──────────────────────────────────┘
        │
        ▼
✅ Build Complete & Image Available
   muhammadrafiq/jobpsych-ai:latest
```

## Image Layer Structure

```
FROM python:3.14-slim
├─ Base OS and Python runtime
│
├─ ENV PYTHONUNBUFFERED=1
└─ ENV settings for Python behavior
│
├─ COPY --from ghcr.io/astral-sh/uv
└─ Install uv package manager
│
├─ WORKDIR /app
└─ Set working directory
│
├─ COPY pyproject.toml uv.lock ./
└─ Copy dependency files
│
├─ RUN uv sync --frozen
└─ Install all dependencies
│
├─ COPY . .
└─ Copy application code
│
├─ EXPOSE 8000
└─ Document port
│
└─ CMD [".venv/bin/python", "main.py"]
   │
   └─ Start FastAPI application
```

## File Structure After Setup

```
jobpsych-ai/
├── .github/
│   └── workflows/
│       └── docker-build.yml          ✨ CI/CD Workflow
├── dockerfile                        ✅ Existing
├── docker-compose.yml                ✅ Existing
├── .dockerignore                     ✅ Existing
├── pyproject.toml                    ✅ Existing
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   └── models/
├── main.py
├── README.md                         📝 Updated
├── DOCKER_SETUP.md                   ✨ Created
├── WORKFLOW_SETUP.md                 ✨ Created
└── DOCKER_QUICK_REF.md              ✨ Created
```

## GitHub Secrets Required

```
GitHub Repository Secrets
┌────────────────────────────┬──────────────────────────┐
│ Secret Name                │ Source                   │
├────────────────────────────┼──────────────────────────┤
│ DOCKER_USERNAME            │ Docker Hub Account       │
│ DOCKER_TOKEN               │ Docker Hub Token         │
└────────────────────────────┴──────────────────────────┘
```

## Success Criteria

✅ Workflow successfully set up when:
1. Secrets added to GitHub
2. First push triggers workflow
3. Build completes without errors
4. Image appears in Docker Hub
5. Can pull with: `docker pull muhammadrafiq/jobpsych-ai:latest`

---

**Pipeline Status:** ✅ Ready to Deploy
