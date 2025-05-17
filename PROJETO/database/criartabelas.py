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
                email VARCHAR(100) NOT NULL,
                senha VARCHAR(100) NOT NULL,
                genero VARCHAR(10)
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS filmes (
                id_filme INT AUTO_INCREMENT PRIMARY KEY,
                titulo_filme VARCHAR(100),
                descricao_filme VARCHAR(300),
                data_de_lancamento DATE,
                genero_filme VARCHAR(50),
                ano YEAR
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS series (
                id_serie INT AUTO_INCREMENT PRIMARY KEY,
                titulo_serie VARCHAR(100),
                genero_serie VARCHAR(50),
                ano INT
            )
        """)


        
