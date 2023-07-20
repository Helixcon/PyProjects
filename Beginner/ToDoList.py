tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def mark_completed(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print("Task completed:", completed_task)
    else:
        print("Invalid task index. Please enter a valid index from the list.")

def todo_list():
    print("Welcome to the To-Do List application!")

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_index = int(input("Enter the index of the completed task: "))
            mark_completed(task_index)
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")


if __name__ == "__main__":
    todo_list()
