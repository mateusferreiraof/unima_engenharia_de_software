from database.conectar import ConectarBanco

class InserirUsuario:

    def __init__(self, conexao):
        self.conexao = conexao()
        self.cursor = self.conexao.cursor()

    def inserirusuario(self):
        self.cursor.execute("""
            INSERT INTO usuarios(
            nome, email, senha, genero_usuario)
            values
            ('Mateus Ferreira, 'mateusunima@gmail. com', '123456', 'Masculino')
            """)