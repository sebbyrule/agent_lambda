import json

class Analytics:
    def __init__(self, file_path="analytics_data.json"):
        self.file_path = file_path

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
