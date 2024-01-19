# Meu exercicio
# num = int(input("Digite um numero dentro de 0 a 9999:"))
# num = num % 10000
# m = num // 1000
# c = (num % 1000) // 100
# d = (num % 100) // 10
# u = num % 10
# print(f"unidade:{u}\ndezena:{d}\ncentena:{c}\nmilhar:{m}")

# Correcao do professor

num = float(input("informe um numero"))
num = num % 10000
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o numero: {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
