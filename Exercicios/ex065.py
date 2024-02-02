soma = media = quant = n = maior = menor = 0
g = "s"
while g in "s":
    a = int(input("Digite um numero:"))
    soma += a
    n += 1
    if maior <= a:
        maior = a
    if menor == 0 and n == 1:
        menor = a
    if menor >= a:
        menor = a
    b = str(input("Voce quer continuar [S/N]?\n:").lower())
    if b == "n":
        g = "n"

media = soma / n
print(f"Foram digitados {n} valores")
print(
    f"A media entre os valores digitados sao:{media:.2f}",
)
print(f"O menor valor digitado e {menor} e o maior valor digitado e {maior}")
