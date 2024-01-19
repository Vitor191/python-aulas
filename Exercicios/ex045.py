from random import choice

lista = ["Pedra", "Papel", "Tesoura"]
a = choice(lista)
print(a)
b = int(input("Escolha:\n1 para Pedra.\n2 para Papel\n3 para Tesoura\n:"))

if b == 1:
    c = "Pedra"
elif b == 2:
    c = "Papel"
elif b == 3:
    c = "Tesoura"
if c == a:
    print("Empate")
elif c == "Pedra" and a == "Papel":
    print(f"{c} perde para {a}")
elif c == "Papel" and a == "Tesoura":
    print(f"{c} perde para {a}")
elif c == "Tesoura" and a == "Pedra":
    print(f"{c} perde para {a}")
elif c == "Pedra" and a == "Tesoura":
    print(f"{c} ganha de {a}")
elif c == "Papel" and a == "Pedra":
    print(f"{c} ganha de {a}")
elif c == "Tesoura" and a == "Papel":
    print(f"{c} ganha de {a}")
print("Tenha um bom dia")
