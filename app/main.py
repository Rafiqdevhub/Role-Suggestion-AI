from fastapi import APIRouter, Request
from app.routers import role_suggestion

router = APIRouter()

router.include_router(role_suggestion.router, prefix="/api", tags=["role-suggestion"])

@router.get("/")
def read_home(request: Request):
    app = request.app
    return {
        "message": f"Welcome to {app.title}",
        "status": "active",
        "app": {
            "title": app.title,
            "description": app.description,
            "version": app.version,
            "docs_url": app.docs_url,
            "redoc_url": app.redoc_url,
            "openapi_url": app.openapi_url,
        },
    }
