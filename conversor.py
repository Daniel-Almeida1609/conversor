import pandas as pd
import PySimpleGUI as sg


def escolhe_arquivo():
    sg.theme("DarkBlue")
    layout = [
        [sg.Text("Escolha o arquivo: "), sg.Input(key="-IN-"), sg.FileBrowse()],
        [sg.Button("Ok"), sg.Button("Cancelar")],
    ]
    janela = sg.Window("Conversor", layout, size=(680, 90), font=50)

    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        elif event == "Ok":
            arq = values["-IN-"]
            return arq


def txt_excel(arq):
    df = pd.read_table(arq)
    df.to_excel("123.xlsx", index=False)


def txt_csv(arq):
    df = pd.read_table(arq)
    df.to_csv("123.csv", index=False)
