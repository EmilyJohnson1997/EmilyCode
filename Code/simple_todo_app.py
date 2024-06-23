# simple_todo_app.py
class Todo:
    def __init__(self, task):
        self.task = task
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TodoApp:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(Todo(task))

    def complete_task(self, task):
        for todo in self.todos:
            if todo.task == task:
                todo.mark_completed()
                return f"Task '{task}' completed."
        return f"Task '{task}' not found."

    def display_tasks(self):
        for todo in self.todos:
            status = "Completed" if todo.completed else "Pending"
            print(f"Task: {todo.task}, Status: {status}")

if __name__ == "__main__":
    app = TodoApp()
    app.add_task("Write code")
    app.add_task("Test code")
    app.display_tasks()
    print(app.complete_task("Write code"))
    app.display_tasks()
