import sqlite3
from contextlib import contextmanager

#Nome do ficheiro de base de dados
DATABASE = 'livros.db'

@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Permite trabalhar com dicionários
    try:
        yield conn
    finally:
        conn.close()
   


# Criação da tabela de livros, se não existir
def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn VARCHAR(150),
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL
            )
        ''')
        conn.commit()
        print("Base de dados inicializada.")
