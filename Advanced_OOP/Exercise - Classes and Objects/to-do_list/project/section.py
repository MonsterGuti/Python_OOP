from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: str):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_amount = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {tasks_amount - len(self.tasks)} tasks."

    def view_section(self):
        task_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{task_details}"