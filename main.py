from funcoes.cadastrar_livro import cadastrar_livro
from funcoes.cadastrar_usuario import cadastrar_usuario
from funcoes.alugar_livro import alugar_livro
from funcoes.devolver_livro import devolver_livro
from funcoes.consultar_livro import consultar_livro
from funcoes.gerar_relatorio import gerar_relatorio



def menu():
    print("------------------------------------\n----Bem vindo a nossa Biblioteca----\n------------------------------------")

    print("\n====== MENU ======\n")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuario")
    print("3. Alugar livro")
    print("4. Devolver livro")
    print("5. Consultar livro")
    print("6. Gerar Relatório")
    print("0. Sair")


def main():

    menu()

    opcao = input("\nSelecione uma opção: ")


    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        alugar_livro()

    elif opcao == "4":
        devolver_livro()

    elif opcao == "5":
        consultar_livro()

    elif opcao == "6":
        gerar_relatorio()

    elif opcao == "0":
        print("Programa Finalizado!")

    else:
        print("\nOpção inválida. Por favor, selecione uma opção válida.")

        main()
        
if __name__ == "__main__":
    main()