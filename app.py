from PROJETO import server
from PROJETO.database.conectar import ConectarBanco
from PROJETO.database.criartabelas import CriarTabelas
from PROJETO.database.criarbanco import CriarBanco

bancodedados = ConectarBanco()
conexao = bancodedados.conectar()
cursor = conexao.cursor()
criarBanco = CriarBanco(conexao)
criarBanco.criar()
criarTabelas = CriarTabelas(conexao)
criarTabelas.criar()
conexao.close()

if __name__ == '__main__':
    server.run(debug=True)''
    