#Alunos
from Alunos.Services.ListarAlunos import ListarAlunos
from Alunos.Services.ConsultarPorRa import ConsultarPorRa
from Alunos.Services.CadastrarAluno import CadastrarAluno
from Alunos.Services.AlterarAluno import AlterarAluno
from Alunos.Services.InativarAluno import InativarAluno
#Professores
from Professores.Services.ListarProfessores import ListarProfessores
from Professores.Services.ConsultarPorRp import ConsultarPorRp
from Professores.Services.CadastrarProfessor import CadastrarProfessor
from Professores.Services.AlterarProfessor import AlterarProfessor
from Professores.Services.InativarProfessor import InativarProfessor
#Mensagens
from Mensagens.Services.EnviarMensagem import EnviarMensagem
from Mensagens.Services.ListarMensagensRecebidas import ListarMensagensRecebidas
from Mensagens.Services.ListarMensagensEnviadas import ListarMensagensEnviadas
from Mensagens.Services.ResopnderMensagem import ResponderMensagem
from Mensagens.Services.LerMensagem import LerMensagem
from Mensagens.Services.ArquivarMensagem import ArquivarMensagem
from Mensagens.Services.ExcluirMensagem import ExcluirMensagem
from Mensagens.Services.DesarquivarMensagem import DesarquivarMensagem
#Imports Gerais
from flask import jsonify, request
from Server import app
from Models.Response import response

@app.route('/alunos', methods = ['GET'])
def ListarAlunosRota():
    response['Status'] = 'Sucesso'
    response['Dados'] = ListarAlunos()
    response['Mensagem'] = 'Lista de alunos cadastrados'
    return jsonify(response)

@app.route('/alunos/<ra>', methods = ['GET'])
def ConsultarPorRaRota(ra):
    response['Status'] = 'Sucesso'
    response['Dados'] = ConsultarPorRa(ra)
    response['Mensagem'] = 'Lista de alunos consultada'
    return jsonify(response)

@app.route('/alunos', methods = ['POST'])
def CadastrarAlunoRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = CadastrarAluno(dados)
    response['Mensagem'] = 'Aluno Cadastrado'
    return jsonify(response)

@app.route('/alunos', methods = ['PUT'])
def AlterarAlunoRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = AlterarAluno(dados)
    response['Mensagem'] = 'Alterar Aluno'
    return jsonify(response)

@app.route('/alunos/<ra>', methods = ['DELETE'])
def InvalidarAlunoRota(ra):
    response['Status'] = 'Sucesso'
    response['Dados'] = InativarAluno(ra)
    response['Mensagem'] = 'Inativar Aluno'
    return jsonify(response)

@app.route('/professores', methods = ['GET'])
def ListarProfessoresRota():
    response['Status'] = 'Sucesso'
    response['Dados'] = ListarProfessores()
    response['Mensagem'] = 'Lista de professores cadastrados'
    return jsonify(response)

@app.route('/professores/<rp>', methods = ['GET'])
def ConsultarPorRpRota(rp):
    response['Status'] = 'Sucesso'
    response['Dados'] = ConsultarPorRp(rp)
    response['Mensagem'] = 'Lista de professores consultada'
    return jsonify(response)

@app.route('/professores', methods = ['POST'])
def CadastrarProfessorRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = CadastrarProfessor(dados)
    response['Mensagem'] = 'Professor Cadastrado'
    return jsonify(response)

@app.route('/professores', methods = ['PUT'])
def AlterarProfessorRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = AlterarProfessor(dados)
    response['Mensagem'] = 'Alterar Professor'
    return jsonify(response)

@app.route('/professores/<rp>', methods = ['DELETE'])
def InvalidarProfessorRota(rp):
    response['Status'] = 'Sucesso'
    response['Dados'] = InativarProfessor(rp)
    response['Mensagem'] = 'Inativar Professor'
    return jsonify(response)

@app.route('/mensagens', methods = ['POST'])
def EnviarMensagemRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = EnviarMensagem(dados)
    response['Mensagem'] = 'Mensagem Enviada'
    return jsonify(response)

@app.route('/mensagens/listar_enviadas/<ra>', methods = ['GET'])
def ListarMensagensEnviadasRota(ra):
    response['Status'] = 'Sucesso'
    response['Dados'] = ListarMensagensEnviadas(ra)
    response['Mensagem'] = 'Lista de Mensagens Enviadas'
    return jsonify(response)

@app.route('/mensagens/listar_recebidas/<rp>', methods = ['GET'])
def ListarMensagensRecebidasRota(rp):
    response['Status'] = 'Sucesso'
    response['Dados'] = ListarMensagensRecebidas(rp)
    response['Mensagem'] = 'Lista de Mensagens Recebidas'
    return jsonify(response)

@app.route('/mensagens/ler/<id>&<rp>', methods = ['GET'])
def LerMensagemRota(id, rp):
    response['Status'] = 'Sucesso'
    response['Dados'] = LerMensagem(id, rp)
    response['Mensagem'] = 'Leitura de Mensagem'
    return jsonify(response)

@app.route('/mensagens/responder', methods = ['POST'])
def ResponderMensagemRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = ResponderMensagem(dados)
    response['Mensagem'] = 'Responder Mensagem'
    return jsonify(response)

@app.route('/mensagens/deletar/<id>&<register>', methods = ['DELETE'])
def ExcluirMensagemRota(id, register):
    response['Status'] = 'Sucesso'
    response['Dados'] = ExcluirMensagem(id, register)
    response['Mensagem'] = 'Excluir Mensagem'
    return jsonify(response)

@app.route('/mensagens/arquivar', methods = ['PUT'])
def ArquivarMensagemRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = ArquivarMensagem(dados)
    response['Mensagem'] = 'Arquivar Mensagem'
    return jsonify(response)

@app.route('/mensagens/desarquivar', methods = ['PUT'])
def DesarquivarMensagemRota():
    dados = request.get_json()
    response['Status'] = 'Sucesso'
    response['Dados'] = DesarquivarMensagem(dados)
    response['Mensagem'] = 'Desarquivar Mensagem'
    return jsonify(response)