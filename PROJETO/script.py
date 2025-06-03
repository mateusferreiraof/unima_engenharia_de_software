from PROJETO.database.conectar import ConectarBanco
from PROJETO.database.criarbanco import CriarBanco
from PROJETO.database.criartabelas import CriarTabelas

bancodedados = ConectarBanco()
conexao = bancodedados.conectar()

cursor = conexao.cursor()

criarBanco = CriarBanco(conexao)
criarBanco.criar()

criarTabelas = CriarTabelas(conexao)
criarTabelas.criar()