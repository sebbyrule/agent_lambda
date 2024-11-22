from agent.memory import Memory
from agent.state_manager import StateManager
from agent.task_manager import TaskManager
class Agent:
    def __init__(self, goal, llm, tools=None):
        self.goal = goal
        self.tasks = []
        self.state_manager = StateManager()  # StateManager instance
        self.memory = Memory()               # Memory instance
        self.llm = llm                       # LLM instance
        self.task_manager = TaskManager()    # TaskManager instance
        self.tools = tools or []             # List of available tools

    def initialize_agent(self, tasks):
        """Initialize the agent with a goal and tasks."""
        self.tasks = tasks
        for i, task in enumerate(tasks):
            self.task_manager.add_task(task_id=i, task=task)
        self.state_manager.transition_to('Idle')
        print(f"Agent initialized with goal: {self.goal} and tasks: {tasks}")

    def execute_task(self):
        """Execute the next task using available tools and LLM."""
        task_id, task = self.task_manager.get_next_task()
        if task_id is None:
            print("All tasks completed.")
            self.state_manager.transition_to('Completed')
            return
        
        self.state_manager.transition_to('Executing')
        print(f"Executing task {task_id}: {task}")

        # If the task requires a tool or LLM, handle it here
        if 'tool' in task:
            tool_name = task['tool']
            parameters = task.get('parameters', {})
            tool = self.get_tool(tool_name)
            if tool:
                result = tool.execute(parameters)
                self.memory.store(f"task_{task_id}_result", result)
                print(f"Result from {tool_name}: {result}")
            else:
                print(f"Tool {tool_name} not found.")
        elif 'llm_prompt' in task:
            prompt = task['llm_prompt']
            response = self.llm.generate_response(prompt)
            self.memory.store(f"task_{task_id}_response", response)
            print(f"Response from LLM: {response}")
        
        self.task_manager.update_task_status(task_id, 'Completed')
        self.state_manager.transition_to('Idle')

    def get_tool(self, tool_name):
        """Retrieve a tool by name."""
        for tool in self.tools:
            if tool.__class__.__name__ == tool_name:
                return tool
        return None

    def manage_memory(self, key, data=None, action='store'):
        """Store, recall, or delete information from memory."""
        if action == 'store':
            self.memory.store(key, data)
        elif action == 'recall':
            return self.memory.recall(key)
        elif action == 'delete':
            self.memory.delete(key)
