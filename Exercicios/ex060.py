# a = int(input("Digite o numero que voce quer saber o seu fatorial:"))
# nome_bara = 1
# c = a
# while c > 0:
#     nome_bara *= c
#     c -= 1
# print(f"a fatorial do numero {a} e igual a :", nome_bara)
n = int(input("Digite o numero para calcular sua fatorial:"))
c = n
f = 1
print(f"Calculando {n}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f)
print("Tchau")
