class Task:
    def __init__(self, task_name, state, id: int = 0):
        self.id = id
        self.task_name = task_name
        self.state = state

    def __repr__(self):
        return f'Task(task_name="{self.task_name}", state="{self.state}")'


def task_serializer(task: Task) -> dict:
    return {
        'task_name': task.task_name,
        'state': task.state
    }

def dump_db(db, serializer):
    return [serializer(obj) for obj in db]