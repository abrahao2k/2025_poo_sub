from tkinter import *

janela = Tk()
janela.geometry("300x150")

entrada = Entry(janela, show="*") # transforma em senha (show="*")
entrada.grid(row=0, column=0)

entrada["width"] = 20 # largura do campo (caracteres)
entrada["bg"] = "yellow"  # cor fundo
entrada["fg"] = "red" # cor letra

entrada["font"] = ("Arial",18) # tipo/tamanho da letra
entrada["justify"] = "center" # alinhamento do texto (left/center/right)

entrada["bd"] = 5 #borda
entrada["relief"] = "ridge" # estilo da borda  ("flat", "sunken", "raised", "groove")

janela.mainloop()