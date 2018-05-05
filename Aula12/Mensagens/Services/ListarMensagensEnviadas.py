from Models.Mensagens import mensagens
from Models.Alunos import alunos

def ListarMensagensEnviadas(ra):
    mensagens_aluno = []
    for aluno in alunos:
        if aluno['ra'] == ra:
            for mensagem in mensagens:
                if aluno['ra'] == mensagem['ra']:
                    if mensagem['status']:
                        if mensagem['id'] not in mensagens_aluno:
                            mensagens_aluno.append(mensagem)
            return mensagens_aluno
    return 'Aluno não encontrado'    