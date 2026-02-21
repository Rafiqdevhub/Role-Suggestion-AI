from typing import Optional
from fastapi import APIRouter, UploadFile, HTTPException, Request, Form, File, Depends, status
from pydantic import ValidationError
from app.services.resume_parser import ResumeParser
from app.models.schemas import ResumeAnalysisResponse
from app.services.prompt.analyze_resume_service import AnalyzeResumeService
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


def format_validation_error(error: ValidationError) -> dict:
    """Format Pydantic validation errors for API response."""
    return {
        "message": "Validation error",
        "errors": error.errors()
    }


@router.post(
    "/role-suggestion",
    response_model=ResumeAnalysisResponse,
    status_code=status.HTTP_200_OK,
)
@limiter.limit("5/day")  # 5 files per IP address per day
async def analyze_resume(
    file: UploadFile,
    request: Request,
    target_role: Optional[str] = Form(None),
    job_description: Optional[str] = Form(None)
):
    try:
        parser = ResumeParser()
        resume_data = await parser.parse(file)
        
        # Generate role recommendations with target role analysis
        analyze_service = AnalyzeResumeService()
        if target_role:
            # Analyze fit for target role + provide alternatives
            role_recommendations = await analyze_service.analyze_role_fit(resume_data, target_role, job_description)
        else:
            # General role recommendations
            role_recommendations = await analyze_service.generate(resume_data)
        
        # Calculate resume score, personality insights, and career path
        resume_score = await analyze_service.calculate_resume_score(resume_data)
        personality_insights = await analyze_service.analyze_personality(resume_data)
        career_path = await analyze_service.predict_career_path(resume_data)
        
        preparation_plan = None
        if target_role:
            try:
                preparation_plan = await analyze_service.generate_role_preparation_plan(
                    resume_data, target_role, job_description
                )
            except Exception as e:
                print(f"Warning: Could not generate preparation plan: {str(e)}")
                preparation_plan = None
        
        response = ResumeAnalysisResponse(
            resumeData=None,
            roleRecommendations=role_recommendations,
            resumeScore=resume_score,
            personalityInsights=personality_insights,
            careerPath=career_path,
            preparationPlan=preparation_plan
        )
        return response

    except ValidationError as e:
        raise HTTPException(
            status_code=422,
            detail=format_validation_error(e)
        )
    except Exception as e:
        error_message = str(e)
        if "PDF" in error_message:
            error_message = "Error reading PDF file. Please ensure it's not corrupted or password protected."
        elif "DOCX" in error_message:
            error_message = "Error reading DOCX file. Please ensure it's a valid Word document."
        raise HTTPException(status_code=500, detail=error_message)