import unittest
from state_mangement.state_manager import StateManager

class TestStateManagemr(unittest.TestCase):
    def setUp(self):
        self.state_manager = StateManager()

    def test_set_and_get_state(self):
        self.state_manager.transition_to("Idle")
        self.assertEqual(self.state_manager.get_current_state(), "Idle")

    def test_state_transitions(self):
        self.state_manager.transition_to("Planning")
        self.assertEqual(self.state_manager.get_current_state(), "Planning")

        self.state_manager.transition_to("Executing")
        self.assertEqual(self.state_manager.get_current_state(), "Executing")

    def test_invalid_state_handling(self):
        with self.assertRaises(ValueError):
            self.state_manager.transition_to("InvalidState")

if __name__ == "__main__":
    unittest.main()
