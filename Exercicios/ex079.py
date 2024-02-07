lista = []
a = 0
while True:
    try:
        nu = int(input("Digite um numero:"))
        if nu in lista:
            print("Esse numero ja esta na lista")
        else:
            print("Valor adicionado com sucesso!")
            lista.append(nu)
        a = 0
        print("=-=" * 15)
        while True:
            a = str(input("Voce quer continuar?[S/N]").strip())
            if a in "SsNn":
                break
        if a in "Nn":
            break
    except ValueError:
        print("Voce digitou errado")

b = sorted(lista)
print(b)
