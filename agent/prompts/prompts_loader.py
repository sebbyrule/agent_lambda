import json

class PromptManager:
    def __init__(self, file_path="agent/prompts/prompts.json"):
        with open(file_path, "r") as file:
            self.prompts = json.load(file)

    def get_prompt(self, name):
        return self.prompts.get(name, "Prompt not found.")
