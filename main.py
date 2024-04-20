from funcoes.cadastrar_livro import cadastrar_livro
from funcoes.cadastrar_usuario import cadastrar_usuario
from funcoes.emprestimo import emprestar_livro

print("------------------------------------\n----Bem vindo a nossa Biblioteca----\n------------------------------------")

def menu():
    print("\n=====MENU=====")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuario")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Consultar livro")
    print("6. Gerar Relatório")
    print("0. Sair")


def main():

    menu()

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        emprestar_livro()

    # elif opcao == 4:

    # elif opcao == 5:

    # elif opcao == 6:

    # elif opcao == 0:

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
        
if __name__ == "__main__":
    main()