from flask import render_template, redirect, request, session
from PROJETO import server
from PROJETO.config import conexao, cursor
from Api.tmdbapi import MovieAPI

@server.route('/home')
def homepage():
    api = MovieAPI()
    dados = api.movie_list()
    return render_template("homepage.html", movies=dados['results'])

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
