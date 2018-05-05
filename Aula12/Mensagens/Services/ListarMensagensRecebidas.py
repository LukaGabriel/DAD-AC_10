from Models.Mensagens import mensagens
from Models.Professores import professores

def ListarMensagensRecebidas(rp):
    mensagens_prof = []
    for prof in professores:
        if prof['rp'] == rp:
            for mensagem in mensagens:
                if mensagem['rp'] == prof['rp']:
                    if mensagem['status']:
                        if mensagem['id'] not in mensagens_prof:
                            mensagens_prof.append(mensagem)
            return mensagens_prof
    return 'Professor não encontrado'