from Models.Mensagens import mensagens
from Models.Professores import professores
from datetime import datetime
now = datetime.now()

def ResponderMensagem(dados):
    resposta = {
        'idResposta':dados['idResposta'],
        'id':dados['id'],
        'rp':dados['rp'],
        'mensagem':dados['mensagem'],
        'data':now,
    }
    for professor in professores:
        if professor['rp'] == dados['rp']:
            for mensagem in mensagens:
                if mensagem['id'] == dados['id']:
                    mensagem['respostas'].append(resposta)
                    return resposta
            return 'Mensagem não encontrada'
    return 'Você não tem esse poder!'