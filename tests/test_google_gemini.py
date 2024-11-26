import unittest
from unittest.mock import patch
from agent.llm_wrappers.google_gemini import GoogleGeminiLLM

class TestGoogleGeminiLLM(unittest.TestCase):
    def setUp(self):
        self.llm = GoogleGeminiLLM()

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generate_response(self, mock_generate_content):
        prompt = "Test prompt"
        mock_generate_content.return_value = "Test response"
        response = self.llm.generate_response(prompt)
        self.assertEqual(response, "Test response")

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_generate_response_with_error(self, mock_generate_content):
        prompt = "Test prompt"
        mock_generate_content.side_effect = Exception("Test error")
        with self.assertRaises(Exception):
            self.llm.generate_response(prompt)

    def test_change_system_instructions(self):
        new_system_instruction = "New system instruction"
        self.llm.change_system_instructions(new_system_instruction)
        self.assertEqual(self.llm.system_instruction, new_system_instruction)

if __name__ == "__main__":
    unittest.main()