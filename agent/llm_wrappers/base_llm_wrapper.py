class BaseLLMWrapper:
    def generate_response(self, prompt: str) -> str:
        """Generate a response based on the given prompt."""
        raise NotImplementedError("Subclasses must implement `generate_response`.")
