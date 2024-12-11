import FreeSimpleGUI as sg
import functions

# Function to update the listbox
def update_todo_listbox(window, todos):
    window['todos'].update(values=todos)

# GUI Layout
layout = [
    [sg.Text("Type a task"), sg.InputText(tooltip="Enter a task", key='todo'), sg.Button("Add")],
    [sg.Listbox(values=functions.get_todos(), key="todos", size=(45, 10), enable_events=True)],
    [sg.Button("Edit"), sg.Button("Complete")],
]

# Create the window
window = sg.Window('Task App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'].strip() + "\n"
        if new_todo.strip():  # Ensure input is not empty
            todos.append(new_todo)
            functions.write_todos(todos)
            update_todo_listbox(window, todos)
        else:
            sg.popup("Please enter a valid task!", title="Error")

    elif event == "Edit":
        try:
            selected_task = values['todos'][0]  # Get the selected task
            new_todo = sg.popup_get_text("Edit the task", default_text=selected_task.strip())
            if new_todo:
                todos = functions.get_todos()
                index = todos.index(selected_task)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                update_todo_listbox(window, todos)
        except IndexError:
            sg.popup("Please select a task to edit!", title="Error")

    elif event == "Complete":
        try:
            selected_task = values['todos'][0]  # Get the selected task
            todos = functions.get_todos()
            todos.remove(selected_task)
            functions.write_todos(todos)
            update_todo_listbox(window, todos)
            sg.popup(f"Task '{selected_task.strip()}' completed!", title="Success")
        except IndexError:
            sg.popup("Please select a task to complete!", title="Error")

# Close the window
window.close()
