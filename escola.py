class Escola:
    def __init__(self):
        self.alunos = []  # Lista para armazenar alunos cadastrados

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)  # Adiciona um aluno na lista

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("\nLista de Alunos:")
            for aluno in self.alunos:
                print(aluno)

    def atualizar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print(f"Atualizando dados do aluno {aluno.nome}")
                aluno.nome = input("Digite o novo nome: ")
                aluno.idade = int(input("Digite a nova idade: "))
                print("Dados atualizados com sucesso!")
                return
        print("Aluno não encontrado!")