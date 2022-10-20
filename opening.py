import PySimpleGUI as sg
import ChBOT


def opening():
    layout = [[sg.Text("Chesterbot v0.1")], [sg.Button("ABRIR")]]

    # Create the window
    window = sg.Window("Demo", layout, margins=(100, 50))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "ABRIR":
            ChBOT.ChBot()
            break
        elif event == sg.WIN_CLOSED:
            break


    window.close()

opening()