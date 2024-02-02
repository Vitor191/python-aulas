from random import randint
from time import sleep

r = randint(0, 5)  # faz o computador gerar um numero aleatorio entre 0 e 5
# print(r)
print("-=-" * 15)
n = int(input("Digite um numero de 0 a 5:"))
print("-=-" * 15)
print("PROCESSANDO...")
sleep(0)

print(f"Voce digitou {n}, o Computador pois {r}")
if n == r:
    print(f"Parabens voce conseguiu acertar o numero")
else:
    print("nao foi dessa vez, tente outra mais tarde")
