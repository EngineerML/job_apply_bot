from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from models.schemas import (
    GenerateCoverLetterRequest, SaveCoverLetterRequest,
    CoverLetterResponse, SaveResponse,
    SaveUserRequest, UserResponse, UserFullResponse,
    DownloadPdfRequest, CheckJobRequest, CheckJobResponse,
    SaveJobRequest, SaveJobResponse, SaveCoverLetterByIdRequest,
)
from services import openai_service, supabase_service, pdf_service

router = APIRouter()


@router.post("/save-job", response_model=SaveJobResponse)
async def save_job(req: SaveJobRequest):
    try:
        job_id = supabase_service.save_job(
            req.job_title, req.company, req.job_description, req.job_url
        )
        return SaveJobResponse(job_id=job_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-cover-letter-by-id", response_model=SaveResponse)
async def save_cover_letter_by_id(req: SaveCoverLetterByIdRequest):
    try:
        cl_id = supabase_service.save_cover_letter(req.job_id, req.cover_letter)
        return SaveResponse(success=True, cover_letter_id=cl_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/check-job", response_model=CheckJobResponse)
async def check_job(req: CheckJobRequest):
    try:
        job = supabase_service.find_existing_job(req.job_url)
        if job and job.get("cover_letter"):
            return CheckJobResponse(
                found=True,
                cover_letter=job["cover_letter"],
                job_title=job.get("title"),
                company=job.get("company"),
                status=job.get("status"),
            )
        return CheckJobResponse(found=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-cover-letter", response_model=CoverLetterResponse)
async def generate_cover_letter(req: GenerateCoverLetterRequest):
    try:
        resume = supabase_service.fetch_user_resume()
        cover_letter = openai_service.generate_cover_letter(
            req.job_title, req.company, req.job_description, resume
        )
        return CoverLetterResponse(cover_letter=cover_letter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-cover-letter", response_model=SaveResponse)
async def save_cover_letter(req: SaveCoverLetterRequest):
    try:
        job_id = supabase_service.save_job(
            req.job_title, req.company, req.job_description, req.job_url
        )
        cover_letter_id = supabase_service.save_cover_letter(job_id, req.cover_letter)
        return SaveResponse(success=True, cover_letter_id=cover_letter_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-user", response_model=UserResponse)
async def save_user(req: SaveUserRequest):
    try:
        supabase_service.upsert_user(req.name, req.base_resume_text)
        return UserResponse(exists=True, name=req.name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user", response_model=UserResponse)
async def get_user():
    try:
        user = supabase_service.get_user()
        if user:
            return UserResponse(exists=True, name=user["name"])
        return UserResponse(exists=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user/full", response_model=UserFullResponse)
async def get_user_full():
    try:
        user = supabase_service.get_user_full()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return UserFullResponse(name=user["name"], base_resume_text=user["base_resume_text"])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/download-pdf")
async def download_pdf(req: DownloadPdfRequest):
    try:
        pdf_bytes = pdf_service.generate_pdf(req.content, req.username, req.job_title)
        filename = f"{req.username}_{req.job_title}_coverletter.pdf".replace(" ", "_")
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
