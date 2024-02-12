from random import sample
from time import sleep

a = "JOGO DA MEGA SENA"
print("{:-^40}".format(""))
print(f"{a:^40}")
print("{:-^40}".format(""))
n = int(input("Quantos numeros voce quer que eu sorteie?"))
print(f" Sorteando {n} jogos ".center(40, "="))
for b in range(n):
    c = sample(range(1, 61), 6)
    c.sort()
    print(f"Jogo {b+1}:{c}")
    c.clear()
    sleep(1)
print(" Boa sorte ".center(40, "="))
