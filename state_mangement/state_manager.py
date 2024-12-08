class StateManager:
    def __init__(self):
        """
        Initializes the state manager.

        The state manager keeps track of the current state of the agent and
        provides a way to transition to a new state with retry logic for
        'Failed' states.

        Args:
            None

        Attributes:
            current_state (str): The current state of the agent.
            valid_states (list[str]): A list of valid states the agent can be in.
            retry_count (int): The number of retries the agent has attempted.
            max_retries (int): The maximum number of retries the agent can attempt.
        """
        self.current_state = None
        self.valid_states = ["Idle", "Planning", "Executing", "Completed", "Failed"]  # Add valid states here
        self.retry_count = 0
        self.max_retries = 3

    def transition_to(self, new_state):
        """Transition to a new state, with retry logic for 'Failed' states."""
        if new_state not in self.valid_states:
            raise ValueError(f"Invalid state: {new_state}")

        print(f"Transitioning from {self.current_state} to {new_state}")
        if new_state == "Failed" and self.retry_count < self.max_retries:
            self.retry_count += 1
            print(f"Retrying task (attempt {self.retry_count}/{self.max_retries})")
            self.current_state = "Executing"
        else:
            self.current_state = new_state
            self.retry_count = 0  # Reset retries on successful transition or non-retry states

    def get_current_state(self):
        """Returns the current state of the agent."""
        
        
        return self.current_state
