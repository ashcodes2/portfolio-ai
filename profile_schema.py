from pydantic import BaseModel
from typing import Optional


class PersonalInfo(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str
    location: str
    email: str
    phone: str
    linkedin: str
    github: str
    portfolio: str
    leetcode: Optional[str] = None


class TechnicalSkills(BaseModel):
    languages: list[str]
    frontend: list[str]
    backend: list[str]
    database: list[str]
    tools: list[str]
    core_cs: list[str]
    currently_learning: list[str]


class Experience(BaseModel):
    role: str
    company: str
    responsibilities: list[str]


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
    highlights: list[str]


class Education(BaseModel):
    institution: str
    degree: Optional[str] = None
    branch: Optional[str] = None
    cgpa: Optional[str] = None


class CandidateProfile(BaseModel):
    personal_info: PersonalInfo
    professional_summary: str
    technical_skills: TechnicalSkills
    experience: list[Experience]
    projects: list[Project]
    education: list[Education]