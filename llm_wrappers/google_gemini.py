import requests
from llm_wrappers.base_llm_wrapper import BaseLLMWrapper

class GoogleGeminiLLM(BaseLLMWrapper):
    def __init__(self, api_key, base_url="https://gemini.googleapis.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def generate_response(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150  # Adjust as needed
        }

        try:
            response = requests.post(
                f"{self.base_url}/generate",
                headers=headers,
                json=payload
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get("text", "No response text provided.")
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Google Gemini API: {e}"
