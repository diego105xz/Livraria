import psycopg2
from psycopg2 import Error

def conectar():
    try:
        db_config = {
            'host': 'localhost',
            'database': 'postgres',
            'user': 'postgres',
            'password': 'senha747',
        }
        conn = psycopg2.connect(**db_config)

        return conn

    except (Exception, Error) as error:
        print("Erro ao conectar ao banco de dados:", error)