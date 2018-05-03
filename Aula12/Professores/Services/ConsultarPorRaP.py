from Models.Professores import professores

def ConsultarPorRaP(rp):
    for professor in professores:
        if professor['rp'] == rp:
            return professor
    return 'Professor não encontrado'