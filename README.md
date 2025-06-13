# LINK: unimaengenhariadesoftware-production.up.railway.app
# Este projeto está sendo desenvolvido como prática avaliativa da segunda unidade de **Engenharia de Software.**
## Nosso projeto consiste na produção de um site de recomendações de filmes e séries, consumindo APIs públicas.
## Base do projeto: Teremos inicialmente a homepage, a página de login e cadastro, e páginas direcionadas para as categorias de filmes e séries. 

## Responsável: Mateus Ferreira, Matheus Gabriel, Maria Layanne, Vinícius Matheus

# PopCorn Movies

PopCorn Movies é uma plataforma web para descoberta e exploração de filmes e séries, oferecendo uma experiência de navegação intuitiva para o usuário. O projeto inclui funcionalidades de autenticação de usuários, exibição de conteúdo multimídia com dados de APIs externas e uma estrutura de banco de dados para gerenciar informações de usuários e conteúdo.

## Visão Geral do Projeto

Este projeto é uma aplicação web que permite aos usuários:
* Registrar e fazer login em suas contas.
* Navegar por listas de filmes e séries populares e bem avaliadas.
* Visualizar detalhes básicos de filmes e séries, incluindo sinopse, gêneros e avaliações.
* Acessar páginas informativas como "Sobre Nós", "Contato", "Suporte", "Termos de Uso" e "Política de Privacidade".

A aplicação é construída com uma combinação de tecnologias web no frontend e Python para o backend e gerenciamento de banco de dados.

## Funcionalidades Principais

* **Autenticação de Usuário:**
    * Páginas de `Cadastro` e `Login` com validação de campos (nome, e-mail, senha).
    * Funcionalidade de `Recuperação de Senha` (indicada como em desenvolvimento).
* **Navegação de Conteúdo:**
    * `Homepage` com destaque e navegação principal para filmes e séries.
    * Páginas dedicadas para `Filmes` e `Séries`, exibindo conteúdo popular e mais avaliado, com paginação.
* **Exibição de Detalhes:** Exibição de pôster, título, sinopse, data de lançamento, gêneros e nota para filmes e séries (informações com origem provável de uma API externa como o TMDB, inferido pela estrutura dos dados no HTML).
* **Páginas Informativas:** Seções "Sobre Nós", "Contato", "Suporte", "Termos de Uso" e "Política de Privacidade" para informações adicionais e suporte ao usuário.
* **Estrutura de Banco de Dados:** Módulos Python para conectar ao banco de dados MySQL/MariaDB, criar o banco de dados (`cadastro`) e as tabelas necessárias (`usuarios`, `filmes`, `series`).

## Tecnologias Utilizadas

* **Frontend:**
    * **HTML:** Estrutura básica das páginas web.
    * **CSS:** Estilização e layout responsivo das páginas.
    * **Jinja2 (inferido):** Sintaxe de templating presente nos arquivos HTML (`{% if ... %}`, `{{ ... }}`).
    * **Font Awesome:** Biblioteca de ícones para a interface do usuário.
* **Backend:**
    * **Python:** Linguagem de programação principal para a lógica do servidor.
    * **Flask (inferido):** Framework web para lidar com as rotas HTTP e renderização de templates (baseado nas rotas como `/cadastrarusuario`, `/validacao-login`, `/home`, etc., e na estrutura geral).
    * **PyMySQL:** Biblioteca para conexão e interação com bancos de dados MySQL/MariaDB.
    * **python-dotenv:** Para carregar variáveis de ambiente de um arquivo `.env`, garantindo a segurança das credenciais do banco de dados.
* **Banco de Dados:**
    * **MySQL/MariaDB:** Sistema de gerenciamento de banco de dados relacional.

## Estrutura do Projeto (Arquivos Fornecidos)

A organização dos arquivos sugere uma estrutura típica de projetos web com Flask:

├── static/
│   ├── css/
│   │   ├── cadastro.css
│   │   ├── filmes_e_series.css
│   │   ├── footersite.css
│   │   ├── homepage.css
│   │   ├── index.css
│   │   └── login.css
│   └── imagens/ (inferido: para favicon, imagem de login etc.)
├── templates/ (inferido: onde os arquivos HTML estariam)
│   ├── cadastro.html
│   ├── contato.html
│   ├── filmes.html
│   ├── homepage.html
│   ├── index.html
│   ├── login.html
│   ├── privacidade.html
│   ├── recuperacao_de_senha.html
│   ├── series.html
│   ├── sobrenos.html
│   ├── suporte.html
│   └── termo.html
└── utils/ (inferido: módulos de utilidade, como os de banco de dados)
├── conectar.py
├── criarbanco.py
└── criartabelas.py

## Como Executar o Projeto (Instruções Gerais)

Para executar o projeto "PopCorn Movies", siga os passos abaixo. Note que algumas etapas são inferidas e dependem de um arquivo `app.py` ou similar que não foi fornecido.

