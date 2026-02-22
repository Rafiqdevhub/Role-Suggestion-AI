from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class PersonalInfo(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None

class Experience(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[List[str]] = []

class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    year: Optional[str] = None
    details: Optional[List[str]] = None

class RoleRecommendation(BaseModel):
    roleName: str
    matchPercentage: float
    reasoning: str
    requiredSkills: List[str] = []
    missingSkills: List[str] = []
    careerLevel: str = "Mid-level"
    industryFit: str = "Good"

class ResumeScore(BaseModel):
    overall_score: float  # 0-100
    technical_score: float
    experience_score: float
    education_score: float
    communication_score: float
    reasoning: str
    strengths: List[str]
    weaknesses: List[str]
    improvement_suggestions: List[str]

class PersonalityInsights(BaseModel):
    traits: Dict[str, float]  # trait_name: score 0-100
    work_style: str
    leadership_potential: float
    team_player_score: float
    analysis: str

class CareerPathPrediction(BaseModel):
    current_level: str
    next_roles: List[str]
    timeline: str
    required_development: List[str]


class ResumeData(BaseModel):
    personalInfo: Optional[PersonalInfo] = None
    experience: Optional[List[Experience]] = []
    education: Optional[List[Education]] = []
    skills: Optional[List[str]] = []
    summary: Optional[str] = None
    certifications: Optional[List[str]] = []


class ResumeAnalysisResponse(BaseModel):
    resumeData: Optional[ResumeData] = None  # None for privacy-focused preparation system
    roleRecommendations: List[RoleRecommendation]
    resumeScore: Optional[ResumeScore] = None
    personalityInsights: Optional[PersonalityInsights] = None
    careerPath: Optional[CareerPathPrediction] = None
    preparationPlan: Optional[Dict[str, Any]] = None  # Role-specific preparation guidance




