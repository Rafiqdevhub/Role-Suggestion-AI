# Docker Hub Workflow Setup Guide

This guide explains how to set up the GitHub Actions workflow to automatically build and push Docker images to Docker Hub.

## Prerequisites

1. Docker Hub account (free or paid)
2. GitHub repository with actions enabled
3. Docker Hub Personal Access Token

## Setup Instructions

### Step 1: Create Docker Hub Personal Access Token

1. Log in to [Docker Hub](https://hub.docker.com)
2. Go to **Account Settings** > **Security**
3. Click **New Access Token**
4. Give it a descriptive name (e.g., `github-actions`)
5. Set appropriate permissions (read/write)
6. Copy the token (you won't see it again)

### Step 2: Add GitHub Secrets

1. Go to your GitHub repository
2. Click **Settings** > **Secrets and variables** > **Actions**
3. Click **New repository secret**
4. Add the following secrets:

| Secret Name | Value |
|-----------|-------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_TOKEN` | Your Docker Hub personal access token (from Step 1) |

### Step 3: Verify Workflow Configuration

The workflow is configured to:
- **Trigger on**: Push to `main` branch or manual trigger
- **Build**: Multi-platform (amd64, arm64)
- **Push**: Only on successful builds to main branch
- **Tags**: 
  - `latest` (on main branch)
  - Branch name
  - Git commit SHA
  - Semantic version (if you use version tags)

### Step 4: Run the Workflow

#### Automatic Triggers
- Push code to `main` branch
- Push to files in the trigger paths (dockerfile, pyproject.toml, etc.)

#### Manual Trigger
1. Go to **Actions** > **Docker Build and Push**
2. Click **Run workflow**
3. Select `Push image to Docker Hub: true`
4. Click **Run workflow**

## Docker Image Naming

Your images will be pushed to:
```
docker.io/<YOUR_USERNAME>/jobpsych-ai:<tag>
```

Example:
```
docker.io/muhammadrafiq/jobpsych-ai:latest
docker.io/muhammadrafiq/jobpsych-ai:main
docker.io/muhammadrafiq/jobpsych-ai:v1.0.0
```

## Pulling the Image

Once pushed, you can pull the image:

```bash
# Latest version
docker pull <your-username>/jobpsych-ai:latest

# Specific version
docker pull <your-username>/jobpsych-ai:main

# Run with docker-compose
docker-compose up
```

## Viewing Workflow Runs

1. Go to **Actions** tab in your GitHub repository
2. Click **Docker Build and Push**
3. View the detailed logs for each run

## Troubleshooting

### "Invalid credentials" error
- Verify `DOCKER_USERNAME` is correct (lowercase)
- Verify `DOCKER_TOKEN` is correct
- Check token hasn't expired in Docker Hub

### Build fails
- Check the detailed logs in GitHub Actions
- Verify Dockerfile is correct
- Check all dependencies in pyproject.toml are available

### Image not appearing on Docker Hub
- Check the GitHub Actions logs for errors
- Verify the trigger conditions are met
- Manually run the workflow with `workflow_dispatch`

## Best Practices

1. **Use semantic versioning** - Tag releases with version numbers (v1.0.0)
2. **Monitor builds** - Set up notifications for failed builds
3. **Clean up old images** - Regularly delete unused images from Docker Hub
4. **Use image scanning** - Enable Docker Hub's vulnerability scanning
5. **Rotate tokens** - Periodically rotate your access tokens for security

## Example Usage

Once the workflow is set up:

```bash
# Pull the latest image
docker pull muhammadrafiq/jobpsych-ai:latest

# Run the container
docker run -p 8000:8000 muhammadrafiq/jobpsych-ai:latest

# Access the API
curl http://localhost:8000/docs
```

## Additional Resources

- [Docker Hub Documentation](https://docs.docker.com/docker-hub/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [docker/build-push-action](https://github.com/docker/build-push-action)
