#Alunos
from Alunos.Services.ListarAlunos import ListarAlunos
from Alunos.Services.ConsultarPorRa import ConsultarPorRa
from Alunos.Services.CadastrarAluno import CadastrarAluno
from Alunos.Services.AlterarAluno import AlterarAluno
from Alunos.Services.InativarAluno import InativarAluno
#Professores
from Professores.Services.ListarProfessores import ListarProfessores
from Professores.Services.ConsultarPorRaP import ConsultarPorRaP
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