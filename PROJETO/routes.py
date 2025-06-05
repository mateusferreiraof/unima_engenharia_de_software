# Importa funções e objetos necessários do Flask
from flask import render_template, redirect, request, session, url_for

# Importa a instância do Flask chamada "server" do pacote PROJETO
from PROJETO import server

# Importa o objeto de conexão com o banco de dados e o cursor para executar comandos SQL
from PROJETO.script import conexao, cursor

# Importa a API de filmes personalizada
from Api.tmdbapifilmes import MovieAPI

# Importa a API de séries personalizada
from Api.tmdbapiseries import SeriesAPI

# Rota da homepage
@server.route('/home', methods=['GET', 'POST'])
def homepage():
    api = MovieAPI()
    filmes = api.movie_list()         # Pega lista de filmes
    series = api.series_list()        # Pega lista de séries
    nome_do_usuario = session.get('nome')  # Pega o nome do usuário da sessão (se estiver logado)

    # Se o usuário pesquisar algo, redireciona para a rota /index com o termo
    if request.method == 'POST':
        pesquisar = request.form.get('barra-de-busca')
        return redirect(url_for('index', pesquisa=pesquisar))

    # Renderiza a homepage com os filmes e séries
    return render_template("homepage.html", movies=filmes['results'], series=series['results'], nome=nome_do_usuario)

# Rota de pesquisa
@server.route('/index')
def index():
    api = MovieAPI()
    nome_do_usuario = session.get('nome')
    pesquisa = request.args.get('pesquisa')  # Pega o termo da URL

    if pesquisa:
        pesquisar = api.movie_search(query=pesquisa)  # Faz a busca de filmes com o termo
        return render_template("index.html", buscar=pesquisar['results'], mensagem=pesquisa, nome=nome_do_usuario)

    return redirect('/home')  # Se não houver termo, volta para home

# Página de filmes
@server.route('/filmes')
def filmes():
    api = MovieAPI()
    filmes = api.movie_list()
    avaliados = api.filmes_bem_avaliados()
    tmdb = api.filmes_populares_tmdb()

    return render_template("filmes.html", filmes=filmes['results'], avaliados=avaliados['results'], tmdb=tmdb['results'])

# Página de séries
@server.route('/series')
def series():
    api = SeriesAPI()
    populares = api.series_list()
    avaliadas = api.series_bem_avaliadas()
    tmdb = api.series_populares_tmdb()
    hj = api.series_exibidas_hj()

    return render_template("series.html", populares=populares['results'], avaliadas=avaliadas['results'], tmdb=tmdb['results'], hj=hj['results'])

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

        # Verifica se existe um usuário com o e-mail e senha fornecidos
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario = cursor.fetchone()

        if usuario:
            # Se válido, salva na sessão o ID e o nome do usuário
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
        else:
            # Verifica se o e-mail já existe
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            resultado = cursor.fetchone()

            if resultado:
                mensagem = "O e-mail já está cadastrado em nosso banco de dados, tente outro."
            else:
                # Cadastra o novo usuário
                cursor.execute("INSERT INTO usuarios (nome, email, senha, genero_usuario) VALUES (%s, %s, %s, %s)", (nome, email, senha, genero_usuario))
                mensagem = "Usuário cadastrado com sucesso!"

        # Confirma as alterações no banco
        conexao.commit()

        return render_template("cadastro.html", mensagem=mensagem)
    
    # Se não for POST, redireciona para a página de cadastro
    return redirect('/cadastro')
