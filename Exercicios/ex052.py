n = int(input("Digite o numero pra ver se ele e primo:"))
if n <= 1:
    print("Nao e primo")
for a in range(2, int(n**0.5) + 1):
    if n % a == 0:
        primo = 0
        break
    else:
        primo = 1
if primo == 0:
    print("Nao e primo pois e dividido pelo numero", a)
else:
    print("E primo")
