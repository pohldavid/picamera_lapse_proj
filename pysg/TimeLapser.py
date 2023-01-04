#! /usr/bin/python3

import PySimpleGUI as sg




#layout=[[sg.Listbox("time", size = (15,1))],[sg.Button("Time")],
#[sg.Listbox("frame_rate")],[sg.Button("Frame Rate")]
#[sg.Listbox("duration")],[sg.Button("Duration")],
#]

layout=[
[sg.Text('Time Lapse Parameters:')],
[sg.Text("Enter Time Lapse Interval"), sg.Combo([i for i in range(1,61)], size=(4, 1), default_value=1), sg.Radio(text = "Seconds", group_id = "lapse_sec", default=True), sg.Radio(text = "Minutes", group_id = "lapse_sec")],
[sg.Text("   Enter Capture Duration"), sg.Combo([i for i in range(1,61)], size=(4, 1), default_value=1), sg.Radio(text = "Seconds", group_id = "duration_sec", default=True), sg.Radio(text = "Minutes", group_id = "duration_sec")],
[sg.Text("Resulting Movie Length: "), sg.Text("idk")],
]

# Create the window
window = sg.Window("TimeLapser", layout, size =(600,400))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()