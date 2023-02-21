import PySimpleGUI as sg
import testes as t

sg.theme('DarkPurple4')

x_ativado = 0
o_ativado = 0

lista_teste = [[], [], [],
               [], [], [],
               [], [], []]

pontos_x = 0
pontos_o = 0

layout_cima = [
    [sg.Push(), sg.Button('', size=(10, 5), key='-1-'),
     sg.Button('', size=(10, 5), key='-2-'),
     sg.Button('', size=(10, 5), key='-3-'), sg.Push()],

    [sg.Push(), sg.Button('', size=(10, 5), key='-4-'),
     sg.Button('', size=(10, 5), key='-5-'),
     sg.Button('', size=(10, 5), key='-6-'), sg.Push()],

    [sg.Push(), sg.Button('', size=(10, 5), key='-7-'),
     sg.Button('', size=(10, 5), key='-8-'),
     sg.Button('', size=(10, 5), key='-9-'), sg.Push()]
]

layout_baixo = [
    [sg.Push(), sg.Button('Jogador X', key='-jogadorx-'), sg.Push(),
     sg.Button(f'{pontos_x} pontos        |||        {pontos_o} pontos', key='-PONTUAÇÃO-', disabled=True),
     sg.Button('Jogador O', key='-jogadoro-'), sg.Push()]
]

layout = [
    [layout_cima],
    [sg.HSeparator()],
    [layout_baixo]
]

window = sg.Window("Jogo da Velha",
                   layout=layout
                   )

while True:

    events, values = window.read()

    match events:
        case '-jogadorx-':
            window['-jogadorx-'].update(disabled=True)
            window['-jogadoro-'].update(disabled=False)
            x_ativado = 1
            o_ativado = 0

        case '-jogadoro-':
            window['-jogadoro-'].update(disabled=True)
            window['-jogadorx-'].update(disabled=False)
            x_ativado = 0
            o_ativado = 1

    if x_ativado == 1:
        match events:
            case '-1-':
                window['-1-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                um = 1
                lista_teste[0] = 1

            case '-2-':
                window['-2-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                dois = 1
                lista_teste[1] = 1

            case '-3-':
                window['-3-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                tres = 1
                lista_teste[2] = 1

            case '-4-':
                window['-4-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                quatro = 1
                lista_teste[3] = 1

            case '-5-':
                window['-5-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                cinco = 1
                lista_teste[4] = 1

            case '-6-':
                window['-6-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                seis = 1
                lista_teste[5] = 1

            case '-7-':
                window['-7-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                sete = 1
                lista_teste[6] = 1

            case '-8-':
                window['-8-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                oito = 1
                lista_teste[7] = 1

            case '-9-':
                window['-9-'].update(disabled=True, button_color=(sg.theme_background_color('Black')))
                nove = 1
                lista_teste[8] = 1

    print(lista_teste)

    if o_ativado == 1:
        match events:
            case '-1-':
                window['-1-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[0] = 2


            case '-2-':
                window['-2-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[1] = 2

            case '-3-':
                window['-3-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[2] = 2

            case '-4-':
                window['-4-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[3] = 2

            case '-5-':
                window['-5-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[4] = 2

            case '-6-':
                window['-6-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[5] = 2

            case '-7-':
                window['-7-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[6] = 2

            case '-8-':
                window['-8-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[7] = 2

            case '-9-':
                window['-9-'].update(disabled=True, button_color=(sg.theme_background_color('Red')))
                lista_teste[8] = 2

    if t.resultado(lista_teste):

        if t.resultado(lista_teste) == 'jogador X ganhou':
            pontos_x += 1
            sg.popup_ok(t.resultado(lista_teste))

        if t.resultado(lista_teste) == 'jogador O ganhou':
            pontos_o += 1
            sg.popup(t.resultado(lista_teste))

        lista_teste = [[], [], [],
                       [], [], [],
                       [], [], []]

        window['-1-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-2-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-3-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-4-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-5-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-6-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-7-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-8-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))
        window['-9-'].update(disabled=False, button_color=(sg.theme_background_color('#382039')))

    window['-PONTUAÇÃO-'].update(f'{pontos_x} pontos        |||        {pontos_o} pontos')

    if events is None:
        break

window.close()
