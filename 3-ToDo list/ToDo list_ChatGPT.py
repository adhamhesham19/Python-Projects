todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added")

def view_tasks():
    if not todo_list:
        print("No task to display.")
    else:
        for task in todo_list:
            print(task)

def remove_task():
    if not todo_list:
        print("No task to remove.")
    else:
        task = input("Enter a task: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed")
        else:
            print("Task not found.")

def exit_program():
    print("Exiting program.")
    return True

def handle_invalid_command():
    print("Invalid command")

def main():
    while True:
        user_action = input("Enter a command (add, view, remove, exit): ")

        if user_action == "add":
            add_task()
        elif user_action == "view":
            view_tasks()
        elif user_action == "remove":
            remove_task()
        elif user_action == "exit":
            if exit_program():
                break
        else:
            handle_invalid_command()

if __name__ == "__main__":
    main()
