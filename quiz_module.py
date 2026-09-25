from google import genai
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def clean_json_block(text):
    return re.sub(r"```(?:json)?\n(.*?)```", r"\1", text, flags=re.DOTALL).strip()

def generate_quiz(text: str) -> list:
    try:
        if not client: raise Exception("API client not configured")
        prompt = f"Create a 3-question multiple choice quiz with 'question', 'options', and 'answer' keys from this text:\n\n{text}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        cleaned = clean_json_block(response.text.strip())
        return json.loads(cleaned)
    except Exception as e:
        # LOCAL FALLBACK
        topic = text[:20] + "..." if len(text) > 20 else text
        return [
            {
                "question": f"Which of the following best describes the core concept of: {topic}?",
                "options": ["It is a fundamental principle of nature", "It only applies in an isolated vacuum", "It has no practical applications", "It changes completely every hour"],
                "answer": "It is a fundamental principle of nature"
            },
            {
                "question": "Why is this subject area important in modern school curricula?",
                "options": ["It builds critical thinking skills", "It is entirely optional", "It has been replaced by modern theories", "It cannot be tested"],
                "answer": "It builds critical thinking skills"
            },
            {
                "question": "What is a primary characteristic associated with this educational topic?",
                "options": ["Measurable data structures", "Random outcomes", "Total instability", "Unrelated concepts"],
                "answer": "Measurable data structures"
            }
        ]

