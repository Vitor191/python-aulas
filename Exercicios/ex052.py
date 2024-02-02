primo = 0
c = 0
n = int(input("Digite o numero pra ver se ele e primo:"))
for a in range(1, n + 1):
    if n % a == 0:
        c += 1
print(f"ele foi dividdido por {c} numeros por isso ele e ", end="")
if c <= 2:
    print("Primo")
else:
    print("Nao e primo")
