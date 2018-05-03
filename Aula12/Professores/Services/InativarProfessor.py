from Models.Professores import professores

def InativarProfessor(rp):
    for professor in range(len(professores)):
        if professores[professor]['rp'] == rp:
            professores.pop(professor)
            return professores
    return 'Professor não encontrado'