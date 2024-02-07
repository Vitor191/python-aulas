lista = []
a = ""

for b in range(0, 5):
    a = int(input("Digite um numero:"))

    inserido = False
    for c, nu in enumerate(lista):
        if a <= nu:
            lista.insert(c, a)
            inserido = True
            break
    if not inserido:
        lista.append(a)
print(lista)
