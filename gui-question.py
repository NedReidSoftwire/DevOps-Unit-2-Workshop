import PySimpleGUI as sg

# TODO: Integrate this question with pub-quiz.py
question = "What is the capital of France?"
options = ["London", "Paris", "Berlin", "Madrid"]
answer = 1

option_buttons = [sg.Button(option) for option in options]
layout = [
    [sg.Text(question)],
    option_buttons
]

window = sg.Window('Pub quiz', layout)

def update_button_colours(selected):
    for i in range(len(option_buttons)):
        if i == answer:
            option_buttons[i].update(button_color="green", disabled=True)
        elif options[i] == selected:
            option_buttons[i].update(button_color="red", disabled=True)
        else:
            option_buttons[i].update(button_color="#292929", disabled=True)


while True:
    event, values = window.read()
    if event == "Continue" or event == sg.WIN_CLOSED:
        break
    elif event:
        update_button_colours(event)
        window.extend_layout(window, [[sg.Push(), sg.Button("Continue"), sg.Push()]])