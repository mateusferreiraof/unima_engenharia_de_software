from flask import render_template, redirect, request, session, url_for
from PROJETO import server
from PROJETO.config import conexao, cursor
from Api.tmdbapifilmes import MovieAPI
from Api.tmdbapiseries import SeriesAPI

@server.route('/home', methods=['GET', 'POST'])
def homepage():
    api = MovieAPI()
    filmes = api.movie_list()
    series = api.series_list()
    nome_do_usuario = session.get('nome')

    if request.method == 'POST':
        pesquisar = request.form.get('barra-de-busca')
        return redirect(url_for('index', pesquisa=pesquisar))

    return render_template("homepage.html", movies=filmes['results'], series=series['results'], nome=nome_do_usuario)


@server.route('/index')
def index():
    api = MovieAPI()
    nome_do_usuario = session.get('nome')
    pesquisa = request.args.get('pesquisa')

    if pesquisa:
        pesquisar = api.movie_search(query=pesquisa)
        return render_template("index.html", buscar=pesquisar['results'], mensagem=pesquisa, nome=nome_do_usuario)

    return redirect('/home') 

@server.route('/filmes')
def filmes():

    api = MovieAPI()
    filmes = api.movie_list()
    avaliados = api.filmes_bem_avaliados()
    tmdb = api.filmes_populares_tmdb()
    
    return render_template("filmes.html", filmes=filmes['results'], avaliados=avaliados['results'],tmdb=tmdb['results'])

@server.route('/series')
def series():
    api =SeriesAPI()
    populares = api.series_list()
    avaliadas = api.series_bem_avaliadas()
    tmdb =api.series_populares_tmdb()
    hj=api.series_exibidas_hj()

    return render_template("series.html",populares=populares['results'], avaliadas=avaliadas['results'], tmdb=tmdb['results'], hj=hj['results'])

@server.route('/')
def inicio():
    return redirect('/home')

@server.route('/login')
def login():

    verificar_login = session.get('usuario_id')
    
    if verificar_login == None:
        return render_template("login.html")
    
    return redirect("/home")

@server.route('/validacao-login', methods=['GET', 'POST'])
def validacao_login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))

        usuario = cursor.fetchone()

        if usuario:
            session['usuario_id'] = usuario[0]
            session['nome'] = usuario[1]
            return redirect('/home')
        
        mensagem = "E-mail ou senha inválidos. Tente novamente."
        return render_template("login.html", mensagem=mensagem)
        
    return render_template("login.html")

@server.route("/Sair")
def sair():
    session.pop('usuario_id', None)
    session.pop('nome')
    return redirect('/home')

@server.route('/recuperacao')
def recuperar_senha():
    return render_template("recuperacao_de_senha.html")

@server.route('/cadastro')
def cadastro():

    validar_login = session.get('usuario_id')

    if validar_login == None:
        return render_template("cadastro.html")
    return redirect('/home')

@server.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrar_usuario():

    mensagem = ""

    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha_confirmada = request.form.get('confirmar-senha')
        genero_usuario = request.form.get('genero')
        print(genero_usuario)

        dominios_aceitos = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com']
       
        if not any(email.endswith(dominio) for dominio in dominios_aceitos):
            mensagem = "E-mail inválido. Tente novamente."
            return render_template("cadastro.html", mensagem=mensagem)
        
        if senha != senha_confirmada:
            mensagem = "Senhas não coincidem. Tente novamente."
        else:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))

            resultado = cursor.fetchone()
            print(resultado)

            if resultado:
                mensagem = "O e-mail já está cadastrado em nosso banco de dados, tente outro."
            else:
                cursor.execute("INSERT INTO usuarios (nome, email, senha, genero_usuario) VALUES (%s, %s, %s, %s)", (nome, email, senha, genero_usuario))
                
                mensagem = "Usuário cadastrado com sucesso!"

        conexao.commit()

        return render_template("cadastro.html", mensagem=mensagem)
        
    return redirect('/cadastro')
