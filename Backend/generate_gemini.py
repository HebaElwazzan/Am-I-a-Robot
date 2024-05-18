from config import GEMINI_API_KEY
import google.generativeai as genai

GEMINI_CONFIG = {
    "generation_config": {
        "temperature": 0
    }
}


class Gemini:
    def __init__(self) -> None:
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model_name='gemini-pro', generation_config=GEMINI_CONFIG['generation_config'])

    def get_gemini_abstract(self, topic):
        prompt = f"""
        Write a wikipedia-like abstract for the following topic: {topic}.
        It should be as close as possible to the first paragraph you may encounter on a Wikipedia page for the topic, along with the correct length and writing style.
        Do not add any markdown to your response.
        Limit your response to one paragraph.
        """
        response = self.model.generate_content(prompt)
        return response.text
