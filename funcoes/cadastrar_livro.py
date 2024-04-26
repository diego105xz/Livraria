import db_conexao
from psycopg2 import Error

def cadastrar_livro():
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        titulo = input("\nDigite o título do livro: ")
        autor = input("\nDigite o autor do livro: ")
        ano = input("\nDigite o ano da publicação do livro: ")
        copias = int(input("\nDigite o número de cópias disponíveis: "))

        cursor.execute("INSERT INTO livros (titulo, autor, ano, copias) VALUES (%s, %s, %s, %s)", (titulo, autor, ano, copias))
        conn.commit()
        print("\nLivro cadastrado com sucesso!")

        cursor.close()
        conn.close()

        from main import main
        main() 

    except (Exception, Error) as error:
        print("\nErro ao cadastrar o livro:", error)