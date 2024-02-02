from random import randint
from time import sleep

c = 1
b = 0
r = randint(0, 10)
print("-=" * 20)
print("Pensei em um numero entre 0 a 10 e vamos ver se voce acerta")
print("-=" * 20)
sleep(2)
acertou = False
while not acertou:
    b = int(input("Qual o seu palpite?\n:"))
    if b == r:
        print("PARABENS VOCE ACERTOU")
        acertou = True
    elif b > 10:
        print("So vale numeros entre 0 a 5")
    elif b < r:
        print("Voce quase acertou tente chutar  MAIS ALTO")
        c = c + 1
    elif b > r:
        print("Voce quase acertou tente chutar MAIS BAIXO")
        c = c + 1
print(f"Voce teve {c} tentativas para acertar")
