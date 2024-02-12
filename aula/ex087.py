lista = []
linha = []
soma = soma3 = b = mai = 0
for a in range(3):
    for b in range(3):
        linha.append(int(input(f"Digiteo numero na posicao [{a}],[{b}]:")))
    lista.append(linha[:])
    linha.clear()
for a in range(3):
    for b in range(3):
        print(f"[{lista[a][b]:^5}]", end=" ")
        if lista[a][b] % 2 == 0:
            soma += lista[a][b]
        if b == 2:
            soma3 += lista[a][2]
    print()
mai = max(lista[1])
print(f"A soma dos valores pares e {soma}")
print(f"A soma dos valores na terceira coluna e {soma3}")
print(f"O maior valor da segunda linha e {mai}")
