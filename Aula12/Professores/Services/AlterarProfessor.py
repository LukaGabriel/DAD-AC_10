from Models.Professores import professores

def AlterarProfessor(dados):
    for professor in professores:
        if dados['rp'] == professor['rp']:
            professor['nome'] = dados['nome']
            return professor
        elif dados['nome'] == professor['nome']:
            professor['rp'] = dados['rp']
            return professor
    return 'Professor não encontrado'