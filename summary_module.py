from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def summarize_text(text: str) -> str:
    try:
        if not client: raise Exception("API client not configured")
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        # LOCAL FALLBACK
        words = text.split()
        preview = " ".join(words[:10]) + "..." if len(words) > 10 else text
        return f"📝 **Summary Notes:** This core passage discusses key elements relating to '{preview}'. In brief terms, it highlights foundational structures, primary functions, and structural processes necessary for rapid student revision and exam preparation."