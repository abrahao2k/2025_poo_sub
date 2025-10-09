class Livro:
    titulo = ""
    autor  = ""
    preco  = 0
    
    def info(self):
        print("--- DADOS DO LIVRO ---")
        print("Título:", self.titulo)
        print("Autor:",  self.autor)
        print("Preço:",  self.preco)

#########################################################
liv1 = Livro()
liv1.titulo = "O Hobbit"
liv1.autor = "J.R.R.Tolkien"
liv1.preco = 39.95
liv1.info()

liv2 = Livro()
liv2.titulo = "Harry Potter"
liv2.autor = "J.K.Rowling"
liv2.preco = 24.99
liv2.info()