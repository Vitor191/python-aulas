num = []
maior = ""
minimo = ""
for _ in range(0, 5):
    num.append(int(input("Digite um valor")))
maior = max(num)
minimo = min(num)
indice_maior = []
indice_menor = [i for i, nu in enumerate(num) if minimo == nu]
for i, nu in enumerate(num):
    if maior == nu:
        indice_maior.append(i)
print("=-=" * 15)
print(f"Voce digitou os valores {num}")
print(f"O maior numero e {maior} e esta na posicao {indice_maior}")
print(f"O menor numero e {minimo} e esta na posicao {indice_menor}")
