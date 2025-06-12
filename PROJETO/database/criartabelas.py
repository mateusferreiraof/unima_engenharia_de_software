import pymysql
import os

class CriarTabelas:
    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def criar(self):
        nome_banco = os.getenv("MYSQLDATABASE")  # Banco criado automaticamente pelo Railway
        self.cursor.execute(f"USE {nome_banco}")

        self.cursor.execute("ALTER TABLE usuarios MODIFY senha VARCHAR(255);")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL,
                genero_usuario VARCHAR(10)
            ) DEFAULT CHARSET = utf8mb4
        """)
