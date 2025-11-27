# RADIOBUTTON
from tkinter import *
janela = Tk()

rot1 = Label(janela, text="VOTAÇÃO")
rot1.grid(row=0,column=0)

voto = IntVar()
cand1  = 0
cand2  = 0
cand3  = 0
branco = 0

rad1 = Radiobutton(janela,text="Candidato 1", variable=voto,value=1)
rad1.grid(row=1,column=0)

rad2 = Radiobutton(janela,text="Candidato 2", variable=voto,value=2)
rad2.grid(row=2,column=0)

rad3 = Radiobutton(janela,text="Candidato 3", variable=voto,value=3)
rad3.grid(row=3,column=0)

def confirmar():
    if voto.get() == 1 :
        print("Voto no Candidato 1 confirmado.")
        global cand1
        cand1 += 1
        
    elif voto.get() == 2 :
        print("Voto no Candidato 2 confirmado.")
        global cand2
        cand2 += 1
    
    elif voto.get() == 3 :
        print("Voto no Candidato 3 confirmado.")
        global cand3
        cand3 += 1
    
    else:
        print("Voto em Branco confirmado.")
        global branco
        branco += 1
    
    voto.set(0) # Desmarcar os botões

bot1 = Button(janela,text="Confirmar", width=15, command=confirmar)
bot1.grid(row=4, column=0)

def apuracao():
    print("==APURAÇÃO==")
    print("Candidato 1:", cand1)
    print("Candidato 2:", cand2)
    print("Candidato 3:", cand3)
    print("Branco:", branco)
    print("Total de votos:", cand1+cand2+cand3+branco)

bot2 = Button(janela,text="Apuração", width=15,command=apuracao)
bot2.grid(row=5,column=0)

janela.mainloop()