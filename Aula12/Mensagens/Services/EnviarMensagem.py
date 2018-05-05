from Models.Mensagens import mensagens
from Models.Alunos import alunos
from datetime import datetime
now = datetime.now()

def EnviarMensagem(dados):
    mensagem = {
        'id':dados['id'],
        'ra':dados['ra'],
        'titulo':dados['titulo'],
        'mensagem':dados['mensagem'],
        'rp':dados['rp'],
        'data':now,
        'status':True,
        'respostas':[],
        'lida':False
    }
    for aluno in alunos:
        if dados['ra'] == aluno['ra']:
            if mensagem not in mensagens:
                mensagens.append(mensagem)
                return mensagem
    return 'Você não é um aluno'
