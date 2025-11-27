# CHECKBUTTON
from tkinter import *
janela = Tk()
janela.title("Musicas")
janela.geometry("250x100")

rot1 = Label(janela,text="GÊNERO MUSICAL")
rot1.grid(row=0,column=0)

sertanejo = IntVar()
check1 = Checkbutton(janela, text="Sertanejo", variable=sertanejo)
check1.grid(row=1,column=0)

rock = IntVar()
check2 = Checkbutton(janela, text="Rock", variable=rock)
check2.grid(row=1,column=1)

def validar():
    if sertanejo.get() == 1 :
        print("Você gosta de sertanejo.")
    
    if rock.get() == 1 :
        print("Você gosta de rock.")

but1 = Button(janela, text="Confirmar", command=validar)
but1.grid(row=2,column=0)

janela.mainloop()