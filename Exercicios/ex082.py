lista = []
lista_p = []
lista_i = []
while True:
    while True:
        n = input("Digite um numero:")
        if n.isdigit():
            n = int(n)
            lista.append(n)
            break
    while True:
        a = str(input("Deseja contibuar?[S/N]"))
        if a in "SsNn":
            break
    if a in "Nn":
        for a in lista:
            if a % 2 == 0:
                lista_p.append(a)
            else:
                lista_i.append(a)
        break
print("os numeros digitados foram:", lista)
print("Os numeros Pares digitados foram", lista_p)
print("Os numeros Impares digitados fooram", lista_i)
