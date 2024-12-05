while True:
    user_action = input("Type add , show , edit, complete or exit: ")
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('tasks.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('tasks.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
           with open('tasks.txt', 'r') as file:
               todos = file.readlines()
               # new_todos = [item.strip('\n') for item in todos]
           for index, item in enumerate(todos):
                item = item.strip('\n')
                row= f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the task to edit:"))
            number = number -1

            with open('tasks.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a  new todo: ")
            todos[number] = new_todo + '\n'

            with open('tasks.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the task to complete:"))
            with open('tasks.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('tasks.txt', 'w') as file:
                file.writelines(todos)

            message = f"Task number {number},{todo_to_remove} has been completed."
            print(message)
        case 'exit':
            break

print("Bye")
