import PySimpleGUI as sg

layout = [[sg.Text("Hello, welcome to the popup!")], [sg.Button("OK")]]
window = sg.Window("Interactive Window", layout)
event, values = window.read()
window.close()
