from fastapi import APIRouter
from app.routers import role_suggestion

router = APIRouter()

router.include_router(role_suggestion.router, prefix="/api", tags=["role-suggestion"])

@router.get("/")
def read_home():
    """
    Home route that returns a welcome message.
    
    Returns:
        dict: A welcome message with status
    """
    return {
        "message": "Welcome to JobPsych AI",
        "status": "active",
        "version": "0.1.0"
    }
