from Models.Mensagens import mensagens
from Models.Professores import professores
from datetime import datetime
now = datetime.now()

def LerMensagem(id, rp):
    for professor in professores:
        if professor['rp'] == rp:
            for mensagem in mensagens:
                if mensagem['id'] == id:
                    mensagem['lida'] = now
                    return mensagem
            return 'Mensagem não encontada'
    return 'Você não tem este poder!' 