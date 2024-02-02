g = 0
a = 0
b = 0
while g == 0:
    n = int(input("Digite o numero que ira ser somado:"))
    if n != 999:
        a += n
        b = b + 1
    elif n == 999:
        g = 1
print(f"Foram digitados {b} valores e somados sao {a}")
