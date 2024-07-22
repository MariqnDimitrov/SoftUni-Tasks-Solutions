from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []
    completed_tasks = 0

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            Task.completed = True
            Section.completed_tasks += 1
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        if Task.completed:
            self.tasks.clear()
        return f"Cleared {Section.completed_tasks} tasks."

    def view_section(self):
        output = f"Section {self.name}:\n"
        for task in self.tasks:
            output += f"{Task.details(task)}\n"
        return output


task = Task("Tst", "27.04.2020")
print(task.change_name("Tst"))
print(task.change_due_date("21.05.2020"))
print(task.add_comment("pay the bills"))
print(task.edit_comment(0, "finish my homework"))
print(task.edit_comment(1, "finish my homework"))
section = Section("New section")
print(section.add_task(task))
print(section.add_task(task))
print(section.complete_task("Tst"))
print(section.complete_task("Tst"))
print(section.clean_section())
print(section.view_section())



