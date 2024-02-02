from time import sleep

a = int(input("Digite o numero que voce quer saber a progrecao:"))
b = int(input("Digite a razao da progrecao:"))
c = 0
d = 10
e = 0
g = 0
print("-=" * 20)
while e == 0:
    d = d + g
    while c != d:
        print(a, end=",")
        a = a + b
        c = c + 1
    print("\n")
    print("-=" * 20)
    sleep(2)
    g = 0
    while g == 0:
        f = int(
            input(
                """\nVoce gostaria de adicionar mais algum outro termo nessa PA?
Digite:
[1] Para Sim
[2] Para Nao
:"""
            )
        )
        if f == 1:
            g = int(
                input("Digite mais quantos termos voce gostaria de ver a frente?\n:")
            )
            print("-=" * 20)
            sleep(2)
        elif f == 2:
            e = 1
            g = 1
            print("-=" * 20)
            sleep(2)
        elif f != 1 and f != 2:
            print("Essa opcao nao existe")
            print("-=" * 20)
            sleep(2)
print("Tenha um bom dia")
