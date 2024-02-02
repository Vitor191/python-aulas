from time import sleep

print("Ola")

a = int(input("Digite o primeiro numero:"))
b = int(input("Digite o segundo numero:"))
d = 0
while d != 1:
    c = int(
        input(
            """Digite qual operacao voce quer fazer
[1]Soma
[2]Multiplicar
[3]Maior
[4]Novos valores
[5]Para sair
:"""
        )
    )

    if c == 1:
        print(f"A soma entre o numero {a} e {b} e igaul a: ", a + b)
    elif c == 2:
        print(f"A multiplicacao entre o numero {a} e {b} e igaul a: ", a * b)
    elif c == 3:
        m = max(a, b)
        print(f"O maior numero entre {a} e {b} igual a :", m)
    elif c == 4:
        print("Digite novos valores")
    elif c == 5:
        d = d + 1
    else:
        print("Nao existe essa operacao")
    sleep(2)
print("Tchau")
