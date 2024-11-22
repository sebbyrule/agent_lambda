class Memory:
    def __init__(self):
        self.memory_store = {}

    def store(self, key, value):
        self.memory_store[key] = value
        print(f"Stored {key} in memory")

    def recall(self, key):
        return self.memory_store.get(key, None)
    def retrieve_all(self):
        return list(self.memory_store.values())
    def delete(self, key):
        if key in self.memory_store:
            del self.memory_store[key]
            print(f"Deleted {key} from memory")
    def clear(self):
        self.memory_store.clear()
        print("Memory cleared")
