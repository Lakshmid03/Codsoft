import datetime

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "Not set"
                print(f"{index + 1}. [{status}] {task.description} (Due: {due_date})")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD), leave empty if not applicable: ")
            if due_date_str:
                due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
            else:
                due_date = None
            task = Task(description, due_date)
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.tasks[task_index].mark_as_completed()
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
