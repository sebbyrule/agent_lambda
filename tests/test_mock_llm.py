import unittest
from llm_wrappers.mock_llm import MockLLM

class TestMockLLM(unittest.TestCase):
    def setUp(self):
        self.llm = MockLLM()

    def test_generate_response(self):
        response = self.llm.generate_response("Hello")
        self.assertEqual(response, "Mock response to: Hello")

if __name__ == "__main__":
    unittest.main()
