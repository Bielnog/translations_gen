import PySimpleGUI as sg


def make_window():
    layout = make_layout()
    window = sg.Window(
        "Translations Gen", layout, background_color="black", size=(500, 300)
    )
    return window


def make_layout():
    layout = [
        [
            sg.Text(
                "Tag a ser gerada:",
                text_color="white",
                background_color="black",
                size=(20, 1),
            ),
        ],
        [
            sg.InputText(
                key="-TAG-",
                background_color="#e8e8e8",
                text_color="black",
                size=(100, 1),
                default_text="i18n_tag_",
            ),
        ],
        [
            sg.Text(
                "Frase a ser traduzida(pt-br):",
                text_color="white",
                background_color="black",
                size=(20, 1),
            ),
        ],
        [
            sg.Multiline(
                key="-FRASE-",
                background_color="#e8e8e8",
                text_color="black",
                size=(100, 3),
            ),
        ],
        [sg.Button("Salvar"), sg.Button("Cancelar")],
    ]
    return layout
