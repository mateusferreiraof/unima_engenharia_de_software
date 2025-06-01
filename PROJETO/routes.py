from flask import render_template, redirect, request, session
from PROJETO import server
from PROJETO.config import conexao, cursor
from Api.tmdbapifilmes import MovieAPI
from Api.tmdbapiseries import SeriesAPI

@server.route('/home', methods=['GET', 'POST'])
def homepage():

    api = MovieAPI()
    filmes = api.movie_list()
    series = api.series_list()

    if request.method == 'POST':
        pesquisar = request.form.get('barra-de-busca')
        pesquisa = api.movie_search(query=pesquisar)
        return render_template("index.html", buscar=pesquisa['results'], mensagem=pesquisar)
        
    return render_template("homepage.html", movies=filmes['results'], series=series['results'])

@server.route('/filmes')
def filmes():

    api = MovieAPI()
    pagina = request.args.get('page', default=1, type=int)
    filmes = api.movie_list(page=pagina)
    avaliados = api.filmes_bem_avaliados(page=pagina)
    tmdb = api.filmes_populares_tmdb(page=pagina)
    
    return render_template("filmes.html", filmes=filmes['results'], avaliados=avaliados['results'],tmdb=tmdb['results'], pagina=pagina)

@server.route('/series')
def series():
    api =SeriesAPI()
    pagina = request.args.get('page', default=1, type=int)
    populares = api.series_list(page=pagina)
    avaliadas = api.series_bem_avaliadas(page=pagina)
    tmdb =api.series_populares_tmdb(page=pagina)
    hj=api.series_exibidas_hj(page=pagina)

    return render_template("series.html",populares=populares['results'], avaliadas=avaliadas['results'], tmdb=tmdb['results'], hj=hj['results'], pagina=pagina)

@server.route('/')
def inicio():
    return redirect('/home')

@server.route('/login')
def login():
    return render_template("login.html")

@server.route('/validacao-login', methods=['GET', 'POST'])
def validacao_login():
    if request.method == "POST":
        email = request.form.get('email')
        senha = request.form.get('senha')

        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))

        usuario = cursor.fetchone()

        if usuario:
            session['usuario_id'] = usuario[0]
            return redirect('/home')
        
        mensagem = "E-mail ou senha inválidos. Tente novamente."
        return render_template("login.html", mensagem=mensagem)
        
    return render_template("login.html")

@server.route('/recuperacao')
def recuperar_senha():
    return render_template("recuperacao_de_senha.html")

@server.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

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
