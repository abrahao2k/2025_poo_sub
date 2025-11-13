from tkinter import *
janela = Tk()

texto1 = "Esse texto\ntem mais de\numa linha."

r1 = Label(janela, text= texto1, justify="right")
r1.grid(row=0,column=0)

logo = PhotoImage(file="xbox.png")
r2 = Label(janela, image = logo)
r2.grid(row=0,column=1)

but = Button(janela, text="SAIR", width=15)
but.grid(row=1,column=0)
but["fg"] = "red"
but["bg"] = "pink"
but["command"] = quit

b2 = Button(janela, text="IMPRIMIR", width=15)
b2.grid(row=2,column=0)

def imprimir():
    print("...estou imprimindo...")

b2["command"] = imprimir  # sem parenteses

janela.mainloop()