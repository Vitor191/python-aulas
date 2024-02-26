# from random import randint
from random import sample


def sorteia(lst):
    b = sample(range(0, 10), 5)
    lst.extend(b)
    print(lst)


def somaPar(z):
    c = 0
    print("Os numeros Pares sao: ")
    for a in z:
        if a % 2 == 0:
            print(f"{a}", end=" ")
            c += a
    print()
    print(f"A soma dos numeros pares sao {c}")


numeros = []
sorteia(numeros)
somaPar(numeros)
