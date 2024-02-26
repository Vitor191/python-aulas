from time import sleep


def contador(inicio, fim, passo):
    a = 1
    if inicio > fim:
        a = -1
    if passo == 0:
        passo = 1
    if fim > inicio and passo < 0 or inicio > fim and passo > 0:
        passo *= -1
    print(f"Contagem de {inicio} ate {fim} de {abs(passo)} em {abs(passo)}")
    print("=" * 25)
    for inicio in range(inicio, fim + a, passo):
        print(inicio, end=" ")
        sleep(0.5)
    print()


contador(0, 10, 1)
contador(10, 0, -2)
print("Agora e sua vez de fazer sua contagem")
print("=" * 25)
contador(int(input("De: ")), int(input("Até: ")), int(input("Passo: ")))
