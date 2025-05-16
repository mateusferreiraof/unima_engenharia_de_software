import pymysql


class CriarTabelas:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def criar(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes(
                id_filme INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(100),
                genero VARCHAR(50),
                ano INT
            )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(30),
                email VARCHAR(60),
                senha VARCHAR(30),
                genero VARCHAR(10)
        )""")

        
