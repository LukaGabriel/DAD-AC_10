import requests as req
url = 'http://localhost/professores'
url = 'http://localhost/alunos'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '1', 'nome': 'Tijolinho'}
ret = req.api.post(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '2', 'nome': 'Gotinha'}
ret = req.api.post(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '3', 'nome': 'Peninha'}
ret = req.api.post(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '1', 'nome': 'Tijolinho'}
ret = req.api.post(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/alunos/1'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/alunos/4'
ret = req.api.get(url).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '1', 'nome': 'Abacaxi'}
ret = req.api.put(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '4', 'nome': 'Abacaxi'}
ret = req.api.put(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos'
aluno = {'ra': '5', 'nome': 'Abaxial'}
ret = req.api.put(url, json = aluno).json()
print(ret)

url = 'http://localhost/alunos/2'
ret = req.api.delete(url).json()
print(ret)

url = 'http://localhost/alunos/5'
ret = req.api.delete(url).json()
print(ret)

url = 'http://localhost/teste'
ret = req.api.delete(url).json()
print(ret)


#professores

url = 'http://localhost/professores'
professor = {'rp': '1', 'nome': 'ArqueiroVilson'}
ret = req.api.post(url, json = professor).json()
print(ret)

url = 'http://localhost/professores'
professor = {'rp': '20', 'nome': 'Gustavo'}
ret = req.api.post(url, json = professor).json()
print(ret)