from pydantic import BaseModel
from typing import Optional


class GenerateCoverLetterRequest(BaseModel):
    job_title: str
    company: str
    job_description: str


class SaveJobRequest(BaseModel):
    job_title: str
    company: str
    job_description: str
    job_url: str


class SaveJobResponse(BaseModel):
    job_id: str


class SaveCoverLetterByIdRequest(BaseModel):
    job_id: str
    cover_letter: str


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


class ProfileData(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    zip: Optional[str] = None
    race: Optional[str] = None
    veteran: Optional[str] = None
    disability: Optional[str] = None
    desired_salary: Optional[str] = None


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
