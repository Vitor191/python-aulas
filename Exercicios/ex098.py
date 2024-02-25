from time import sleep


def contador():
    print("Contagem de 1 ate 10 de 1 em 1")
    print("=" * 25)
    for a in range(1, 11):
        print(a, end=" ")
        sleep(0.5)
    print()
    print("Contagem de 10 ate 0 de 2 em 2")
    print("=" * 25)
    for a in range(10, -1, -2):
        print(a, end=" ")
        sleep(0.5)
    print()
    print("Agora e a sua vez de fazer a sua contagem")
    print("=" * 25)
    a = int(input("Inicio:"))
    b = int(input("Fim:"))
    c = int(input("Passo:"))
    if a < b:
        if c < 0:
            c = c * (-1)
        elif c == 0:
            c = 1
        print(f"Contagem de {a} ate {b} de {c} em {c}")
        print("=" * 25)
        for a in range(a, b, c):
            print(a, end=" ")
            sleep(0.5)
    elif a > b:
        d = c
        if c > 0:
            c = c * (-1)
        elif c == 0:
            c = -1
        if d < 0:
            d = d * (-1)
        elif d == 0:
            d == 1
        print(f"Contagem de {a} ate {b} de {d} em {d}")
        print("=" * 25)
        for a in range(a, b, c):
            print(a, end=" ")
            sleep(0.5)


contador()
