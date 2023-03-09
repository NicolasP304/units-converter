import PySimpleGUI as sg 

layout = [
    [
        [[sg.Text('Input:')], sg.Input(key = '-INPUT-')],
        [[sg.Text('Units:')], sg.Spin(['m to km', 'g to kg'], key = '-UNITS-')],
        [sg.Button('Convert', key = '-CONVERT-')]
    ],
    [sg.Text('Result:', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'm to km':
                    output =  float(input_value) / 1000
                case 'g to kg':
                    output = float(input_value) / 1000
            window['-OUTPUT-'].update(output)
        else:
            window['-OUTPUT-'].update('Please enter a number')
    

    
window.close()