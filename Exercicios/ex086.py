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
