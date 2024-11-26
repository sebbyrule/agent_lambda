class ToolBase:
    def __init__(self, name):
        self.name = name

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Plugins must implement the `execute` method.")
