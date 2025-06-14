# Importa funções e objetos necessários do Flask
from flask import render_template, redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash


# Importa a instância do Flask chamada "server" do pacote PROJETO
from PROJETO import server

# Importa o objeto de conexão com o banco de dados e o cursor para executar comandos SQL
from PROJETO.script import conexao, cursor

# Importa a API de filmes personalizada
from Api.tmdbapifilmes import MovieAPI

# Importa a API de séries personalizada
from Api.tmdbapiseries import SeriesAPI
from Api.categorias import Categoria

# Rota da homepage
@server.route('/home', methods=['GET', 'POST'])
def homepage():
    api = MovieAPI()
    filmes = api.movie_list()         # Pega lista de filmes
    api_series =SeriesAPI()
    api_categorias = Categoria()
    

    series =api_series.series_populares_tmdb()        # Pega lista de séries
    nome_do_usuario = session.get('nome')  # Pega o nome do usuário da sessão (se estiver logado)

    # Se o usuário pesquisar algo, redireciona para a rota /index com o termo
    if request.method == 'POST':
        pesquisar = request.form.get('barra-de-busca')
        pesquisa = api.movie_search(query=pesquisar)
        return redirect(url_for('index', pesquisa=pesquisar))
    
    categorias = api_categorias.obter_generos()
    generos_dict = {g['id']: g['name'] for g in categorias['genres']}

    def adicionar_nomes_generos(lista, generos_dict):
        for item in lista.get('results', []):
            if 'genre_ids' in item:
                item['genres_nomes'] = [generos_dict.get(gid, "Desconhecido") for gid in item['genre_ids']]

    # Aplica a função para filmes e séries
    adicionar_nomes_generos(filmes, generos_dict)
    adicionar_nomes_generos(series, generos_dict)

    return render_template( "homepage.html", movies=filmes['results'], categorias=categorias['genres'],series=series['results'], nome=nome_do_usuario)

@server.route('/index')
def index():
    api = MovieAPI()
    nome_do_usuario = session.get('nome')
    pesquisa = request.args.get('pesquisa')
    pagina = request.args.get('page', default=1, type=int) 

    if pesquisa:
        pesquisar = api.movie_search(query=pesquisa, page=pagina)  
        tem_proxima = len(pesquisar['results']) == 20  

        return render_template("index.html",buscar=pesquisar['results'],mensagem=pesquisa,nome=nome_do_usuario,pagina=pagina,tem_proxima=tem_proxima)
    return redirect('/home') 

@server.route('/filmes')
def filmes():
    api = MovieAPI()
    api_categorias = Categoria()
    nome_do_usuario = session.get('nome')

    pagina = request.args.get('page', default=1, type=int)
    filmes = api.movie_list(page=pagina)
    avaliados = api.filmes_bem_avaliados(page=pagina)
    tmdb = api.filmes_populares_tmdb(page=pagina)
    cartaz = api.filmes_em_cartaz(page=pagina)


# Obtemos a lista de categorias
    categorias = api_categorias.obter_generos()
    generos_dict = {g['id']: g['name'] for g in categorias['genres']}
    
    def adicionar_nomes_generos(lista_filmes, generos_dict):
        for filme in lista_filmes.get('results', []):
            if 'genre_ids' in filme:
                filme['genres_nomes'] = [generos_dict.get(gid, "Desconhecido") for gid in filme['genre_ids']]

    # Aplica para todas as listas
    adicionar_nomes_generos(filmes, generos_dict)
    adicionar_nomes_generos(avaliados, generos_dict)
    adicionar_nomes_generos(tmdb, generos_dict)
    adicionar_nomes_generos(cartaz, generos_dict)


    return render_template("filmes.html", filmes=filmes['results'],categorias=categorias['genres'], avaliados=avaliados['results'], tmdb=tmdb['results'], cartaz=cartaz['results'],pagina=pagina, nome=nome_do_usuario)

#rota para direcionar informações do filme
@server.route('/filme/<int:filme_id>')
def detalhes_filme(filme_id):
    api = MovieAPI()
    api_categorias = Categoria()
    provedores = api.onde_assistir(filme_id)
    elenco = api.get_elenco_filme(filme_id)
    nome_do_usuario = session.get('nome')
    
    
    dados = api.get_detalhes_filme(filme_id)
    # Obtemos a lista de categorias
    categorias = api_categorias.obter_generos()
    # Extrai os nomes dos gêneros diretamente do detalhe do filme
    dados['genres_nomes'] = [g['name'] for g in dados.get('genres', [])]

    return render_template('detalhes_filme.html',categorias=categorias['genres'], filme=dados, provedores=provedores,elenco=elenco, nome=nome_do_usuario)


# Página de séries
@server.route('/series')
def series():
    api = SeriesAPI()
    api_categorias = Categoria()
    nome_do_usuario = session.get('nome')

    pagina = request.args.get('page', default=1, type=int)
    populares = api.series_list(page=pagina)
    avaliadas = api.series_bem_avaliadas(page=pagina)
    tmdb = api.series_populares_tmdb(page=pagina)
    hj = api.series_exibidas_hj(page=pagina)

    categorias = api_categorias.obter_generos_tv()
    generos_dict = {g['id']: g['name'] for g in categorias['genres']}

    def adicionar_nomes_generos(lista_series, generos_dict):
        for serie in lista_series.get('results', []):
            if 'genre_ids' in serie:
                serie['genres_nomes'] = [generos_dict.get(gid, "Desconhecido") for gid in serie['genre_ids']]

    # Aplica para todas as listas
    adicionar_nomes_generos(populares, generos_dict)
    adicionar_nomes_generos(avaliadas, generos_dict)
    adicionar_nomes_generos(tmdb, generos_dict)

    return render_template("series.html", populares=populares['results'], avaliadas=avaliadas['results'], tmdb=tmdb['results'], hj=hj['results'], categorias=categorias['genres'], pagina=pagina, nome=nome_do_usuario)


