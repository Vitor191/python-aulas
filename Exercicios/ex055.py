lista = []
for a in range(0, 5):
    peso_pessoas = int(input(f"Digite o peso da pessoa {a+1}"))
    lista.append(peso_pessoas)
maior = max(lista)
posicao_maior = lista.index(maior) + 1
menor = min(lista)
posicao_menor = lista.index(menor) + 1
print(f"O maior peso foi da pessoa numero {posicao_maior} com {maior} Kilos")
print(f"O menor peso foi da pessoa numero {posicao_menor} com {menor} Kilos")
