lista = (
    int(input("Digite o numero 1:")),
    int(input("Digite o numero 2:")),
    int(input("Digite o numero 3:")),
    int(input("Digite o numero 4:")),
)
print(f"O numero 9 apareceu um total de {lista.count(9)} vezes")
if 3 in lista:
    print(f"O numero apareceu primeiro na posicao {lista.index(3)}")
else:
    print("O valor 3 Nao foi digitado em nenhuma posicao")
print(f"Os numeros pares sao ", end="")
for a in lista:
    if a % 2 == 0:
        print(a, end=" ")
