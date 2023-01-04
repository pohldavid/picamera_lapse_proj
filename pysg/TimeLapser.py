#! /usr/bin/python3

import PySimpleGUI as sg




#layout=[[sg.Listbox("time", size = (15,1))],[sg.Button("Time")],
#[sg.Listbox("frame_rate")],[sg.Button("Frame Rate")]
#[sg.Listbox("duration")],[sg.Button("Duration")],
#]

timelist =  []
for i in range(1,26):
    timelist.append(i)

layout=[[sg.Combo(timelist), sg.Combo([i for i in range(10)]), sg.Combo([i for i in range(1,26)])],
[sg.Button("Time"), sg.Button("Duration"), sg.Button("Frame Rate")]
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