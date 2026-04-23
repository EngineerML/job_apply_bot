from fastapi import APIRouter, HTTPException
from models.schemas import GenerateCoverLetterRequest, SaveCoverLetterRequest, CoverLetterResponse, SaveResponse
from services import openai_service, supabase_service

router = APIRouter()


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
