class BaseTool:
    def execute(self, parameters):
        """Override this method to define tool behavior."""
        raise NotImplementedError("Tool must implement the execute method.")
