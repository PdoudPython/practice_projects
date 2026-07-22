import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from file, or return an empty list if file doesn't exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the tasks list to file as JSON."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file) 

def add_task(tasks, description):
    """Add a new task dict to the tasks list."""
    tasks.append({"task": description, "done": False})

def view_tasks(tasks):
    """Print all tasks with their index and status."""
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{status} {index}. {task['task']}")

def complete_task(tasks, index):
    """Mark a task as done by its index."""
    try:
        tasks[index]["done"] = True
        print(f"{tasks[index]['task']} has been completed!")
    except IndexError:
        print("Invalid task number.")

def delete_task(tasks, index):
    """Remove a task by its index."""
    try:
        removed = tasks.pop(index)
        print(f"{removed['task']} has been deleted.")
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View tasks  2. Add task  3. Complete task  4. Delete task  5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            description = input("Please provide a name or Description for the task: ")
            add_task(tasks, description)
            print(f"{description} has been added to the task list!")
        elif choice == "3":
            try:
                task_num = int(input("Please provide the task number: "))
                if task_num < 1:
                    print("Task number must be 1 or higher")
                else:
                    complete_task(tasks, task_num - 1)
            except ValueError:
                print("I'm sorry, please enter a valid number in integer form")
        elif choice == "4":
            try:
                task_num = int(input("Please provide the task number: "))
                if task_num < 1:
                    print("Task number must be 1 or higher")
                else:
                    delete_task(tasks, task_num - 1)
            except ValueError:
                print("I'm sorry, please enter a valid number in integer form")
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("please select a valid task number")

if __name__ == "__main__":
    main()