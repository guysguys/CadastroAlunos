from aluno import Aluno
from escola import Escola


def main():
    escola = Escola()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Atualizar dados de aluno")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            matricula = input("Digite a matrícula do aluno: ")
            aluno = Aluno(nome, idade, matricula)
            escola.cadastrar_aluno(aluno)
            print(f"Aluno {nome} cadastrado com sucesso!")

        elif opcao == "2":
            escola.listar_alunos()

        elif opcao == "3":
            matricula = input("Digite a matrícula do aluno que deseja atualizar: ")
            escola.atualizar_aluno(matricula)

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()