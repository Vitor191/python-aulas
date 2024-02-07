lista = []
while True:
    while True:
        a = input("Digite um numero")
        if a.isdigit():
            a = int(a)
            lista.append(a)
            break
    while True:
        b = str(input("Deseja continuar?[S/N]"))
        if b in "SsNn":
            break
    if b in "Nn":
        break
print(f"Foram digitados {len(lista)} numeros")
lista.sort(reverse=True)
print("A lista na forma decrecente fica ", lista)
if 5 in lista:
    print(f"O valor 5 faz parte dessa lista")
else:
    print("O valor 5 nao faz parte dessa lista")
