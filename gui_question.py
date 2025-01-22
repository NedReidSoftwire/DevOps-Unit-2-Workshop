import PySimpleGUI as sg

def update_button_colours(selected, option_buttons, options, answer):
    for i in range(len(option_buttons)):
        if i == answer:
            option_buttons[i].update(button_color="green", disabled=True)
        elif options[i] == selected:
            option_buttons[i].update(button_color="red", disabled=True)
        else:
            option_buttons[i].update(button_color="#292929", disabled=True)

def show_gui_question(question: str, options: list[str], answer: int):
    option_buttons = [sg.Button(option) for option in options]
    layout = [
        [sg.Text(question, size=(40, None))],
        option_buttons
    ]

    window = sg.Window('Pub quiz', layout)

    while True:
        event, values = window.read()
        if event == "Continue" or event == sg.WIN_CLOSED:
            break
        elif event:
            update_button_colours(event, option_buttons, options, answer)
            window.extend_layout(window, [[sg.Push(), sg.Button("Continue"), sg.Push()]])

    window.close()