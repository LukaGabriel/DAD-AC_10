from Models.Professores import professores

def CadastrarProfessor(dados):
    professor = {'rp': dados['rp'], 'nome': dados['nome']}
    if professor not in professores:
        professores.append(professor)
        return professores
    return professores