from tkinter import *
janela = Tk()
janela.title("Meu programa")
# largura x altura +x +y
janela.geometry("400x250+300+200")
# redimensionamento
janela.resizable(width=False,height=False)
# cor de fundo (nome ou código hexa)
janela.configure(bg="#FF5733") # blue, red, green, etc..,
# manter em primeiro plano
janela.attributes("-topmost", True)
janela.mainloop()  # dsd sd s df