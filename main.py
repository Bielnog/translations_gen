import PySimpleGUI as sg
from layout import make_window
from events import processar_eventos

def main():
    window = make_window()

    while True:
        event, values = window.read()
        if not processar_eventos(event, values):
            break

    window.close()

if __name__ == "__main__":
    main()
