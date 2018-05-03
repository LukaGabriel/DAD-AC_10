from Server import app
from Models.Response import response
from flask import jsonify

@app.errorhandler(500)
def TrataErroServerError(error):
    response['Status'] = 'Erro'
    response['Dados'] = '{0}'.format(error)
    response['Mensagem'] = 'Tivemos um problema interno pedimos desculpas pelo inconveniente'
    return jsonify(response)

@app.errorhandler(404)
def TrataErroNotFound(error):
    response['Status'] = 'Erro'
    response['Dados'] = ''
    response['Mensagem'] = 'URL não encontrada'
    return jsonify(response)

@app.errorhandler(403)
def TrataErroForbiden(error):
    response['Status'] = 'Erro'
    response['Dados'] = ''
    response['Mensagem'] = 'Entrada não autorizada'
    return jsonify(response)

@app.errorhandler(400)
def TrataErroIvadidRequisition(error):
    response['Status'] = 'Erro'
    response['Dados'] = ''
    response['Mensagem'] = 'Requisicao inválida'
    return jsonify(response)