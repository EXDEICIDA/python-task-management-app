while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('tasks.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        with open('tasks.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('tasks.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif 'edit' in user_action:
        number = int(input("Number of the task to edit: ")) - 1

        with open('tasks.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + '\n'

        with open('tasks.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(input("Number of the task to complete: ")) - 1

        with open('tasks.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[number].strip('\n')
        todos.pop(number)

        with open('tasks.txt', 'w') as file:
            file.writelines(todos)

        message = f"Task number {number + 1}, {todo_to_remove}, has been completed."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("This command is not valid!")

print("Bye")
