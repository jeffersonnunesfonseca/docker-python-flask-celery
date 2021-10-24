<div>

[![Generic badge](https://img.shields.io/badge/flask-2.0.2-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/python-3.06-<COLOR>.svg)](https://shields.io/)

</div>
<h1 align="center">
  <img alt="mysqlDocker" title="" src="./static/image.png"/>
</h1>
<h2>
    <b>Objetivo</b>
</h2> 
<div>

- Disponibilizar um conteúdo onde contém uma api em python com o framework Flask, tendo como principais tecnologias:
    - docker, 
    - conda, 
    - rabbitMQ sendo orquestrado pela poderosa lib <a href="https://docs.celeryproject.org/en/stable/">Celery</a>.
</div>
<h2>
    <b>Modo de usar</b>    
</h2> 
<div>

- crie um novo arquivo .env com base no .env.example
- rodar local, necessário ter o <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html">conda</a>:
    - Criar virtual env(será executado apenas 1x): `conda create --name docker-python-flask python=3.6`
    - Ativar venv: `conda activate docker-python-flask`
    - matar processos: ` kill -9 $(ps -ef | grep gunicorn | awk '{print $2}')`
- subir um banco de dados Mysql, pode utilizar esse projeto <a href="https://github.com/jeffersonnunesfonseca/mysql"> Mysql </a>
- subir as tabelas com a migration `python migrationSqlAlchemy.py`, se estiver utilizando o projeto de mysql sugerido só sera necessario executar 1x
- subir rabbit
    -  `docker-compose up -d` 
- rodar o consumer, necessário estar no ambiente  `celery -A tasks  worker --loglevel=info`
- subir a api direto com o python ou <a href="https://gunicorn.org/#docs">gunicorn</a>
    -   python: `python run.py`
    -   gunicorn: `gunicorn --config=gunicorn.py run:app`
- para gerar uma imagem executar `docker build -t "it:<version>" .`
    -  subir a imagem `docker run -d --name it-app -p 8000:8000  --env-file .env it:v1`
</div>
<h2>
    <b>Acesso</b>    
</h2> 

`http://localhost:<PORT_HOST>`

<h2>
    Testes
</h2>

- para realizar os testes estou utilizando a lib <a href="https://docs.python.org/3/library/unittest.html">unittest</a>

- para rodar a suite de testes basta executar `python tests` na raiz do projeto e ele executara todos os testes que estiverem em `/apiTests/__init__.py` 

<h2>
    APIs
</h2>

### Autenticação

<div>

#### <a href="https://pyjwt.readthedocs.io/en/stable/"> JWT - PYJWT</a>
- Gerar TOKEN
    
    ```
    - GET /generateToken/
    - payload any json
    {
	    "name":"Jeff",
	    "age":26
    }

    ``` 
- Decode TOKEN
    ```
    - POST /decodeToken/
        - payload token in json
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYnJhYm8iLCJhZ2UiOjI1fQ.DQu6nPdEmJhxrCAIFX8qzMajBzP40i--_BkLPpJpFPA"
        }

    ```
- Create User
    ```
    - POST /createUser/
        - payload JSON
        {
            "nome": "Jeff Teste",
            "email": "teste@teste.com",
            "telefone": "(41) 99999-9985",
            "telefone2": "(41) 99999-9985",
            "nome_empresa": "teste",
            "cpf_cnpj": "94.187.140/0001-64",
            "data_nascimento": "1995-06-12",
            "sexo": "M",
            "senha": "12345",
            "login": "jeffTeste"
        }

    ```


<div>
