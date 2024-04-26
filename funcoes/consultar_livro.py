import db_conexao
from psycopg2 import Error

def consultar_livro():

    try:

        print("\nConsultar livro: ")
        print("1. Por título: ")
        print("2. Por autor: ")
        print("3. Por Ano da publicação")

        numero_consulta = input("\nInforme o número da consulta: \n")

        try:
            numero_consulta = int(numero_consulta)
        except ValueError:
            print("\nPor favor, insira um número válido para a consulta.\n")
            return
        

        if numero_consulta == 1:
            print("\nConsulta por título: \n")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            pesquisar_titulo = input("\nInforme o título: \n")


            sql_consulta_titulo = """
                SELECT 
                    titulo,
                    autor,
                    ano,
                    copias 
                FROM
                    livros
                WHERE 
                    UPPER(titulo) LIKE UPPER(%s)
                ORDER BY
                    titulo
            """

            cursor.execute(sql_consulta_titulo, (f'%{pesquisar_titulo}%',))
            resultados = cursor.fetchall()

            
            if resultados:
                print("Resultado encontrado: \n")

                for titulo, autor, ano, copias in resultados:
                    print(f"| Título: {titulo:<40} | Autor: {autor:<25} | Ano: {ano:<5} | Cópias: {copias:<3}|")

                cursor.close()
                conn.close()    
            else:
                print("\nResultado não encontrado!\n")

            cursor.close()
            conn.close()


        elif numero_consulta == 2:
            print("\nConsulta por autor: \n")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            pesquisar_autor = input("\nInforme o autor: \n")


            sql_consulta_autor = """
                SELECT 
                    autor,
                    titulo,
                    ano,
                    copias 
                FROM
                    livros
                WHERE 
                    UPPER(autor) LIKE UPPER(%s)
                ORDER BY
                    autor
            """

            cursor.execute(sql_consulta_autor, (f'%{pesquisar_autor}%',))
            resultados = cursor.fetchall()

            
            if resultados:
                print("\nResultado encontrado: \n")

                for autor, titulo, ano, copias in resultados:
                    print(f"| Autor: {autor:<25} | Título: {titulo:<40} | Ano: {ano:<5} | Cópias: {copias:<3}|")

                cursor.close()
                conn.close()    
            else:
                print("\nResultado não encontrado!\n")

            cursor.close()
            conn.close()



        elif numero_consulta == 3:
            print("\nConsulta por ano da publicação: \n")
            
            conn = db_conexao.conectar()
            cursor = conn.cursor()

            pesquisar_ano = input("\nInforme o ano da publicação: \n")


            sql_consulta_ano = """
                SELECT 
                    ano,
                    titulo,
                    autor,
                    copias 
                FROM
                    livros
                WHERE 
                    ano LIKE %s
                ORDER BY
                    ano
            """

            cursor.execute(sql_consulta_ano, (f'%{pesquisar_ano}%',))
            resultados = cursor.fetchall()

            
            if resultados:
                print("\nResultado encontrado: \n")

                for ano, titulo, autor, copias in resultados:
                    print(f"| Ano: {ano:<5} | Título: {titulo:<40} | Autor: {autor:<25} |  Cópias: {copias:<3}|")

                cursor.close()
                conn.close()    
            else:
                print("\nResultado não encontrado!\n")

            cursor.close()
            conn.close()
        else:
            print("\nNúmero inválido!\n")

        from main import main
        main()

    except Error as error:
        print("\nErro ao consultar livros: ", error)
        cursor.close()
        conn.close()