from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def novo(event=None):
    area_texto.delete(1.0, END)

def abrir(event=None):
    caminho = filedialog.askopenfilename()
    
    if caminho:
        arq = open(caminho,"r")
        conteudo = arq.read()
        area_texto.delete(1.0, END)
        area_texto.insert(END,conteudo)
        arq.close()
######################################################################        

def salvar(event=None):
    caminho = filedialog.asksaveasfilename()
    
    if caminho:
        arq = open(caminho,"w")
        conteudo = area_texto.get(1.0, END)
        arq.write(conteudo)
        arq.close()
        messagebox.showinfo(message="Arquivo gravado com sucesso.")
        
######################################################################

janela = Tk()
janela.title("Bloco de Notas")
janela.geometry("600x400")

area_texto = Text(janela, wrap="word")
area_texto.pack(expand=1, fill="both") 

barra_menu = Menu(janela)

menu_arquivo = Menu(barra_menu, tearoff=0)

menu_arquivo.add_command(label="Novo", command=novo,
                         underline=0,accelerator="Ctrl+N")
janela.bind_all("<Control-n>", novo)

menu_arquivo.add_command(label="Abrir", command=abrir,
                         underline=1,accelerator="Ctrl+A")
janela.bind_all("<Control-a>", abrir)

menu_arquivo.add_command(label="Salvar", command=salvar,
                         underline=3,accelerator="Ctrl+S")
janela.bind_all("<Control-s>", salvar)

menu_arquivo.add_separator()

menu_arquivo.add_command(label="Sair", command=quit,
                         underline=3,accelerator="Alt+F4")

barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo,
                       underline=0)

janela.config(menu=barra_menu)
janela.mainloop()