**Pré-requisitos:**

* **Python 3.x:** Ambiente de execução Python.
* **pip:** Gerenciador de pacotes do Python.
* **Servidor MySQL/MariaDB:** Um servidor de banco de dados relacional (e.g., XAMPP, Docker, ou instalação local).

**Passos:**

1.  **Clone o Repositório (se aplicável):**
    ```bash
    git clone [https://github.com/mateusferreiraof/unima_engenharia_de_software.git](https://github.com/mateusferreiraof/unima_engenharia_de_software.git)
    cd unima_engenharia_de_software
    ```
2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Linux/macOS
    source venv/bin/activate
    # No Windows
    .\venv\Scripts\activate
    ```
3.  **Instale as Dependências Python:**
    ```bash
    pip install Flask pymysql python-dotenv
    ```
4.  **Configure as Variáveis de Ambiente:**
    * Crie um arquivo chamado `.env` na raiz do seu projeto.
    * Adicione as credenciais do seu banco de dados neste arquivo:
        ```env
        DB_USER='seu_usuario_mysql'
        DB_PASSWORD='sua_senha_mysql'
        DB_HOST='localhost'
        DB_PORT=3306
        ```
        Substitua `'seu_usuario_mysql'` e `'sua_senha_mysql'` pelas suas credenciais reais. `DB_HOST` pode ser `localhost` ou o IP/endereço do seu servidor de banco de dados.

5.  **Configure o Banco de Dados:**
    * Os scripts `criarbanco.py` e `criartabelas.py` são responsáveis por criar o banco de dados `cadastro` e suas tabelas (`usuarios`, `filmes`, `series`).
    * Você precisará executar esses scripts. Se você tem um arquivo `app.py` (ou similar) que gerencia a aplicação Flask, a chamada a esses scripts geralmente é feita uma vez na inicialização ou através de um comando específico. Um exemplo de execução direta (apenas para setup inicial):
        ```bash
        python -c "from utils.conectar import ConectarBanco; from utils.criarbanco import CriarBanco; from utils.criartabelas import CriarTabelas; conn = ConectarBanco().conectar(); CriarBanco(conn).criar(); CriarTabelas(conn).criar(); conn.close()"
        ```
        **Importante:** Este comando deve ser executado apenas uma vez para configurar o banco de dados e as tabelas.

6.  **Execute a Aplicação Flask:**
    * Presume-se a existência de um arquivo principal da aplicação Flask (ex: `app.py`) que define as rotas e inicializa o servidor. Se você não o tem, precisará criá-lo.
    * Exemplo básico de como `app.py` poderia ser (isso é uma suposição, o arquivo real deve ter a lógica completa):
        ```python
        # Exemplo de app.py (NÃO FORNECIDO, DEVE SER CRIADO POR VOCÊ)
        from flask import Flask, render_template, request, redirect, url_for, session, jsonify
        from utils.conectar import ConectarBanco
        import pymysql

        app = Flask(__name__, template_folder='templates', static_folder='static')
        app.secret_key = 'sua_chave_secreta_aqui' # Importante para sessões Flask

        # Exemplo de rota, você teria várias dessas
        @app.route('/')
        @app.route('/home')
        def home():
            nome_usuario = session.get('nome') # Pega o nome da sessão, se houver
            return render_template('homepage.html', nome=nome_usuario)

        @app.route('/cadastro')
        def cadastro_page():
            return render_template('cadastro.html')

        @app.route('/cadastrarusuario', methods=['POST'])
        def cadastrar_usuario():
            # Lógica de cadastro (conectar BD, inserir usuário, etc.)
            try:
                conexao = ConectarBanco().conectar()
                cursor = conexao.cursor()
                # Exemplo: Lógica para inserir no banco de dados
                nome = request.form['nome']
                email = request.form['email']
                senha = request.form['senha']
                genero = request.form.get('genero') # Pode ser None

                cursor.execute("USE cadastro")
                sql = "INSERT INTO usuarios (nome, email, senha, genero_usuario) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nome, email, senha, genero))
                conexao.commit()
                return render_template('cadastro.html', mensagem='Usuário cadastrado com sucesso!')
            except pymysql.err.IntegrityError:
                return render_template('cadastro.html', mensagem='Erro: E-mail já cadastrado.')
            except Exception as e:
                return render_template('cadastro.html', mensagem=f'Erro ao cadastrar: {e}')
            finally:
                if 'conexao' in locals() and conexao.open:
                    conexao.close()


        # ... adicione outras rotas como /login, /validacao-login, /filmes, /series, /contato, /suporte etc.

        if __name__ == '__main__':
            app.run(debug=True) # debug=True para desenvolvimento
        ```
    * Com seu `app.py` configurado, execute-o:
        ```bash
        python app.py
        ```
7.  **Acesse a Aplicação:**
    * Abra seu navegador web e navegue para `http://127.0.0.1:5000` (ou a porta que seu Flask app estiver configurado para usar).
