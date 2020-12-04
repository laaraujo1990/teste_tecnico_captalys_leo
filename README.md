Projeto Teste Tecnico Captalys - Leonardo Araujo - 03/12/2020

- Repositorio do codigo:
https://github.com/laaraujo1990/teste_tecnico_captalys_leo

- Repositorio do container Docker:
https://hub.docker.com/repository/docker/laaraujo1990/teste_tecnico_captalys
https://hub.docker.com/r/laaraujo1990/teste_tecnico_captalys

- Ambiente de hardware:
MacBook Air (13-inch, Early 2015)

- Ambiente de software:
macOS Catalina v10.15.7
Python v3.8.2
Flask v1.1.2

- Ambiente de desenvolvimento e teste
Visual Studio Code v1.51.1
Google Chrome
web.postman.co

- Ambiente virtual
Docker v2.5.0.1

- Arquivos
# descricao_teste.pdf : Enunciado do desafio tecnico
# ex01_hello_word_flask.py : Usado para entender o Flask funcionando
# ex02_exemplo_crud_flask.py : Usado para entender o funcionamento do CRUD basico com Flask
# ex03_repositorios_por_usuario_github.py : Usado para listar repositorios da API do GitHub
# teste_tecnico_captalys.py : Arquivo principal do desafio tecnico
# Dockerfile : Usado para subir o programa num container Docker

- Configuracao de ambiente:
# Criar ambiente virtual
>python3 -m venv ambiente_virtual_desafio
# Ativar ambiente virtual
>source ambiente_virtual_desafio/bin/activate
# Atualizar o pip
>pip install --upgrade pip
# Instalar Flask
>pip install flask
# Instalar a biblioteca requests
>pip install requests
# Desativar ambiente virtual
>deactivate

- Execucao do programa no ambiente local
>python3 teste_tecnico_captalys.py
# Resultado: acesse a url http://localhost:5000
- Primeiro Endpoint
# Resultado: acesse a url http://localhost:5000/repositories/<nome do usuario>
- Segundo Endpoint
# Resultado: acesse a url http://localhost:5000/repositories/<nome do usuario>/<nome do repositorio>

- Configuracao no Docker
# Gerando o Container
>docker image build -t teste_tecnico_captalys .
# Executando o Container
>docker run -p 5001:5000 -d teste_tecnico_captalys
# Logando no Docker Hub
>docker login
# Fazendo a tag do container
>docker tag teste_tecnico_captalys [dockerhub username]/teste_tecnico_captalys
# Enviando a imagem para o docker hub
>docker push [dockerhub username]/teste_tecnico_captalys
# Resultado: acesse a url http://localhost:5001
- Primeiro Endpoint
# Resultado: acesse a url http://localhost:5001/repositories/<nome do usuario>
- Segundo Endpoint
# Resultado: acesse a url http://localhost:5001/repositories/<nome do usuario>/<nome do repositorio>

