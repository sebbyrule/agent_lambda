class BaseLLMWrapper:
    def generate_response(self, prompt):
        """Override this method to define LLM behavior."""
        raise NotImplementedError("LLM Wrapper must implement generate_response.")
