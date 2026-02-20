from fastapi import FastAPI
import uvicorn
from app.main import router
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Role Suggestion AI",
    description="An intelligent job role suggestion system that analyzes resumes and provides personalized career recommendations.",
    version="0.1.0"
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
