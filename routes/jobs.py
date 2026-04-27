from fastapi import APIRouter, HTTPException
from models.schemas import JobRecord, UpdateStatusRequest
from services import supabase_service
from typing import List

router = APIRouter()


@router.get("/jobs", response_model=List[JobRecord])
async def get_jobs():
    try:
        return supabase_service.get_jobs()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/jobs/{job_id}/status")
async def update_job_status(job_id: str, req: UpdateStatusRequest):
    valid = {"Applied", "Denied", "Interview", "Accepted"}
    if req.status not in valid:
        raise HTTPException(status_code=400, detail=f"Status must be one of {valid}")
    try:
        supabase_service.update_job_status(job_id, req.status)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
