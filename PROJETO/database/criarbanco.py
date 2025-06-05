import pymysql

class CriarBanco:

    def __init__(self, conexao):
        # Recebe a conexão ao banco de dados já criada
        self.conexao = conexao
        # Cria um cursor para executar comandos SQL
        self.cursor = self.conexao.cursor()
    
    def criar(self):
        # Executa um comando SQL para listar os bancos de dados existentes
        self.cursor.execute("""
            SHOW DATABASES
        """)
        # Busca todos os resultados da consulta, ou seja, a lista de bancos existentes
        bancos = self.cursor.fetchall()
        print(bancos)  # Exibe os bancos no console (para debug)

        # Verifica se o banco chamado "cadastro" não está na lista
        if ("cadastro",) not in bancos:
            # Se não existir, cria o banco de dados "cadastro" com charset UTF8
            self.cursor.execute("""
                CREATE DATABASE IF NOT EXISTS cadastro
                DEFAULT CHARACTER SET UTF8
                DEFAULT COLLATE UTF8_GENERAL_CI
            """)
