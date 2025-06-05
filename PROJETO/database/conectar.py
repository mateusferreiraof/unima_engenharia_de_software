import pymysql  # Biblioteca para conectar ao MySQL/MariaDB
import os       # Biblioteca para manipular variáveis e caminhos do sistema
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de um arquivo .env


class ConectarBanco:

    def __init__(self):       
        # Carrega as variáveis definidas no arquivo .env para o ambiente do sistema
        # Isso permite que você acesse os dados sensíveis (usuário, senha, host, porta) de forma segura
        load_dotenv()  

    def conectar(self):
        # Cria e retorna uma conexão com o banco de dados MySQL usando pymysql
        # As credenciais são obtidas das variáveis de ambiente carregadas pelo load_dotenv
        self.conexao = pymysql.connect (
            user = os.getenv('DB_USER'),           # Usuário do banco de dados
            password = os.getenv('DB_PASSWORD'),   # Senha do banco
            host = os.getenv('DB_HOST'),           # Endereço do servidor (ex: localhost)
            port = int(os.getenv('DB_PORT'))       # Porta de conexão (convertida para inteiro)
        )       
        return self.conexao  # Retorna o objeto conexão criado
