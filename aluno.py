from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def __str__(self):
        return f"{super().__str__()} - Matrícula: {self.matricula}"
