from PROJETO import server
from PROJETO.database.conectar import conectarBanco
from PROJETO.database.criartabelas import CriarTabelas

bancodedados = conectarBanco()
conexao = bancodedados.conectar()
cursor = conexao.cursor()
criador = CriarTabelas(conexao)
criador.criar()
print(conexao.get_host_info())

if __name__ == '__main__':
    server.run(debug=True)
