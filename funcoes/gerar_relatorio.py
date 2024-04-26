import db_conexao
from psycopg2 import Error

def gerar_relatorio():

    try:

        print("\nRelatórios")
        print("1. Livros disponíveis: ")
        print("2. Livros alugados: ")
        print("3. Livros com atraso de devolução: ")
        print("4. Usuários cadastrados: ")


        numero_relatorio = input("\nEscolha qual relatório deseja: ")

        if numero_relatorio == "1":

            print("\nRelatório de Livros disponíveis: ")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            sql_relatorio_livros_disponiveis = """
                SELECT 
                    a.titulo, 
                    a.copias - COALESCE(SUM(CASE WHEN b.status = 'alugado' THEN 1 ELSE 0 END), 0) AS disponiveis
                FROM 
                    livros a
                LEFT JOIN 
                    emprestimo b 
                ON 
                    a.id_livro = b.id_livro 
                GROUP BY 
                    a.id_livro, a.titulo, a.copias
                HAVING 
                    a.copias - COALESCE(SUM(CASE WHEN b.status = 'alugado' THEN 1 ELSE 0 END), 0) > 0
                ORDER BY 
                    a.titulo
            """

            cursor.execute(sql_relatorio_livros_disponiveis)

            if cursor.rowcount == 0:
                print("\nNão há livros disponíveis")

                cursor.close()
                conn.close()

            else:
                relatorio_livros_disponiveis = cursor.fetchall()

                for titulo, copias in relatorio_livros_disponiveis:
                    print(f"| Título: {titulo:<35} | Disponíveis: {copias:>2} | ")
    
                cursor.close()
                conn.close()

        elif numero_relatorio == "2":
            print("\nRelatório de Livros alugados: ")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            sql_relatorio_livros_alugados = """
                SELECT 
                    a.titulo,
                    a.autor,
                    a.ano,
                    COALESCE(b.alugadas, 0) AS copias_alugadas
                FROM
                    livros a
                LEFT JOIN
                    (SELECT 
                        id_livro,
                        COUNT(*) AS alugadas
                    FROM
                        emprestimo
                    WHERE
                        status = 'alugado'
                    GROUP BY id_livro) b ON a.id_livro = b.id_livro
                WHERE
                    a.id_livro IN (SELECT id_livro FROM emprestimo WHERE status = 'alugado')
                ORDER BY
                    a.titulo
            """

            cursor.execute(sql_relatorio_livros_alugados)

            if cursor.rowcount == "0":
                print("\nNão há livros alugados.")          

                cursor.close()
                conn.close()
            else:
                relatorio_livros_alugados = cursor.fetchall()
                for titulo, autor, ano, copias in relatorio_livros_alugados:
                    print(f"| Título: {titulo:<35} | Autor: {autor} | Ano: {ano} | Cópias alugadas: {copias:>2} | ")

                cursor.close()
                conn.close()
        
        elif numero_relatorio == "3":
            print("\nRelatório de livros atrasados devolução: ")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            sql_relatorio_atraso_devolucao = """
                SELECT 
                    a.titulo,
                    c.nome,
                    b.data_devolucao
                FROM 
                    livros a
                JOIN 
                    emprestimo b ON a.id_livro = b.id_livro 
                join
                    usuarios c on b.id_usuario = c.id_usuario 	
                WHERE 
                    b.status = 'alugado' 
                    AND b.data_devolucao < CURRENT_TIMESTAMP
                ORDER BY 
                    a.titulo
            """

            cursor.execute(sql_relatorio_atraso_devolucao)

            if cursor.rowcount == "0":
                print("\nNão temos livros com atraso de devolução!")

                cursor.close()
                conn.close()
            else:
                relatorio_atraso_devolucao = cursor.fetchall()
                for titulo, nome, dt_devolucao in relatorio_atraso_devolucao:
                    print(f"\n| Título: {titulo:<30} | Cliente: {nome:<20} | Data de Devolução: {dt_devolucao} |") 

                cursor.close()
                conn.close()    

        elif numero_relatorio == "4":
            print("\nRelatório de usuários cadastrados: ")

            conn = db_conexao.conectar()
            cursor = conn.cursor()

            sql_relatorio_usuarios_cadastrados = """
                SELECT 
                    id_usuario,
                    nome,
                    tel,
                    email
                FROM 
                    usuarios
                ORDER BY nome 
            """

            cursor.execute(sql_relatorio_usuarios_cadastrados)

            if cursor.rowcount == "0":
                print("\nNão temos usuários cadatrados!")
                
                cursor.close()
                conn.close()
            else:
                relatorio_usuarios_cadastrados = cursor.fetchall()
                for matricula, nome, tel, email in relatorio_usuarios_cadastrados:
                    print(f"| Matrícula: {matricula} | Cliente: {nome:<20} | Telefone: {tel:<15} | E-mail: {email:<25} |")

                cursor.close()
                conn.close()
        else:
            print("\nNúmero inválido!")

        from main import main
        main()

    except Error as error:
        print("\nErro ao exibir os relatórios ", error)
        cursor.close()
        conn.close()