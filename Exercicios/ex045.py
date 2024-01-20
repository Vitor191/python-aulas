# from random import choice
#
# lista = ["Pedra", "Papel", "Tesoura"]
# a = choice(lista)
# print(a)
# b = int(input("Escolha:\n1 para Pedra.\n2 para Papel\n3 para Tesoura\n:"))
#
# if b == 1:
#     c = "Pedra"
# elif b == 2:
#     c = "Papel"
# elif b == 3:
#     c = "Tesoura"
# if c == a:
#     print("Empate")
# elif c == "Pedra" and a == "Papel":
#     print(f"{c} perde para {a}")
# elif c == "Papel" and a == "Tesoura":
#     print(f"{c} perde para {a}")
# elif c == "Tesoura" and a == "Pedra":
#     print(f"{c} perde para {a}")
# elif c == "Pedra" and a == "Tesoura":
#     print(f"{c} ganha de {a}")
# elif c == "Papel" and a == "Pedra":
#     print(f"{c} ganha de {a}")
# elif c == "Tesoura" and a == "Papel":
#     print(f"{c} ganha de {a}")
# print("Tenha um bom dia")
from random import randint

itens = ["Pedra", "Papel", "Tesoura"]
pc = randint(0, 2)
# print(f"O computador escolheu {itens[pc]}")
print(
    """Suas opcoes:
{ 0 } Pedra
{ 1 } Papel
{ 2 } Tesoura"""
)
j = int(input("Qual a sua escolha?"))
print("-=" * 20)
if j <= 2:
    print(f"O Computador jogou {itens[pc]}")
    print(f"Voce jogou {itens[j]}")
else:
    print("Erro")
print("-=" * 20)
if pc == 0 and j <= 2:  # jogou pedra
    if pc == j:
        print("Deu EMPATE")
    elif j == 1:
        print("Voce VENCEU")
    else:
        print("Voce PERDEU")
elif pc == 1 and j <= 2:  # jogou papel
    if pc == j:
        print("Deu EMPATE")
    elif j == 2:
        print("Voce VENCEU")
    else:
        print("Voce PERDEU")
elif pc == 2 and j <= 2:  # jogou tesoura
    if pc == j:
        print("Deu EMPATE")
    elif j == 0:
        print("Voce VENCEU")
    else:
        print("Voce PERDEU")
else:
    print("Nao existe essa opcao")
