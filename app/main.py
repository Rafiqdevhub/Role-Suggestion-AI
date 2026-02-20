from fastapi import APIRouter

router = APIRouter()


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
