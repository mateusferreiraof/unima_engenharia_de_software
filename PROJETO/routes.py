from flask import render_template, redirect
from PROJETO import server

@server.route('/')
def inicio():
    return redirect('/login')

@server.route('/login')
def login():
    return render_template("login.html")

@server.route('/recuperacao')
def recuperar_senha():
    return render_template("recuperacao_de_senha.html")

@server.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")
