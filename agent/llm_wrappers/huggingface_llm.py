from agent.llm_wrappers.base_llm_wrapper import BaseLLMWrapper
class HuggingFaceLLM(BaseLLMWrapper):
    def generate_response(self, prompt):
        # Example call to Hugging Face API
        return f"Response for prompt: {prompt}"