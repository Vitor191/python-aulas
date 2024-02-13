aluno = {}
aluno["nome"] = str(input("Nome:"))
aluno["media"] = float(input(f"Media de {aluno["nome"]}:"))
if aluno["media"] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f"Nome e igual a {aluno["nome"]}")
print(f'A media e igual a {aluno["media"]}')
print(f'A situacao do aluno e igual a {aluno['situacao']}')
