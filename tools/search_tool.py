from tools.base_tool import BaseTool

class SearchTool(BaseTool):
    def execute(self, parameters):
        query = parameters.get('query', '')
        if not query:
            return "Error: No query provided."
        # Simulate search results
        return f"Search results for '{query}': [result1, result2, result3]"
