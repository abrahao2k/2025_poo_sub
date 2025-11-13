from tkinter import *
janela = Tk()

rotulo = Label(janela,text="Olá, Pessoal!")
rotulo.grid(row=0,column=0)
rotulo["font"] = ("Arial","18","bold")
rotulo["fg"] = "red"
rotulo["bg"] = "yellow"

rotulo2 = Label(janela,text="Tudo bem?")
rotulo2.grid(row=1,column=1)
rotulo2["font"] = ("Consolas","22","italic")
rotulo2["fg"] = "green"
rotulo2["bg"] = "black"

rotulo3 = Label(janela, text="OK",
                fg="blue", bg="white")
rotulo3.grid(row=2,column=2)

janela.mainloop() # exibir janela