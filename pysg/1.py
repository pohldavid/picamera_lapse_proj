#! /usr/bin/python3

import PySimpleGUI as sg

layout = [
    [sg.Text("Enter"), sg.Input(key="-IN-")],
    [sg.Text("text goes here", key="-OUT-")],
    [sg.Button("Ok"), sg.Button("Exit")],
]

window = sg.Window("Title", layout)

while True:
    event, values = window.read()
    if event is None or event == "Exit":
        break
    window["-OUT-"].update(values["-IN-"])

window.close()
