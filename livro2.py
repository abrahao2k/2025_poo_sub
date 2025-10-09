class Livro:
    titulo = ""
    autor  = ""
    preco  = 0
    
    def __init__(self, t, a, p):  # Construtor personalizado
        self.titulo = t
        self.autor = a
        
        # testar se o valor é positivo        
        if p < 0 : self.preco = 0
        else:      self.preco = p
        
        # testar se é texto
        # if isinstance(p, str):
        
    def info(self):
        print("--- DADOS DO LIVRO ---")
        print("Título:", self.titulo)
        print(" Autor:",  self.autor)
        print(" Preço:",  self.preco, "\n")
        
#####################################################
liv3 = Livro("2666","Roberto Bolano",45.83)  # Passa valores ao criar
liv3.info()

liv4 = Livro("A Primeira Mentira", "Ashley Elston", -53) #não aceita negativo
liv4.info()