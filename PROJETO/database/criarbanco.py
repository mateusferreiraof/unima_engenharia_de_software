import pymysql

class CriarBanco:

    def __init__(self, conexao):
        self.conexao = conexao
        self.cursor = self.conexao.cursor()
    
    def verificar(self):
        # Apenas mostra os bancos disponíveis (opcional)
        self.cursor.execute("SHOW DATABASES")
        bancos = self.cursor.fetchall()
        print("Bancos disponíveis:", bancos)
