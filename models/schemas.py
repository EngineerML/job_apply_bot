from pydantic import BaseModel
from typing import Optional


class GenerateCoverLetterRequest(BaseModel):
    job_title: str
    company: str
    job_description: str


class SaveCoverLetterRequest(BaseModel):
    job_title: str
    company: str
    job_description: str
    job_url: str
    cover_letter: str


class CoverLetterResponse(BaseModel):
    cover_letter: str


class SaveResponse(BaseModel):
    success: bool
    cover_letter_id: Optional[str] = None


class SaveUserRequest(BaseModel):
    name: str
    base_resume_text: str


class UserResponse(BaseModel):
    exists: bool
    name: Optional[str] = None


class UserFullResponse(BaseModel):
    name: Optional[str] = None
    base_resume_text: Optional[str] = None
