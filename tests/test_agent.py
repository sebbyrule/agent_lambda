import unittest
from agent.agent import Agent
from llm_wrappers.openai_llm import OpenAILLM
from llm_wrappers.mock_llm import MockLLM
from llm_wrappers.google_gemini import GoogleGeminiLLM
from llm_wrappers.ollama import OllamaLLM
from tools.search_tool import SearchTool
from tools.file_operation_tool import FileOperationTool
class TestAgentIntegration(unittest.TestCase):
    def setUp(self):
        llm = MockLLM()
        tools = [SearchTool(), FileOperationTool()]
        self.agent = Agent(goal="Test Goal", llm=llm, tools=tools)
        tasks = [{"tool": "SearchTool", "parameters": {"query": "AI Framework"}}]
        self.agent.initialize_agent(tasks)

    def test_agent_task_execution(self):
        # Execute task and verify completion
        self.agent.execute_task()
        state = self.agent.state_manager.get_current_state()
        self.assertEqual(state, 'Idle')  # Agent should return to Idle after executing

    def test_memory_store_and_recall(self):
        self.agent.manage_memory("test_key", "test_data", action='store')
        data = self.agent.manage_memory("test_key", action='recall')
        self.assertEqual(data, "test_data")

if __name__ == "__main__":
    unittest.main()
