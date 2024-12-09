import FreeSimpleGUI as sg

label = sg.Text("Type a task")
input_box = sg.InputText(tooltip="Enter a task")
add_button = sg.Button("Add")

# Correct casing for Window
window = sg.Window('Task App', layout=[[label],  [input_box,add_button]])
window.read()
window.close()
