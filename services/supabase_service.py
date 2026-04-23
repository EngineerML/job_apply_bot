import os
from supabase import create_client, Client

_client: Client = None


def get_client() -> Client:
    global _client
    if _client is None:
        _client = create_client(
            os.environ["SUPABASE_URL"],
            os.environ["SUPABASE_KEY"],
        )
    return _client


def fetch_user_resume(user_id: str = "default") -> str:
    client = get_client()
    result = client.table("users").select("base_resume_text").eq("id", user_id).single().execute()
    return result.data["base_resume_text"]


def save_job(title: str, company: str, description: str, url: str) -> str:
    client = get_client()
    result = client.table("jobs").insert({
        "title": title,
        "company": company,
        "description": description,
        "url": url,
    }).execute()
    return result.data[0]["id"]


def save_cover_letter(job_id: str, content: str, user_id: str = "default") -> str:
    client = get_client()
    result = client.table("cover_letters").insert({
        "user_id": user_id,
        "job_id": job_id,
        "content": content,
    }).execute()
    return result.data[0]["id"]
