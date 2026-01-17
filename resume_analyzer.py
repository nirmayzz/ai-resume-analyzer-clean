from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(resume_text, role):
    try:
        prompt = f"""
You are an expert resume reviewer.

Analyze the resume below for the role of {role}.
Give:
1. Strengths
2. Missing skills
3. Improvements

Resume:
{resume_text}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except OpenAIError:
        return (
            "⚠️ AI service is temporarily unavailable.\n\n"
            "This project uses a paid API. Please try again later "
            "or enable billing for full functionality."
        )


def analyze_resume(resume_text, role):
    if not resume_text.strip():
        return "❗ Please paste your resume text."

    return (
        "⚠️ AI analysis is currently unavailable.\n\n"
        "This project is integrated with a paid AI API.\n"
        "The backend, UI, and integration are complete.\n\n"
        "In a real deployment, this would return:\n"
        "- Strengths\n"
        "- Missing skills\n"
        "- Resume improvements"
    )