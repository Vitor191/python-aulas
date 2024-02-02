from random import randint

#
# n = a = r = b = c = p = 0
# print(
#     "=-=" * 10,
# )
# print("VAMOS JOGAR PAR OU IMPAR")
# print(
#     "=-=" * 10,
# )
# while True:
#     r = randint(0, 10)
#     n = input("Digite um numero:")
#     if n.isnumeric() == False:
#         while True:
#             n = input("Voce digitou errado.\nDigite um numero:")
#             if n.isnumeric():
#                 break
#     n = int(n)
#     b = (n + r) % 2
#     if b == 1:
#         p = "Impar"
#     elif b == 0:
#         p = "Par"
#     a = str(input("Voce quer Par ou Impar? [P/I]").strip().upper()[0])
#     if a != "P" and a != "I":
#         while True:
#             a = str(
#                 input("Voce digitou errado.Voce quer Par ou Impar? [P/I]")
#                 .strip()
#                 .upper()[0]
#             )
#             if a == "P" or a == "I":
#                 break
#     print(f"Voce jogou {n} e o computador jogou {r} o total deu {n+r}, e {n+r} e {p}")
#     print(
#         "=-=" * 10,
#     )
#     if a == "P" and b == 0:
#         print("Voce ganhou. Vamos jogar denovo")
#         c += 1
#         print(
#             "=-=" * 10,
#         )
#     elif a == "I" and b == 1:
#         print("Voce ganhou. Vamos jogar denovo")
#         c += 1
#         print(
#             "=-=" * 10,
#         )
#     else:
#         print("Voce Perdeu.")
#         break
# print(
#     "=-=" * 10,
# )
# print(f"GAME OVER!Voce ganhou {c} Vezes")
v = 0
while True:
    jogador = input("Diga um valor:")
    if jogador.isdigit():
        jogador = int(jogador)
        computador = randint(0, 10)
        total = jogador + computador
        tipo = " "
        while tipo not in "PI":
            tipo = str(input("Par ou Impar? ")).strip().upper()[0]
        print(
            f"Voce jogou {jogador} e o computador jogou {computador}. Total de {total}"
        )
        if tipo == "P":
            if total % 2 == 0:
                print("Voce VENCEU")
                v += 1
            else:
                print("Voce PERDEU")
                break
        elif tipo == "I":
            if total % 2 == 1:
                print("Voce VENCEU")
                v += 1
            else:
                print("Voce PERDEU")
                break
        print("Vamos jogar novamente...")
    else:
        print("Valor invalido. Digite novamente")
print(f"GAME OVER! Voce venceu {v} vezes.")
