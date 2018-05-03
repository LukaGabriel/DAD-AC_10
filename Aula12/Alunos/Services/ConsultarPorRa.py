from Models.Alunos import alunos

def ConsultarPorRa(ra):
    for aluno in alunos:
        if aluno['ra'] == ra:
            return aluno
    return 'Aluno não encontrado'