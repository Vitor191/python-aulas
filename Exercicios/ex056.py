nome_lista = []
idade_lista = []
sexo_lista = []
maior_idade = []
maior_idade_nome = []
c = 0
for a in range(0, 4):
    for b in range(2000):
        nome_pessoa = input(f"Digite o nome da pessoa numero {a+1}\n:")
        if nome_pessoa.isalpha():
            nome_lista.append(str(nome_pessoa))
            print("OK")
            break
        else:
            print("Resposta invalida, tente novamente")
    for b in range(2000):
        idade_pessoa = input(f"Digite a idade da pessoa numero {a+1}\n:")
        if idade_pessoa.isnumeric():
            idade_lista.append(int(idade_pessoa))
            print("OK")
            break
        else:
            print("Resposta invalida, tente novamente")
    for b in range(2000):
        print(f"Digite o Sexo da Pessoa numero {a+1}")
        sexo_pessoa = str(input(f"Digite 'H' para Homem E 'M' para mulher\n:")).lower()
        if sexo_pessoa == "h" or sexo_pessoa == "m":
            sexo_lista.append(sexo_pessoa)
            print("OK")
            break
        else:
            print("Resposta invalida, tente novamente")

media = sum(idade_lista) / len(idade_lista)
print(f"A media da idade da lista e {media} anos")

maior_idade = [0]
for a in range(0, 4):
    if sexo_lista[a] == "h":
        if maior_idade[0] <= idade_lista[a]:
            maior_idade[0] = idade_lista[a]

for a in range(0, 4):
    if sexo_lista[a] == "h" and idade_lista[a] == maior_idade[0]:
        maior_idade_nome.append(nome_lista[a])
if maior_idade != 0:
    print(
        f"A(s) pessoa(s) do sexo masculino com maior idade sao {maior_idade_nome} com {max(maior_idade)} anos"
    )
for a in range(0, 4):
    if (idade_lista[a] < 20) and (sexo_lista[a] == "m"):
        c = c + 1
print(f"Na lista de 4 pessoas tem {c} mulheres abaixo de 20 anos")
