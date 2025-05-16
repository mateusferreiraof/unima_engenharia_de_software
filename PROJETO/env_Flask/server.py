from flask import Flask, request, render_template, redirect
from database.conectar import conectarBanco
from database.criartabelas import CriarTabelas


server = Flask(__name__)
bancodedados = conectarBanco()
conexao = bancodedados.conectar()
cursor = conexao.cursor()
criador = CriarTabelas(conexao)
criador.criar()
print(conexao.get_host_info())


@server.route('/')
def inicio():
    return redirect('/login')

@server.route('/login')
def login():
    return render_template("login.html")

@server.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

if __name__ == '__main__':
    server.run(debug=True)