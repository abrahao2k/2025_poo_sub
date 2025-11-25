from tkinter import *
from tkinter import messagebox

def verificar():
    usu = ent1.get()
    sen = ent2.get()
    if usu == "admin" and sen == "987":
        abrir_menu() # abrir janela principal
    else:
        messagebox.showerror("Erro","Usuário/Senha incorreto.")

def abrir_menu():
    janela.destroy()  # fechar a tela
    menu = Tk()
    menu.geometry("300x200")
    menu.title("SISTEMA LEGAL v.1.0")
    menu.mainloop()

janela = Tk()
janela.geometry("300x100")
janela.title("ACESSO AO SISTEMA")

rot1 = Label(janela,text="Usuário:")
rot1.grid(row=0,column=0)

rot1 = Label(janela,text="Senha:")
rot1.grid(row=1,column=0)

ent1 = Entry(janela)
ent1.grid(row=0, column=1)

ent2 = Entry(janela, show="*")
ent2.grid(row=1,column=1)

but1 = Button(janela,text="ENTRAR",command=verificar)
but1.grid(row=2,column=1)

janela.mainloop()