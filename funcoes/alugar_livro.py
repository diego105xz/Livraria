import db_conexao
from datetime import datetime, timedelta
from psycopg2 import Error

def alugar_livro():
    print("\nLivros Disponíveis: ")

    try:

        conn = db_conexao.conectar()
        cursor = conn.cursor()

        sql_exibir_livros_disponiveis = """
            SELECT 
                a.id_livro,
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

        cursor.execute(sql_exibir_livros_disponiveis)
        
        if cursor.rowcount == 0:
            print("\nNão há livros disponíveis no momento.")
        else:
            livros_disponiveis = cursor.fetchall()
            for idx, livro in enumerate(livros_disponiveis, start=1):
                livro_id, titulo, disponiveis = livro
                print(f"| {idx:<2}. | Título: {titulo:<50} | Disponíveis: {disponiveis:>5} |")
            
            livro_escolhido_numero = int(input("\nDigite o número do livro que deseja alugar: "))
            
            if 1 <= livro_escolhido_numero <= len(livros_disponiveis):
                nome_livro_escolhido = livros_disponiveis[livro_escolhido_numero - 1][1]
                
                # Verifica se há cópias disponíveis para alugar
                if livros_disponiveis[livro_escolhido_numero - 1][2] > 0:
                    cursor.execute("SELECT id_usuario, nome FROM usuarios")
                    usuarios = cursor.fetchall()
                    print("\nInforme qual o cliente que quer alugar:")
                    print("\n| Matricula  |  Cliente:            |")
                    for usuario in usuarios:
                        user_id, user_nome = usuario
                        print(f"| {user_id:<10} | {user_nome:<20} |")
                    
                    usuario_escolhido_id = int(input("\nDigite a matricula do cliente que deseja alugar: "))
                    
                    if any(usuario_escolhido_id == user[0] for user in usuarios):
                        cursor.execute("SELECT id_livro FROM livros WHERE titulo = %s AND copias > (SELECT COUNT(*) FROM emprestimo WHERE id_livro = livros.id_livro AND status = 'alugado')", (nome_livro_escolhido,))
                        livro_disponivel = cursor.fetchone()

                        data_emprestimo = datetime.now().strftime('%Y-%m-%d')
                        data_devolucao = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
                        
                        cursor.execute("INSERT INTO emprestimo (id_livro, id_usuario, status, data_emprestimo, data_devolucao) VALUES (%s, %s, 'alugado', %s, %s)", (livro_disponivel[0], usuario_escolhido_id, data_emprestimo, data_devolucao))
                        conn.commit()
                        print("\nLivro alugado com sucesso!")
                        
                    else:
                        print("\nMatricula de usuário inválido.")
                else:
                    print("\nEstamos sem cópias disponíveis para alugar no momento.")
            else:
                print("\nNúmero do livro inválido.")

        from main import main
        main() 
        
    except (Exception, Error) as error:
        print("\nErro ao consultar os livros disponíveis:", error)