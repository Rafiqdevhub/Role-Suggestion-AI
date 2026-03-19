from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import role_suggestion

router = APIRouter()

router.include_router(role_suggestion.router, prefix="/api", tags=["role-suggestion"])


def create_app() -> FastAPI:
    app = FastAPI(
        title="Role Suggestion AI",
        description=(
            "An intelligent job role suggestion system that analyzes resumes "
            "and provides personalized career recommendations."
        ),
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://jobpsych.vercel.app",
            "http://localhost:3000",
        ],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    app.include_router(router)
    return app


app = create_app()

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
