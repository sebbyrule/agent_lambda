class Memory:
    def __init__(self):
        """
        Initializes an empty memory store

        The memory store is a dictionary where the key is a string identifier
        and the value is the stored information.
        """
        self.memory_store = {}

    def store(self, key, value):
        """
        Stores a value in memory with the given key

        Args:
            key (str): the key to store the value under
            value (any): the value to store
        """
        self.memory_store[key] = value
        print(f"Stored {key} in memory")

    def recall(self, key):
        """
        Retrieves a value from memory with the given key

        Args:
            key (str): the key to retrieve the value for

        Returns:
            any: the stored value if found, None otherwise
        """

        return self.memory_store.get(key, None)
    def retrieve_all(self):
        """
        Retrieves all values from memory

        Returns:
            list: a list of all values in memory
        """
        return list(self.memory_store.values())
    def delete(self, key):
        """
        Deletes a value from memory with the given key

        Args:
            key (str): the key to delete the value for
        """
        if key in self.memory_store:
            del self.memory_store[key]
            print(f"Deleted {key} from memory")
    def clear(self):
        """
        Clears all values from memory.

        This method removes all key-value pairs from the memory store,
        effectively resetting it to an empty state.
        """
        self.memory_store.clear()
        print("Memory cleared")
