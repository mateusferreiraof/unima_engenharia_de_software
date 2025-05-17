from PROJETO import server
from PROJETO.database.conectar import ConectarBanco
from PROJETO.database.criartabelas import CriarTabelas
from PROJETO.database.criarbanco import CriarBanco
import os
from dotenv import load_dotenv
import pymysql


load_dotenv()  # carrega variáveis do .env

conexao = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
    port=int(os.getenv('DB_PORT', 3306))
)


bancodedados = ConectarBanco()
conexao = bancodedados.conectar()
cursor = conexao.cursor()
criarBanco = CriarBanco(conexao)
criarBanco.criar()
criarTabelas = CriarTabelas(conexao)
criarTabelas.criar()
conexao.close()

if __name__ == '__main__':
    server.run(debug=True)
    