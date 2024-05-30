from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Dicionários para armazenar os dados recebidos dos bancos
dados_base = []
dados_cliente = []
regras_negocio = []

# Rota para receber os dados do Banco 1
@app.route('/banco1', methods=['POST'])
def receber_dados_banco1():
    dados = request.json
    dados_base.extend(dados)
    return "Dados do Banco 1 recebidos com sucesso!", 200

# Rota para receber os dados do Banco 2
@app.route('/banco2', methods=['POST'])
def receber_dados_banco2():
    dados = request.json
    dados_cliente.extend(dados)
    return "Dados do Banco 2 recebidos com sucesso!", 200

# Rota para receber os dados do Banco 3
@app.route('/banco3', methods=['POST'])
def receber_dados_banco3():
    dados = request.json
    regras_negocio.extend(dados)
    return "Dados do Banco 3 recebidos com sucesso!", 200

# Rota para consolidar os dados e aplicar regras de negócio
@app.route('/consolidar', methods=['GET'])
def consolidar_dados():
    # Aqui você faria a lógica para consolidar os dados e aplicar as regras de negócio
    # Por simplicidade, vamos apenas juntar todos os dados em um único dicionário
    dados_consolidados = {
        "dados_base": dados_base,
        "dados_cliente": dados_cliente,
        "regras_negocio": regras_negocio
    }
    return jsonify(dados_consolidados), 200

# Rota para enviar o arquivo CSV para o servidor de envio
@app.route('/enviar_arquivo', methods=['POST'])
def enviar_arquivo():
    # Nome do arquivo CSV a ser enviado
    nome_arquivo = 'arquivo_lote.csv'
    # End-point para chamada de conexão
    endpoint = 'coloque servidor de envio'
    # AppKey / chave utilizada
    app_key = 'chave de acesso'
    # Hostname do servidor de envio
    hostname = 'host'

    # Verifica se o arquivo existe
    if os.path.exists(nome_arquivo):
        # Envia o arquivo CSV para o servidor de envio
        files = {'file': (nome_arquivo, open(nome_arquivo, 'rb'), 'text/csv')}
        headers = {'AppKey': app_key, 'Hostname': hostname}
        resposta = requests.post(endpoint, files=files, headers=headers)
        if resposta.status_code == 200:
            return "Arquivo enviado com sucesso!", 200
        else:
            return "Erro ao enviar o arquivo.", 500
    else:
        return "Arquivo não encontrado.", 404

if __name__ == '__main__':
    app.run(debug=True)
