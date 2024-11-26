import openai
from agent.llm_wrappers.base_llm_wrapper import BaseLLMWrapper

class OpenAILLM(BaseLLMWrapper):
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error generating response: {e}"
