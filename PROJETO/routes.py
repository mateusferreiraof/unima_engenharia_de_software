from flask import render_template, redirect, request, session
from PROJETO import server
from PROJETO.config import conexao, cursor
from Api.tmdbapi import MovieAPI

@server.route('/')
def homepage():
    api = MovieAPI()
    dados = api.movie_list()
    return render_template("homepage.html", movies=dados['results'])

@server.route('/')
def inicio():
    return redirect('/login')

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
            return render_template("/index.html")
        
    return render_template("login.html")


@server.route('/recuperacao')
def recuperar_senha():
    return render_template("recuperacao_de_senha.html")

@server.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

@server.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrar_usuario():

    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        genero_usuario = request.form.get('genero')

        cursor.execute("INSERT INTO usuarios (nome, email, senha, genero_usuario) VALUES (%s, %s, %s, %s)", (nome, email, senha, genero_usuario))

        conexao.commit()
        
        return redirect('/login')
    return redirect('/cadastro')
