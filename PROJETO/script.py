# Importa a classe responsável pela conexão com o banco de dados
from PROJETO.database.conectar import ConectarBanco

# Importa a classe que apenas verifica os bancos disponíveis
from PROJETO.database.criarbanco import CriarBanco  # agora só verifica

# Importa a classe que cria as tabelas dentro do banco de dados
from PROJETO.database.criartabelas import CriarTabelas


# Instancia a classe que controla a conexão com o banco
bancodedados = ConectarBanco()

# Abre a conexão com o banco (retorna o objeto conexão)
conexao = bancodedados.conectar()

# Cria o cursor que será usado para executar comandos SQL
cursor = conexao.cursor()

# Instancia o verificador do banco (sem criar)
criarBanco = CriarBanco(conexao)
criarBanco.verificar()  # Apenas mostra os bancos existentes (debug opcional)

# Instancia o criador das tabelas, passando a conexão
criarTabelas = CriarTabelas(conexao)

# Executa a criação das tabelas, se não existirem
criarTabelas.criar()
