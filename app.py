# Importa a instância do Flask chamada 'server' do pacote PROJETO
from PROJETO import server

# Importa o módulo 'script' que provavelmente contém as rotas e lógica da aplicação
from PROJETO import script  

# Verifica se este arquivo está sendo executado diretamente (não importado)
if __name__ == '__main__':
    # Inicia o servidor Flask no modo debug para facilitar o desenvolvimento
    server.run(debug=True)
