# JobPsych AI

An intelligent job psychology application powered by FastAPI and Google Generative AI.

## Quick Start

### Running the Application

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
