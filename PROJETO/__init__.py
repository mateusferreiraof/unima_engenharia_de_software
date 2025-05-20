from flask import Flask

server = Flask(__name__)
server.secret_key = '12345678'
from PROJETO import routes
