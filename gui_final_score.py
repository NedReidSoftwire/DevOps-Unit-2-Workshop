import PySimpleGUI as sg

def show_gui_score(final_score_text: str, goodbye_text: str):
    layout = [
        [sg.Text(goodbye_text, justification='center', size=(40, None))],
        [sg.Text(final_score_text, justification='center', size=(40, None))],
        [[sg.Push(), sg.Button("OK"), sg.Push()]]
    ]

    window = sg.Window('Pub quiz', layout)

    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()