
class ToDoList:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print("No tasks available.")

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        print(f"item {task_id} '{description}' was successfully added to the list.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} was successfully deleted.")
                break
        else:
            print(f"Task {task_id} not found.")

    def task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.cocmpleted = not_task.completed
                status = "Completed" if task.completed else "Pending"
                print(f"Task {task_id} completion status toggled to {status}.")
                break
        else:
            print(f"Task {task_id} not found.")

    def toggle_completion(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = not task.completed
                status = "Completed" if task.completed else "Pending"
                print(f"Task {task_id} completion status toggled to {status}.")
                break
        else:
            print(f"Task {task_id} not found.")

class Task:
    def __init__(self, task_id, description, completed = False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.task_id}] {self.description} - {status}"

    def __repr__(self):
        return self.__str__()

def main():
    todo_list = ToDoList()
    while True:
        print("-"*77)
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Toggle completion status")
        print("4. Delete a task")
        print("5. Quit")
        option = input("Make your choice in the form of a number: ")
        
        if option == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif option == "2":
            todo_list.list_tasks()
        elif option == "3":
            task_id = int(input("Enter task id: "))
            todo_list.toggle_completion(task_id)
        elif option == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif option == "5":
            print("Thank you for using the To-Do List Manager. We hope your mind is still working!")
            break
        else:
            print("Invalid choice. Please enter a number between '1-5'.")

if __name__ == "__main__":
    main()
