from tkinter import *
import csv
import os
from tkinter import messagebox

def salvar():
    nome = ent_nome.get()
    curso = ent_curso.get()
    serie = ent_serie.get()
    #print(nome,curso,serie)
    
    existe = os.path.exists("alunos.csv")            #verifica se o arq existe
    
    arquivo = open("alunos.csv","a",newline="") #abre o arquivo
    gravador = csv.writer(arquivo)              #objeto que grava os dados
    
    if not existe:
        gravador.writerow(["Nome","Curso","Série"])  #grava cabeçalho se não existe
    
    gravador.writerow([nome, curso, serie])     #realiza a gravação
    arquivo.close()                             #fecha arquivo
    
    messagebox.showinfo("Confirmação","Gravado com sucesso.")
    
    ent_nome.delete(0,END)
    ent_curso.delete(0,END)
    ent_serie.delete(0,END)
    ent_nome.focus()          # selecionar esse campo

## UI ###################################################    

janela = Tk()
janela.geometry("300x100")
janela.title("Cadastro de Alunos")

rot_nome = Label(janela,text="Nome:")
rot_nome.grid(row=0,column=0)
ent_nome = Entry(janela,width=40)
ent_nome.grid(row=0,column=1)

rot_curso = Label(janela,text="Curso:")
rot_curso.grid(row=1,column=0)
ent_curso = Entry(janela,width=40)
ent_curso.grid(row=1,column=1)

rot_serie = Label(janela,text="Série:")
rot_serie.grid(row=2,column=0)
ent_serie = Entry(janela,width=40)
ent_serie.grid(row=2,column=1)

bot_salvar = Button(janela,text="Salvar",
                    bg="green", fg="white",
                    width=20, command=salvar)
bot_salvar.grid(row=3,column=1)

janela.mainloop()