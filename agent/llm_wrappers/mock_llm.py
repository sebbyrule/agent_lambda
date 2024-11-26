from agent.llm_wrappers.base_llm_wrapper import BaseLLMWrapper

class MockLLM(BaseLLMWrapper):
    def generate_response(self, prompt):
        return f"Mock response to: {prompt}"
