from tkinter import *
janela = Tk()
janela.geometry("200x150")

r1 = Label(janela, text="Valor1:").grid(row=0,column=0)
e1 = Entry(janela)
e1.grid(row=0,column=1)

r2 = Label(janela, text="Valor2:").grid(row=1,column=0)
e2 = Entry(janela)
e2.grid(row=1,column=1)

def calcular():
    v1 = int(e1.get()) # captura o texto / converte pra int
    v2 = int(e2.get())
    soma = v1 + v2
    e3.delete(0, len(e3.get())) # excluir o texto na posição indicada
    e3.insert(0, str(soma))  # inserir texto na posição indicada do campo
    e3["state"] = "readonly" # bloqueia o campo

b1 = Button(janela,text="Calcular")
b1.grid(row=2,column=1)
b1["command"] = calcular

r3 = Label(janela, text="Total:").grid(row=3,column=0)
e3 = Entry(janela)
e3.grid(row=3, column=1)

def limpar():
    e3["state"] = "normal"  # libera o campo
    e1.delete(0, len(e1.get()))
    e2.delete(0, len(e2.get()))
    e3.delete(0, len(e3.get()))
    e1.focus() # põe o cursor no primeiro entry

b2 = Button(janela,text="Limpar")
b2.grid(row=4,column=1)
b2["command"] = limpar

janela.mainloop()