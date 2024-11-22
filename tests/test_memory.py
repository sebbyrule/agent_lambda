import unittest
from agent.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_store_to_memory(self):
        self.memory.store(0, "This is a test memory.")
        self.assertEqual(self.memory.recall(0), "This is a test memory.")

    def test_retrieve_all(self):
        self.memory.store(0, "First memory.")
        self.memory.store(1, "Second memory.")
        all_memories = self.memory.retrieve_all()
        self.assertEqual(all_memories, ["First memory.", "Second memory."])

    def test_clear_memory(self):
        self.memory.store(0,"Memory to clear.")
        self.memory.clear()
        self.assertEqual(self.memory.retrieve_all(), [])

if __name__ == "__main__":
    unittest.main()
