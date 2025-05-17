import pymysql

class CriarBanco:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()
    
    def criar(self):
        self.cursor.execute("""
            SHOW DATABASES
        """)
        bancos = self.cursor.fetchall()
        print(bancos)
        if ("cadastro",) not in bancos:
            self.cursor.execute("""
                CREATE DATABASE cadastro
            """)