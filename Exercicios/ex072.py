numeros_por_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    n = input("Digite um numero de zero a vinte:")
    if n.isdigit():
        n = int(n)
        if 0 <= n <= 20:
            print("Voce digitou o numero:", numeros_por_extenso[n])
            break
        else:
            print("Voce digitou errado")
    else:
        print("Voce digitou errado")
print("Fim")
