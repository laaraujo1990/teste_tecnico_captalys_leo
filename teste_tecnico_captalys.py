#!//usr/local/bin/python3
#
# Desafio tecnico Captalys
# Listagem de dados da API do GitHub
#
# Leonardo Araujo

from flask import Flask, jsonify, request, json
import requests
import json

app = Flask(__name__)

# Classe do primeiro Endpoint para listar repositorios por usuario
class ListaRepositorios():

    def __init__(self, usuario):
        self._usuario = usuario

    def requisicao_api_lista_repositorios(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def lista_repositorios(self):
        dados_api = self.requisicao_api_lista_repositorios()
        lista_repositorios_usuario = []
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                lista_repositorios_usuario.append(dados_api[i]['name'])
            return jsonify({'user_id': dados_api[0]['owner']['id'], 
                'username': dados_api[0]['owner']['login'], 
                    'repositories': [lista_repositorios_usuario]}), 200
        else:
            return jsonify({'404': 'Usuario nao encontrado no GitHub!'}), 404

# Classe do segundo Endpoint para listar dados de um repositorio
class ListaDadosRepositorios():

    def __init__(self, usuario, reponame):
        self._usuario = usuario
        self._reponame = reponame

    def requisicao_api_lista_repositorios(self):
        resposta = requests.get(
            f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code

    def lista_repositorios_dados(self):
        dados_api = self.requisicao_api_lista_repositorios()
        reponame_str = f'{self._reponame}'
        count = 0
        if type(dados_api) is not int:
            for index in dados_api:
                count = count + 1
                if index['name'] == reponame_str:
                    return jsonify({'url': dados_api[count-1]['html_url'], 
                        'nome': dados_api[count-1]['name'], 
                            'tipo de acesso': dados_api[count-1]['owner']['type'], 
                                'data de criacao': dados_api[count-1]['created_at'],
                                    'data da ultima alteracao': dados_api[count-1]['updated_at'],
                                        'tamanho': dados_api[count-1]['size'],
                                            'stars': dados_api[count-1]['stargazers_count'],
                                                'watchers': dados_api[count-1]['watchers'],}), 200                                    
            return jsonify({'404': 'Repositorio nao encontrado no GitHub!'}), 404
        else:
            return jsonify({'404': 'Usuario nao encontrado no GitHub!'}), 404   

# Rota home
@app.route('/', methods=['GET'])
def home():
    return "Teste tecnico Captalys - Leonardo Araujo - Home", 200

# Rota do primeiro Endpoint da aplicacao
@app.route('/repositories/<string:username>', methods=['GET'])
def lista_repositorios(username):
    repositorios = ListaRepositorios(username)
    lista_repositorios_pronta = repositorios.lista_repositorios()
    return lista_repositorios_pronta

# Rota do segundo Endpoint da aplicacao
@app.route('/repositories/<string:username>/<string:reponame>', methods=['GET'])
def lista_repositorios_dados(username, reponame): 
    dados_repositorios = ListaDadosRepositorios(username, reponame)
    lista_repositorios_pronta = dados_repositorios.lista_repositorios_dados()
    return lista_repositorios_pronta

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)