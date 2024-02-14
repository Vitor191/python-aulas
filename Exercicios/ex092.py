from datetime import datetime

data = datetime.now()
pessoa = {}
pessoa["nome"] = str(input("Nome:"))
nacimento = int(input("Ano de nasciment:"))
idade = data.year - nacimento
pessoa["idade"] = idade
pessoa["ctps"] = int(input("CTPS:(0 nao tem)"))
if pessoa["ctps"] != 0:
    pessoa["ano"] = int(input("Ano de contratacao:"))
    pessoa["salario"] = int(input("Salario: R$"))
    pessoa["aposentadoria"] = (pessoa["ano"] + 35) - nacimento
for k, v in pessoa.items():
    print(f"{k} tem valor {v}")
