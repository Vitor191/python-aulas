Par = []
Impar = []
numeros = []
for b in range(1, 8):
    a = int(input(f"Digite o numero {b}:"))
    if a % 2 == 0:
        Par.append(a)
    else:
        Impar.append(a)
Par.sort()
Impar.sort()
numeros.append(Par[:])
numeros.append(Impar[:])
print(f"Os numeros PARES sao {numeros[0]}")
print(f"Os numeros IMPARES sao {numeros[1]}")
