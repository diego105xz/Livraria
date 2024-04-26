import db_conexao
from psycopg2 import Error

def devolver_livro():

    print("\nLivros pendentes de devolução: ")

    try:

        conn = db_conexao.conectar()
        cursor = conn.cursor()

        sql_exibir_livros_devolucao = """
            SELECT 
                b.id_emprestimo AS numero_emprestimo,
                a.nome AS alugado_por,
                c.titulo,
                b.status,
                b.data_emprestimo,
                b.data_devolucao
            FROM
                usuarios a
            JOIN
                emprestimo b ON a.id_usuario = b.id_usuario 
            JOIN 
                livros c ON c.id_livro = b.id_livro 
            WHERE 
                b.status = 'alugado'
            ORDER BY
                a.nome
        """

        cursor.execute(sql_exibir_livros_devolucao)
        livros_pendentes = cursor.fetchall()

        if not livros_pendentes:
            print("Não há livros pendentes de devolução.")

            cursor.close()
            conn.close()

        else:
            for id_emprestimo, aulgador_por, titulo, status, dt_emp, dt_dev in livros_pendentes:
                print(f"|Número Devolução: {id_emprestimo:<5}| Responsável: {aulgador_por:<20}| Título: {titulo:<30}| Status: {status:<10}| Empréstimo: {dt_emp} | Devolução: {dt_dev} |")

            escolha_devolucao_numero = input("\nInforme o número da devolução do livro: ")

            if escolha_devolucao_numero.isdigit():
                escolha_devolucao_numero = int(escolha_devolucao_numero)
                if escolha_devolucao_numero > 0:
                    sql_devolver_livro = """
                        UPDATE 
                            emprestimo 
                        SET 
                            status = 'devolvido'
                        WHERE 
                            id_emprestimo = %s
                    """
                    cursor.execute(sql_devolver_livro, (escolha_devolucao_numero,))
                    conn.commit()

                    cursor.close()
                    conn.close()
                    
                    print("\nLivro devolvido com sucesso!")
                else:
                    print("\nNúmero inválido")  
                    cursor.close()
                    conn.close()
            else:
                print("\nNúmero inválido")  
                cursor.close()
                conn.close()
                
        from main import main
        main()

    except Error as error:
        print("\nErro ao consultar livros pendentes de devolução: ", error)
        cursor.close()
        conn.close()