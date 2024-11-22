import unittest
from agent.task_manager import TaskManager
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task(1, "Test Task")
        self.assertEqual(self.task_manager.get_task_status(1), 'Pending')

    def test_update_task_status(self):
        self.task_manager.add_task(2, "Another Task")
        self.task_manager.update_task_status(2, "Completed")
        self.assertEqual(self.task_manager.get_task_status(2), 'Completed')

    def test_get_next_task(self):
        self.task_manager.add_task(3, "Next Task")
        task_id, task = self.task_manager.get_next_task()
        self.assertEqual(task_id, 3)
        self.assertEqual(task, "Next Task")

if __name__ == "__main__":
    unittest.main()
