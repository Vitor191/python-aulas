lista = []
linha = []
soma = soma3 = b = mai = 0
for a in range(3):
    for b in range(3):
        linha.append(int(input(f"Digiteo numero na posicao [{a}],[{b}]:")))
    lista.append(linha[:])
    linha.clear()
for a in lista:
    print(a)
for linha in lista:
    for a in range(3):
        if linha[a] % 2 == 0:
            soma += linha[a]
        if a == 2:
            soma3 += linha[a]
mai = max(lista[1])
print(f"A soma dos valores pares e {soma}")
print(f"A soma dos valores na terceira coluna e {soma3}")
print(f"O maior valor da segunda linha e {mai}")
