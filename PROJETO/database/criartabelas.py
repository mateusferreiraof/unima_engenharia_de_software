import pymysql

class CriarTabelas:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()

    def criar(self):

        self.cursor.execute("USE cadastro")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(100) NOT NULL,
                genero_usuario VARCHAR(10)
            ) DEFAULT CHARSET = UTF8
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id_filme INT AUTO_INCREMENT PRIMARY KEY,
                titulo_filme VARCHAR(100) UNIQUE,
                descricao_filme VARCHAR(300),
                data_de_lancamento DATE,
                genero_filme VARCHAR(50),
                ano_do_filme YEAR
            ) DEFAULT CHARSET = UTF8
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS series (
                id_serie INT AUTO_INCREMENT PRIMARY KEY,
                titulo_serie VARCHAR(100) UNIQUE,
                descricao_serie VARCHAR(300),
                data_de_lancamento DATE,
                genero_serie VARCHAR(50),
                ano_da_serie YEAR
            ) DEFAULT CHARSET = UTF8
        """)


        
