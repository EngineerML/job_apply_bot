import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_pdf(content: str, username: str, job_title: str) -> bytes:
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=2.5 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "title",
        parent=styles["Normal"],
        fontSize=13,
        fontName="Helvetica-Bold",
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "body",
        parent=styles["Normal"],
        fontSize=11,
        fontName="Helvetica",
        leading=18,
        spaceAfter=10,
    )

    story = []
    story.append(Paragraph(f"{username}", title_style))
    story.append(Paragraph(f"Cover Letter — {job_title}", body_style))
    story.append(Spacer(1, 0.4 * cm))

    for para in content.strip().split("\n\n"):
        text = para.replace("\n", " ").strip()
        if text:
            story.append(Paragraph(text, body_style))

    doc.build(story)
    return buffer.getvalue()
