import pymysql
import os
from dotenv import load_dotenv


class ConectarBanco:

    def __init__(self):       
        load_dotenv()  

    def conectar(self):
        self.conexao = pymysql.connect (
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            host = os.getenv('DB_HOST'),
            port = int(os.getenv('DB_PORT'))
)       
        return self.conexao


