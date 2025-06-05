import pymysql

class CriarTabelas:

    def __init__(self, conexao):
        # Recebe a conexão ao banco de dados já criada
        self.conexao = conexao
        # Cria um cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()

    def criar(self):
        # Seleciona o banco de dados 'cadastro' para usar nas próximas queries
        self.cursor.execute("USE cadastro")
        
        # Cria a tabela 'usuarios' caso não exista, com os seguintes campos:
        # id_usuario: chave primária auto-incrementada
        # nome: nome do usuário, varchar 100, não nulo
        # email: único, varchar 100, não nulo
        # senha: varchar 100, não nulo
        # genero_usuario: varchar 10 (opcional)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(100) NOT NULL,
                genero_usuario VARCHAR(10)
            ) DEFAULT CHARSET = UTF8
        """)
        
        # Cria a tabela 'filmes' caso não exista, com:
        # id_filme: chave primária auto-incrementada
        # titulo_filme: título do filme, varchar 100, único
        # descricao_filme: descrição do filme, varchar 300
        # data_de_lancamento: data
        # genero_filme: varchar 50
        # ano_do_filme: ano (tipo YEAR)
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

        # Cria a tabela 'series' com estrutura similar à de filmes:
        # id_serie: chave primária auto-incrementada
        # titulo_serie: varchar 100, único
        # descricao_serie: varchar 300
        # data_de_lancamento: data
        # genero_serie: varchar 50
        # ano_da_serie: ano (YEAR)
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
