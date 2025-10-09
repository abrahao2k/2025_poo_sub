class Aluno:
    nome = ""
    curso = ""
    serie = 0
    
    def __init__(self, n, c, s):
        self.nome  = n
        self.curso = c
        self.serie = s
    
    def info(self):
        print(self.nome, self.curso, self.serie)
#######################################################
a1 = Aluno("Ana", "Informática", 2)
a2 = Aluno("Bianca", "Edificações", 4)

a1.info()
a2.info()