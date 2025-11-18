from tkinter import *
from tkinter import messagebox
janela = Tk()
janela.geometry("300x150")

rotulo = Label(janela, text="Qual é o seu nome?")
rotulo.grid(row=0, column=0)

entrada = Entry(janela)
entrada.grid(row=1, column=0)

def bemvindo():
    messagebox.showinfo("Bemvindo", f"Bem vindo, {entrada.get()}!")

botao = Button(janela, text="Confirmar")
botao.grid(row=2, column=0)
botao["command"] = bemvindo

janela.mainloop() # exibir a janela