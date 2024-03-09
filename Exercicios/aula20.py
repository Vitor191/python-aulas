def soma(a, b):
    s = a + b
    print(s)


def contador(*num):
    tam = len(num)
    print(f"Recei oc valores {num} e sao ao todo {tam} numeros")


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


# Programa Principal
c = [2, 4, 5, 6]
dobra(c)
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
