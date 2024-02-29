def leiaint(msg):
    while True:
        a = input("Digite um numero:")
        if a.isdigit():
            a = int(a)
            break
        else:
            print("\033[91mERRO!! Você acabou de digitar um número inválido\033[0m")
    return a


n = leiaint("Digite um numero:")
print(f"Voce acabou de digitar o numero {n}")
