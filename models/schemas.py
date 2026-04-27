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


class CheckJobRequest(BaseModel):
    job_url: str


class CheckJobResponse(BaseModel):
    found: bool
    cover_letter: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    status: Optional[str] = None


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


class DownloadPdfRequest(BaseModel):
    content: str
    username: str
    job_title: str


class JobRecord(BaseModel):
    id: str
    title: Optional[str]
    company: Optional[str]
    description: Optional[str]
    url: Optional[str]
    created_at: Optional[str]
    status: Optional[str]
    cover_letter: Optional[str]


class UpdateStatusRequest(BaseModel):
    status: str
