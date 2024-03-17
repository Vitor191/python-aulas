n = a = 0
while True:
    print("=-=" * 15)
    n = int(input("Digite o numero que voce quer saber fim tabuada:"))
    print("=-=" * 15)

    a = 1
    if n < 0:
        break
    while a <= 10:
        print(f"{n}x{a} = {n*a}")
        a += 1
print("Fim")
