# function definition: Getting Tasks
def get_todos(filepath="tasks.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local

# A function for writing tasks


def write_todos(todos_arg, filepath="tasks.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

