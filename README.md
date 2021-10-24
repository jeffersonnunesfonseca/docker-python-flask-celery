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
Ambiente docker com python utilizando o framework flask
<h2>
    <b>Modo de usar</b>    
</h2> 

- crie um novo arquivo .env com base no .env.example
- para gerar uma imagem executar `docker build -t "it:<version>" .`
    -  subir a imagem `docker run -d --name it-app -p 8000:8000  --env-file .env it:v1`
- rodar local, necessário ter o conda:
    - `conda create --name docker-python-flask python=3.6`
    - `conda activate docker-python-flask`
    - matar processos: ` kill -9 $(ps -ef | grep gunicorn | awk '{print $2}')`
- subir rabbit
    -  `docker-compose up -d` 
- rodar consumer  `celery -A tasks  worker --loglevel=info`
    
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
<div>


conda create --name docker-python-flask python=3.6
