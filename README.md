# Role Suggestion AI

An intelligent resume-driven role suggestion API powered by Google Gemini. Upload a PDF/DOCX resume, optionally add a target role and job description, and get role recommendations, resume scoring, personality insights, and a career path.

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

3. Run the app (local dev)

```bash
uvicorn main:app --reload
```

### Running with Docker (Recommended)

**Option 1: Using pre-built image from Docker Hub**

```bash
# Pull the latest image
docker pull rafiq9323/role-suggestion-ai:latest

# Run the container
docker run -p 8000:8000 --env-file .env rafiq9323/role-suggestion-ai:latest
```

**Option 2: Using Docker Compose**

```bash
docker-compose up
```

**Option 3: Building locally**

```bash
# Build the image
docker build -t role-suggestion-ai .

# Run the container
docker run -p 8000:8000 --env-file .env role-suggestion-ai
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

## API Overview

### Base URL

```
http://localhost:8000
```

### Routes

**GET /**
Returns a simple health/status response.

**POST /api/role-suggestion**
Upload a resume file and get role recommendations and analysis.

**Rate limit:** 5 requests per IP per day.

### Request (multipart/form-data)

- `file` (required): PDF or DOCX resume
- `target_role` (optional): string
- `job_description` (optional): string

Example using `curl`:

```bash
curl -X POST "http://localhost:8000/api/role-suggestion" \
	-F "file=@/path/to/resume.pdf" \
	-F "target_role=Frontend Developer" \
	-F "job_description=We need React, TypeScript, and accessibility experience."
```
