import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env localmente

class ConectarBanco:

    def conectar(self):
        host = os.getenv("MYSQLHOST")
        user = os.getenv("MYSQLUSER")
        password = os.getenv("MYSQLPASSWORD")
        database = os.getenv("MYSQLDATABASE")
        port = int(os.getenv("MYSQLPORT", "3306"))
        print(f"Conectando em {host}:{port} com user {user} e db {database}")
        return pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
    )
