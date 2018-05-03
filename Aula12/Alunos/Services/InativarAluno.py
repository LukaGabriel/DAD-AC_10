from Models.Alunos import alunos

def InativarAluno(ra):
    for aluno in range(len(alunos)):
        if alunos[aluno]['ra'] == ra:
            alunos.pop(aluno)
            return alunos
    return 'Aluno não encontrado'