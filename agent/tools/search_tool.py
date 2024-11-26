from agent.tools.base_tool import ToolBase

class SearchTool(ToolBase):
    def __init__(self):
        super().__init__("SearchTool")
        
    def execute(self, parameters):
        query = parameters.get('query', '')
        if not query:
            return "Error: No query provided."
        # Simulate search results
        return f"Search results for '{query}': [result1, result2, result3]"
