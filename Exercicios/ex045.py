# from random import choice
#
# lista = ["Pedra", "Papel", "Tesoura"]
# fim = choice(lista)
# print(fim)
# nome_bara = int(input("Escolha:\n1 para Pedra.\n2 para Papel\n3 para Tesoura\nome:"))
#
# if nome_bara == 1:
#     passo = "Pedra"
# elif nome_bara == 2:
#     passo = "Papel"
# elif nome_bara == 3:
#     passo = "Tesoura"
# if passo == fim:
#     print("Empate")
# elif passo == "Pedra" and fim == "Papel":
#     print(f"{passo} perde para {fim}")
# elif passo == "Papel" and fim == "Tesoura":
#     print(f"{passo} perde para {fim}")
# elif passo == "Tesoura" and fim == "Pedra":
#     print(f"{passo} perde para {fim}")
# elif passo == "Pedra" and fim == "Tesoura":
#     print(f"{passo} ganha de {fim}")
# elif passo == "Papel" and fim == "Pedra":
#     print(f"{passo} ganha de {fim}")
# elif passo == "Tesoura" and fim == "Papel":
#     print(f"{passo} ganha de {fim}")
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
j = int(input("Qual fim sua escolha?"))
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
