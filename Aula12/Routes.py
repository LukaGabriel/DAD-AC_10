from Alunos.Services.ListarAlunos import ListarAlunos
from Alunos.Services.ConsultarPorRa import ConsultarPorRa
from Alunos.Services.CadastrarAluno import CadastrarAluno
from Alunos.Services.AlterarAluno import AlterarAluno
from Alunos.Services.InativarAluno import InativarAluno

from Professores.Services.ListarProfessores import ListarProfessores
from Professores.Services.ConsultarPorRaP import ConsultarPorRaP
from Professores.Services.CadastrarProfessor import CadastrarProfessor
from Professores.Services.AlterarProfessor import AlterarProfessor
from Professores.Services.InativarProfessor import InativarProfessor

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

@app.route('/professores/<ra>', methods = ['GET'])
def ConsultarPorRaPRota(ra):
    response['Status'] = 'Sucesso'
    response['Dados'] = ConsultarPorRa(ra)
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

@app.route('/professores/<ra>', methods = ['DELETE'])
def InvalidarProfessorRota(ra):
    response['Status'] = 'Sucesso'
    response['Dados'] = InativarProfessor(ra)
    response['Mensagem'] = 'Inativar Aluno'
    return jsonify(response)