#rota para direcionar informações do filme
@server.route('/serie/<int:serie_id>')
def detalhes_serie(serie_id):
    api = SeriesAPI()
    api_categorias = Categoria()
    provedores = api.onde_assistir_serie(serie_id)
    elenco = api.get_elenco_serie(serie_id)
    nome_do_usuario = session.get('nome')

    dados = api.get_detalhes_serie(serie_id)
    # Obtemos a lista de categorias
    categorias = api_categorias.obter_generos()
    # Extrai os nomes dos gêneros diretamente do detalhe da serie
    dados['genres_nomes'] = [g['name'] for g in dados.get('genres', [])]

    return render_template('detalhes_serie.html',categorias=categorias['genres'], serie=dados, provedores=provedores, elenco=elenco, nome=nome_do_usuario)


# Redireciona a raiz do site para a home
@server.route('/')
def inicio():
    return redirect('/home')

# Página de login
@server.route('/login')
def login():
    verificar_login = session.get('usuario_id')

    # Se não estiver logado, mostra a página de login
    if verificar_login is None:
        return render_template("login.html")
    
    return redirect("/home")  # Se já estiver logado, redireciona para home

# Validação do login
@server.route('/validacao-login', methods=['GET', 'POST'])
def validacao_login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Busca usuário pelo e-mail
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario:
            senha_hash = usuario[3]  # Coluna da senha no banco

            # Verifica se a senha está correta
            if check_password_hash(senha_hash, senha):
                session['usuario_id'] = usuario[0]
                session['nome'] = usuario[1]
                return redirect('/home')

        mensagem = "E-mail ou senha inválidos. Tente novamente."
        return render_template("login.html", mensagem=mensagem)

    return render_template("login.html")


# Rota para logout
@server.route("/Sair")
def sair():
    session.pop('usuario_id', None)  # Remove o ID da sessão
    session.pop('nome')              # Remove o nome da sessão
    return redirect('/home')

# Página de recuperação de senha
@server.route('/recuperacao')
def recuperar_senha():
    return render_template("recuperacao_de_senha.html")

# Página de cadastro
@server.route('/cadastro')
def cadastro():
    validar_login = session.get('usuario_id')

    if validar_login is None:
        return render_template("cadastro.html")
    
    return redirect('/home')

# Lógica de cadastro de novo usuário
@server.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    mensagem = ""

    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha_confirmada = request.form.get('confirmar-senha')
        genero_usuario = request.form.get('genero')

        dominios_aceitos = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com']

        # Valida o domínio do e-mail
        if not any(email.endswith(dominio) for dominio in dominios_aceitos):
            mensagem = "E-mail inválido. Tente novamente."
            return render_template("cadastro.html", mensagem=mensagem)

        # Verifica se as senhas coincidem
        if senha != senha_confirmada:
            mensagem = "Senhas não coincidem. Tente novamente."
            return render_template("cadastro.html", mensagem=mensagem)
        else:
            # Verifica se o e-mail já existe
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            resultado = cursor.fetchone()

            if resultado:
                mensagem = "O e-mail já está cadastrado em nosso banco de dados, tente outro."
            else:
                # Gera hash seguro da senha
                senha_hash = generate_password_hash(senha)

                # Cadastra o novo usuário com senha criptografada
                cursor.execute("INSERT INTO usuarios (nome, email, senha, genero_usuario) VALUES (%s, %s, %s, %s)", (nome, email, senha_hash, genero_usuario))

                mensagem = "Usuário cadastrado com sucesso!"

        # Confirma as alterações no banco
        conexao.commit()

        return render_template("cadastro.html", mensagem=mensagem)
    
    # Se não for POST, redireciona para a página de cadastro
    return redirect('/cadastro')

@server.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    email = request.form.get('email')
    mensagem = ""
    if request.method == 'POST':
        mensagem = "Se este email estiver cadastrado, você receberá um e-mail para redefinição de sua senha."
    return render_template("recuperacao_de_senha.html", mensagem=mensagem)


@server.route('/sobrenos')
def sobrenos():
    nome_do_usuario = session.get('nome')
    return render_template('sobrenos.html', nome=nome_do_usuario)

@server.route('/contato')
def contato():
    nome_do_usuario = session.get('nome')
    return render_template('contato.html', nome=nome_do_usuario)

@server.route('/termo')
def termo():
    nome_do_usuario = session.get('nome')
    return render_template('termo.html', nome=nome_do_usuario)

@server.route('/privacidade')
def privacidade():
    nome_do_usuario = session.get('nome')
    return render_template('privacidade.html', nome=nome_do_usuario)

@server.route('/suporte')
def suporte():
    nome_do_usuario = session.get('nome')
    return render_template('suporte.html', nome=nome_do_usuario)