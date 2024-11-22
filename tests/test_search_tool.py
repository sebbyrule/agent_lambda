import unittest
from tools.search_tool import SearchTool

class TestSearchTool(unittest.TestCase):
    def setUp(self):
        self.tool = SearchTool()

    def test_search_tool(self):
        result = self.tool.execute({'query': 'AI Framework'})
        self.assertIn("Search results for 'AI Framework'", result)

if __name__ == "__main__":
    unittest.main()
