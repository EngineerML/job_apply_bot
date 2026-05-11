from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.cover_letter import router as cover_letter_router
from routes.jobs import router as jobs_router

load_dotenv()

app = FastAPI(title="Bid Assist API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cover_letter_router)
app.include_router(jobs_router)


@app.get("/health")
def health():
    return {"status": "ok"}

