import requests as req

#alunos
url = 'http://localhost/alunos'
aluno = {'ra': '1', 'nome': 'Tijolinho'}
ret = req.api.post(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '2', 'nome': 'Gotinha'}
ret = req.api.post(url, json = aluno).json()
print(ret)
#professores

url = 'http://localhost/professores'
professor = {'rp': '1', 'nome': 'ArqueiroVilson'}
ret = req.api.post(url, json = professor).json()
print(ret)

url = 'http://localhost/professores'
professor = {'rp': '2', 'nome': 'Gustavo'}
ret = req.api.post(url, json = professor).json()
print(ret)

#mensagens

url = 'http://localhost/mensagens'
mensagem = {
        'id':'1',
        'ra':'1',
        'titulo':'teste',
        'mensagem':'Isto é um teste',
        'rp':'1',
    }
ret = req.api.post(url, json = mensagem).json()
print(ret)

url = 'http://localhost/mensagens'
mensagem = {
        'id':'2',
        'ra':'2',
        'titulo':'teste1',
        'mensagem':'Isto é um teste2',
        'rp':'2',
    }
ret = req.api.post(url, json = mensagem).json()
print(ret)

url = 'http://localhost/mensagens/listar_enviadas/1'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/mensagens/listar_recebidas/2'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/mensagens/ler/1&1'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/mensagens/ler/2&2'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/mensagens/responder'
resposta = {
        'idResposta':'1',
        'id':'1',
        'rp':'1',
        'mensagem':'teste resposta',
    }
ret = req.api.post(url, json = resposta).json()
print(ret)

url = 'http://localhost/mensagens/deletar/1&1'
ret = req.api.delete(url).json()
print(ret)

url = 'http://localhost/mensagens/arquivar'
mensagem = {
        'id':'2',
        'ra':'2',
        'rp':'2',
    }
ret = req.api.put(url, json = mensagem).json()
print(ret)

url = 'http://localhost/mensagens/listar_recebidas/2'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/mensagens/desarquivar'
mensagem = {
        'id':'2',
        'ra':'2',
        'rp':'2',
    }
ret = req.api.put(url, json = mensagem).json()
print(ret)

url = 'http://localhost/mensagens/listar_recebidas/2'
ret = req.api.get(url).json()
print(ret)

