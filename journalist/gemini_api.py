from google import genai
from journalist import prompts


class GeminiAPI():
    def __init__(self, topic):
        if topic not in ["title", "short_content", "long_content", "tts"]:
            raise ValueError("Invalid topic. Choose from 'title', 'short_content', 'long_content', 'tts'.")
        self.messages = [
            ("system", prompts.prompts_dict[topic]),
        ]
        self.llm = genai.Client(

        )

    def get_response(self, content):
        self.response = self.llm.models.generate_content(
            model="gemini-2.0-flash",
            contents=self.messages + [("user", content)]
        )
        return self.response.text
    
