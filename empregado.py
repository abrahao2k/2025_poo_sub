class Empregado:
    
    nome = ""
    salario = 0
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome;    
    
    def getSalario(self):
        return self.salario
    
    def setSalario(self, salario):
        self.salario = salario

    def info(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)

#################################################
        
class Gerente(Empregado):
    
    departamento = ""
    
    def __init__(self, nome, salario, dep):
        self.nome = nome
        self.salario = salario
        self.departamento = dep
    
    def getDepartamento(self):
        return self.departamento
    
    def setDepartamento(self, dep):
        self.departamento = dep
    
    def info(self):
        super().info()
        print("Departamento:", self.departamento)
    
    
    