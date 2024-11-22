class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task):
        self.tasks[task_id] = {'task': task, 'status': 'Pending'}

    def update_task_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = status
            print(f"Task {task_id} status updated to {status}")

    def get_next_task(self):
        """Retrieve the next pending task."""
        for task_id, task_info in self.tasks.items():
            if task_info['status'] == 'Pending':
                return task_id, task_info['task']
        return None, None

    def get_task_status(self, task_id):
        """Retrieve the status of a given task."""
        return self.tasks.get(task_id, {}).get('status', 'Not Found')
