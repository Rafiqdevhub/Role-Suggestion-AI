from fastapi import APIRouter
from app.routers import role_suggestion

router = APIRouter()

router.include_router(role_suggestion.router, prefix="/api", tags=["role-suggestion"])

@router.get("/")
def read_home():
    return {
        "message": "Welcome to Role Suggestion AI",
        "status": "active",
        "version": "0.1.0"
    }
