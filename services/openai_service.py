import os
from openai import OpenAI

_client: OpenAI = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    return _client


def generate_cover_letter(job_title: str, company: str, job_description: str, resume: str) -> str:
    client = get_client()

    prompt = f"""You are a professional cover letter writer.

Using the resume below, write a tailored cover letter for the job posting.

Guidelines:
- 4 to 6 sentences, concise and professional
- Highlight relevant skills and experience from the resume
- Avoid generic phrases like "I am a hard worker" or "I am passionate"
- Address the specific role and company

Resume:
{resume}

Job Title: {job_title}
Company: {company}
Job Description:
{job_description}

Write only the cover letter body. No subject line or date."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()
