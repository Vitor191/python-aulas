lista = []
linha = []
soma = soma3 = b = mai = 0
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = b = mai = 0
for c in range(3):
    for l in range(3):
        lista[l][c] = int(input(f"Digiteo numero na posicao [{l}],[{c}]:"))
for c in range(3):
    for l in range(3):
        print(f"[{lista[l][c]:^5}]", end="")
    print()
