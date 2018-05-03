from Models.Alunos import alunos

def CadastrarAluno(dados):
    aluno = {'ra': dados['ra'], 'nome': dados['nome']}
    if aluno not in alunos:
        alunos.append(aluno)
        return alunos
    return alunos