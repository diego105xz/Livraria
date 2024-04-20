import db_conexao
from psycopg2 import Error

def cadastrar_livro():
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = input("Digite o ano da publicação do livro: ")
        copias = int(input("Digite o número de cópias disponíveis: "))

        cursor.execute("INSERT INTO livros (titulo, autor, ano, copias) VALUES (%s, %s, %s, %s)", (titulo, autor, ano, copias))
        conn.commit()
        print("Livro cadastrado com sucesso!")

        cursor.close()
        conn.close()

    except (Exception, Error) as error:
        print("Erro ao cadastrar o livro:", error)