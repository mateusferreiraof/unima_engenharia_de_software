# Importa a classe Flask da biblioteca flask
from flask import Flask

# Cria uma instância da aplicação Flask, chamada 'server'
# Essa instância será responsável por rodar o servidor web
server = Flask(__name__)

# Define uma chave secreta para a aplicação
# Essa chave é usada pelo Flask para proteção
server.secret_key = '12345678'

# Importa as rotas da aplicação a partir da pasta 'PROJETO'
# Isso deve conter os arquivos com os endpoints (rotas) da aplicação Flask
from PROJETO import routes
