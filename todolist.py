import os
import pickle
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date=None, priority=0, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {status}"

def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

def load_tasks():
    if os.path.exists('tasks.pkl'):
        with open('tasks.pkl', 'rb') as f:
            tasks = pickle.load(f)
    else:
        tasks = []
    return tasks

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"Task {index + 1}:")
            print(task)
            print("--------------------")

def add_task(tasks):
    print("Enter task details:")
    title = input("Title: ")
    description = input("Description: ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    priority = int(input("Priority (1 for highest, 0 for lowest): "))
    new_task = Task(title, description, due_date, priority)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].completed = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            print("Enter updated task details:")
            tasks[index].title = input("Title: ")
            tasks[index].description = input("Description: ")
            tasks[index].due_date = input("Due Date (YYYY-MM-DD): ")
            tasks[index].priority = int(input("Priority (1 for highest, 0 for lowest): "))
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Update Task")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                show_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                mark_complete(tasks)
            elif choice == 5:
                update_task(tasks)
            elif choice == 6:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
