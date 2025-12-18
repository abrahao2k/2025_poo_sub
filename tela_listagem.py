from tkinter import *
from tkinter import ttk
import csv

def carregar():
    arq = open("alunos.csv",newline="")
    leitor = csv.reader(arq)
    cabecalho = next(leitor) # pular o cabeçalho
    for linha in leitor:
        tabela.insert('', END, values=linha)
    
#################################################################

janela = Tk()
janela.title("Lista de Alunos")
janela.geometry("300x300")

colunas = ("Nome","Curso", "Série")
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=100)

tabela.pack(fill=BOTH, expand=True)

botao = Button(janela, text="Carregar Dados", command=carregar, width=20, bg="yellow")
botao.pack(pady=10)

janela.mainloop()