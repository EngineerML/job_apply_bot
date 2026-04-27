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


def find_existing_job(url: str) -> dict | None:
    client = get_client()
    if not url:
        return None
    result = client.table("jobs").select(
        "id, title, company, url, status, cover_letters(content)"
    ).eq("url", url).order("created_at", desc=True).limit(1).execute()
    if result.data:
        row = result.data[0]
        cl = row.pop("cover_letters", None)
        row["cover_letter"] = cl[0]["content"] if cl else None
        return row
    return None


def save_cover_letter(job_id: str, content: str, user_id: str = "default") -> str:
    client = get_client()
    result = client.table("cover_letters").insert({
        "user_id": user_id,
        "job_id": job_id,
        "content": content,
    }).execute()
    return result.data[0]["id"]


def upsert_user(name: str, base_resume_text: str, user_id: str = "default") -> None:
    client = get_client()
    client.table("users").upsert({
        "id": user_id,
        "name": name,
        "base_resume_text": base_resume_text,
    }).execute()


def get_user(user_id: str = "default") -> dict | None:
    client = get_client()
    result = client.table("users").select("id, name").eq("id", user_id).execute()
    return result.data[0] if result.data else None


def get_user_full(user_id: str = "default") -> dict | None:
    client = get_client()
    result = client.table("users").select("id, name, base_resume_text").eq("id", user_id).execute()
    return result.data[0] if result.data else None


def get_jobs() -> list:
    client = get_client()
    # Join cover_letters to get content alongside each job
    result = client.table("jobs").select(
        "id, title, company, description, url, created_at, status, cover_letters(content)"
    ).order("created_at", desc=True).execute()
    rows = []
    for row in result.data:
        cl = row.pop("cover_letters", None)
        row["cover_letter"] = cl[0]["content"] if cl else None
        rows.append(row)
    return rows


def update_job_status(job_id: str, status: str) -> None:
    client = get_client()
    client.table("jobs").update({"status": status}).eq("id", job_id).execute()
