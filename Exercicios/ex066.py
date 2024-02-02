n = soma = cont = 0
while True:
    n = int(input("Digite um numero inteiro [Digite 999 para parar]:"))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"Foram digitados {cont} numeros e somando todos eles sao {soma}")
