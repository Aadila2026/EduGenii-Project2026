from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def get_learning_recommendations(topic: str) -> str:
    try:
        if not client: raise Exception("API client not configured")
        prompt = f"Suggest a structured learning path with resources for: {topic}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        # LOCAL FALLBACK
        return f"""📚 **Custom Learning Roadmap for: {topic}**

🟢 **Phase 1: Beginner Level (Week 1)**
* Learn foundational terminology, basic theories, and real-world impacts.
* *Resource:* Introductory textbook chapters and introductory video playlists.

🟡 **Phase 2: Intermediate Level (Week 2)**
* Study core functional formulas, system processes, and standard problem variants.
* *Resource:* Open-source interactive quizzes and school study guides.

🔴 **Phase 3: Advanced Level (Week 3+)**
* Analyze complex problem configurations and apply knowledge to personal projects.
* *Resource:* Advanced library documentation and case study reviews."""
