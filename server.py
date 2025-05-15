from flask import Flask, request, render_template
from database.conectar import conectarBanco


server = Flask(__name__)
bancodedados = conectarBanco()
conexao = bancodedados.conectar()
print(conexao.get_host_info())

@server.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    server.run(debug=True)