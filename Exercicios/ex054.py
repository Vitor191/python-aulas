from datetime import datetime

data_atual = datetime.now()
lista = []
for a in range(0, 7):
    ano_nascimento = int(input("Digite o ano de nascimento"))
    lista.append(ano_nascimento)
for a in range(0, 7):
    idade = data_atual.year - lista[a]
    if idade < 18:
        print(f"A pessoa numero {a+1} possui {idade} e nao atingiu a maioridade")
    else:
        print(f"A pessoa numero {a+1} possui {idade} e atingiu a maioridade")
