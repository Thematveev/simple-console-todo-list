class TodoList:
    tasks = []

    def __init__(self, name):
        self.name = name

    def add_task(self, task_text):
        self.tasks.append(task_text)

    def remove_task(self, index):
        self.tasks.pop(index - 1)


