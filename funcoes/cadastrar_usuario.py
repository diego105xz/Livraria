import db_conexao
from psycopg2 import Error

def cadastrar_usuario():
    try:
        conn = db_conexao.conectar()
        cursor = conn.cursor()

        nome = input("\nDigite o nome de usuário: ")
        tel = input("\nDigite o telefone: ")
        email = input("\nDigite o email: ")

        cursor.execute("INSERT INTO usuarios (nome, tel, email) VALUES (%s, %s, %s)", (nome, tel, email))
        conn.commit()
        print("\nUsuário cadastrado com sucesso!")

        cursor.close()
        conn.close()
        
        from main import main
        main() 

    except (Exception, Error) as error:
        print("\nErro ao cadastrar o usuário:", error)