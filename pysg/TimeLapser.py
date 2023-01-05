#! /usr/bin/python3
# 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
import PySimpleGUI as sg

layout=[
[sg.Text('Time Lapse Parameters:')],
[sg.Text("Enter Time Lapse Interval"), sg.Combo([i for i in range(1,61)], key='-INTERVAL-', size=(4, 1), default_value=1), sg.Radio(text = "Seconds", group_id = "lapse_sec", default=True), sg.Radio(text = "Minutes", group_id = "lapse_sec")],
[sg.Text("   Enter Capture Duration"), sg.Combo([i for i in range(1,61)], key='-DURATION-', size=(4, 1), default_value=1), sg.Radio(text = "Seconds", group_id = "duration_sec", default=True), sg.Radio(text = "Minutes", group_id = "duration_sec")],
[sg.Text("   Enter Movie Frame Rate"), sg.Combo([i for i in range(1,26)], key='-FRAMERATE-', size=(4, 1), default_value=25), sg.Radio(text = "Seconds", group_id = "framerate_sec", default=True), sg.Radio(text = "Minutes", group_id = "framerate_sec")],
[sg.Text("Resulting Movie Length: "), sg.Text("idk", key='-MOVIE_LENGHT-')],
[sg.Button('OK')]
]

# Create the window
window = sg.Window("TimeLapser", layout,)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    print(event, values)
    if event == "OK" or event == sg.WIN_CLOSED:

        window['-MOVIE_LENGHT-'].update(values['-INTERVAL-']*values['-DURATION-'])

window.close()