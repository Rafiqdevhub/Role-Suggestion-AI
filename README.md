# JobPsych AI

An intelligent job psychology application powered by FastAPI and Google Generative AI.

[![Docker Build and Push](https://github.com/muhammadrafiq/jobpsych-ai/actions/workflows/docker-build.yml/badge.svg)](https://github.com/muhammadrafiq/jobpsych-ai/actions/workflows/docker-build.yml)
[![Docker Image Size](https://img.shields.io/docker/image-size/muhammadrafiq/jobpsych-ai/latest)](https://hub.docker.com/r/muhammadrafiq/jobpsych-ai)

## Quick Start

### Prerequisites

1. Copy the environment template file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Google API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

### Running with Docker (Recommended)

**Option 1: Using pre-built image from Docker Hub**
```bash
# Pull the latest image
docker pull muhammadrafiq/jobpsych-ai:latest

# Run the container
docker run -p 8000:8000 --env-file .env muhammadrafiq/jobpsych-ai:latest
```

**Option 2: Using Docker Compose**
```bash
docker-compose up
```

**Option 3: Building locally**
```bash
# Build the image
docker build -t jobpsych-ai .

# Run the container
docker run -p 8000:8000 --env-file .env jobpsych-ai
```

The application will be available at http://localhost:8000

### Running Locally

**Option 1: Using the run script (recommended)**
```bash
chmod +x run.sh
./run.sh
```

**Option 2: Manual activation with virtual environment**
```bash
# Activate virtual environment
source .venv/bin/activate

# Run the application
python main.py
```

**Option 3: Direct Python execution**
```bash
.venv/bin/python main.py
```

### Installing Dependencies

If you need to install/update packages:

```bash
# Option 1: Using the run script directly with pip
.venv/bin/python -m pip install -e .

# Option 2: With activated venv
source .venv/bin/activate
pip install -e .
```

## API Documentation

Once the application is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Home**: http://localhost:8000/

## Project Structure

```
.
├── main.py              # Application entry point
├── app/
│   ├── main.py         # Router setup
│   ├── models/         # Pydantic models
│   ├── routers/        # API route handlers
│   └── services/       # Business logic
└── README.md
```
