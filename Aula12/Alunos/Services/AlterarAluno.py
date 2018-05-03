from Models.Alunos import alunos

def AlterarAluno(dados):
    for aluno in alunos:
        if dados['ra'] == aluno['ra']:
            aluno['nome'] = dados['nome']
            return aluno
        elif dados['nome'] == aluno['nome']:
            aluno['ra'] = dados['ra']
            return aluno
    return 'Aluno não encontrado'
            
