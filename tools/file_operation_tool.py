from tools.base_tool import BaseTool

class FileOperationTool(BaseTool):
    def execute(self, parameters):
        action = parameters.get('action')
        file_path = parameters.get('file_path')
        content = parameters.get('content', '')

        if action == 'read':
            try:
                with open(file_path, 'r') as f:
                    return f.read()
            except FileNotFoundError:
                return f"Error: File '{file_path}' not found."
        elif action == 'write':
            try:
                with open(file_path, 'w') as f:
                    f.write(content)
                    return f"File '{file_path}' written successfully."
            except Exception as e:
                return f"Error writing to file: {e}"
        else:
            return "Error: Invalid action. Use 'read' or 'write'."
