from Models.Mensagens import mensagens
from Models.Alunos import alunos
from Models.Professores import professores

def ArquivarMensagem(dados):
    for aluno in alunos:
        if aluno['ra'] == dados['ra']:
            for mensagem in range(len(mensagens)):
                if mensagens[mensagem]['id'] == dados['id']:
                    mensagens[mensagem]['status'] = False
                    return 'A mensagem foi arquivada'
            return 'Mensagem não encontrada'
    for professor in professores:
        if professor['rp'] == dados['rp']:
            for mensagem in range(len(mensagens)):
                if mensagens[mensagem]['id'] == dados['id']:
                    mensagens[mensagem]['status'] = False
                    return 'A mensagem foi arquivada'
            return 'Mensagem não encontrada'
    return 'Você não tem este poder!'