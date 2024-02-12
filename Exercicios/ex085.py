numeros = [[], []]
for b in range(1, 8):
    a = int(input(f"Digite o numero {b}:"))
    if a % 2 == 0:
        numeros[0].append(a)
    else:
        numeros[1].append(a)
numeros[0].sort()
numeros[1].sort()
print(f"Os numeros PARES sao {numeros[0]}")
print(f"Os numeros IMPARES sao {numeros[1]}")
