from fastapi import FastAPI
import uvicorn
from app.main import router
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="JobPsych AI",
    description="An intelligent job psychology application",
    version="0.1.0"
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
