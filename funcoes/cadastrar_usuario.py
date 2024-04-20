import db_conexao
from psycopg2 import Error

def cadastrar_usuario():
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        nome = input("Digite o nome de usuario: ")
        tel = input("Digite o telefone: ")
        email = input("Digite o email: ")

        cursor.execute("INSERT INTO usuarios (nome, tel, email) VALUES (%s, %s, %s)", (nome, tel, email))
        conn.commit()
        print("Usuário cadastrado com sucesso!")

        cursor.close()
        conn.close()

    except (Exception, Error) as error:
        print("Erro ao cadastrar o usuário:", error)