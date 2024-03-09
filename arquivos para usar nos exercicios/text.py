nome_lista = []
idade_lista = []
sexo_lista = []
for a in range(0, 4):
    # nome_pessoa = str(input(f"Digite o nome da pessoa numero {fim+1}"))
    # nome_lista.append(nome_pessoa)
    #  idad_pessoa = int(input(f"Digite fim idade da pessoa numero {fim+1}"))
    #   idade_lista.append(idad_pessoa)
    sexo_pessoa = str(input(f"Digite H para Homem ou M para a pessoa {a+1}")).lower()
    for b in range(2):
        if sexo_pessoa not in ["h", "m"]:
            print(f".Resposta invalida.Digite H para Homem ou M para a pessoa {a+1}")
            sexo_pessoa = str(
                input(f"Digite H para Homem ou M para a pessoa {a+1}")
            ).lower()
    sexo_lista.append(sexo_pessoa)
# media = sum(idade_lista) / len(idade_lista)
# print(f"A media das idades e {media} anos")
