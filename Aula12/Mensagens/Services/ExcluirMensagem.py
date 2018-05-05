from Models.Mensagens import mensagens
from Models.Alunos import alunos
from Models.Professores import professores

def ExcluirMensagem(id, register):
    for aluno in alunos:
        if aluno['ra'] == register:
            for mensagem in range(len(mensagens)):
                if mensagens[mensagem]['id'] == id:
                    mensagens.pop(mensagem)
                    return 'A mensagem foi excluida'
            return 'Mensagem não encontrada'
    for professor in professores:
        if professor['rp'] == register:
            for mensagem in range(len(mensagens)):
                if mensagens[mensagem]['id'] == id:
                    mensagens.pop(mensagem)
                    return 'A mensagem foi excluida'
            return 'Mensagem não encontrada'
    return 'Você não tem este poder!'