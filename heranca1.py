class Pessoa:
    nome = "__"
    telefone ="__"
    email = "__"
    endereco = "__"
    
    def info(self):
        print(self.nome, self.telefone, self.email, self.endereco)

##############################################
class Aluno(Pessoa):  # Aluno herda de Pessoa
    curso = ""
    
    def info(self):
        super().info() # executa o código da classe pai
        print(self.curso)
        
        
##############################################
a1 = Aluno()
a1.nome = "Pedro"
a1.curso = "Informática"
a1.info() # sobrescrita (comportamento diferente do pai)



'''
p1 = Pessoa()
p1.nome = "Joao"
p1.telefone = "1234"
p1.email = "joao@gmail.com"
p1.endereco = "Rua A, 25"
p1.info()
'''