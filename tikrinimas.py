def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task added: {task}")

def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")

def print_tasks(todo_list):
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Initial to-do list
todo_list = []

while True:
    print('=== To-Do List Management ===')
    print('0: Exit')
    print('1: Add Task')
    print('2: Remove Task')
    print('3: Print Tasks')
    choice = input('Enter your choice: ')

    if choice == '0':
        break
    elif choice == '1':
        task = input('Enter task: ')
        add_task(todo_list, task)
    elif choice == '2':
        task = input('Enter task: ')
        remove_task(todo_list, task)
    elif choice == '3':
        print_tasks(todo_list)
    else:
        print("Invalid choice. Please try again.")
