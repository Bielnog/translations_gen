import PySimpleGUI as sg

def processar_eventos(event, values):
    if event == 'Salvar':
        nome = values['-NOME-']
        idade = values['-IDADE-']
        sg.popup(f'Nome: {nome}\nIdade: {idade}')
    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        return False
    return True
