"""
## This is the best GUI library for me as a begginer
## https://docs.pysimplegui.com/en/latest/documentation/what_is_it/window_creation/
# pip install PySimpleGUI
psgissue
psgmain
psghome
psgupgrade
psghelp
psgver
psgsettings
import PySimpleGUI as sg




#
import PySimpleGUI as sg

layout = [[sg.Text("Hello, welcome to the popup!")], [sg.Button("OK")]]
window = sg.Window("Interactive Window", layout)
event, values = window.read()
window.close()


#
import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

#
import PySimpleGUI as sg

layout = [  [sg.Text('ROW 1'), sg.Button('Row 1 - #1'), sg.Checkbox('Row 1 - #2'), sg.Button('Row 1 - #3')],
            [sg.Text('ROW 2'), sg.Checkbox('Row 2 - #1'), sg.Checkbox('Row 2 - #2'), sg.Checkbox('Row 2 - #3')],
            [sg.Text('ROW 3'), sg.Button('Row 3 - #1'), sg.Button('Row 3 - #2')]  ]

window = sg.Window('Window Title', layout)

event, values = window.read()

window.close()

# 
import PySimpleGUI as sg

layout = [  [sg.Text('Network Tester', font='_ 20')],
            [sg.TabGroup([[
                sg.Tab('Send', [[sg.Text('Message to send:'), sg.Multiline(size=(60,10), key='-SEND-')]]),
                sg.Tab('Receive', [[sg.Text('Message Received'), sg.Multiline(size=(60,10), key='-RCV-')]])]])],
            [sg.Button('Send Message'), sg.Button('Exit')]  ]

window = sg.Window('My Network Tester', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Send Message':
        sg.popup('Sending:', values['-SEND-'])
        window['-RCV-'].update(values['-SEND-'])
window.close()

"""


