import requests
from dotenv import load_dotenv
import os
import sys
import google.generativeai as genai
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from agent.llm_wrappers.base_llm_wrapper import BaseLLMWrapper
class GoogleGeminiLLM(BaseLLMWrapper):
    def __init__(self, model="gemini-1.5-flash", system_instruction: str = "You are a helpful assistant."):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.system_instruction = system_instruction
        self.model = genai.GenerativeModel(model, system_instruction=self.system_instruction)
    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response
    def change_system_instructions(self, system_instruction):
        self.system_instruction = system_instruction

if __name__ == "__main__":
    SYSTEM_INSTRUCTIONS = """You are an expert in copywriting and editing. You operate a tech and media blog.
    Your task is to create a blog post from a given prompt. Ensure that the blog post is engaging, informative, and relevant to the given prompt.
    Respond in markdown format."""
    gemini_llm = GoogleGeminiLLM(system_instruction=SYSTEM_INSTRUCTIONS)
    response = gemini_llm.generate_response("The power of mindfullness")
    print(response)