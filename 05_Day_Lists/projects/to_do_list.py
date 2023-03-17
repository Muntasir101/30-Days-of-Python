"""
To-Do List Application: A To-Do list application is a simple project that
uses Python lists to store the tasks to be completed.
The user can add tasks to the list, mark tasks as completed,
or remove completed tasks
"""
tasks = []

while True:
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Remove completed tasks")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        index = int(input("Enter task number to mark as completed: "))
        tasks.pop(index-1)
        print("Task marked as completed successfully!")
    elif choice == "3":
        tasks = [task for task in tasks if not task.startswith("Completed")]
        print("Completed tasks removed successfully!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
