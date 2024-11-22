import unittest
from unittest import mock
from llm_wrappers.google_gemini import GoogleGeminiLLM

class TestGoogleGeminiLLM(unittest.TestCase):
    
    def setUp(self):
        self.llm = GoogleGeminiLLM(api_key="test_key", base_url="http://mock_api.com")
    @mock.patch("requests.post")
    def test_generate_response(self, mock_post):
        mock_post.return_value.json.return_value = {"text": "Test response"}
        mock_post.return_value.raise_for_status = lambda: None

        response = self.llm.generate_response("Test prompt")
        self.assertEqual(response, "Test response")

if __name__ == "__main__":
    unittest.main()
