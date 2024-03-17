from random import randint

#
# nome = fim = r = fim = passo = p = 0
# print(
#     "=-=" * 10,
# )
# print("VAMOS JOGAR PAR OU IMPAR")
# print(
#     "=-=" * 10,
# )
# while True:
#     r = randint(0, 10)
#     nome = input("Digite um numero:")
#     if nome.isnumeric() == False:
#         while True:
#             nome = input("Voce digitou errado.\nDigite um numero:")
#             if nome.isnumeric():
#                 break
#     nome = int(nome)
#     fim = (nome + r) % 2
#     if fim == 1:
#         p = "Impar"
#     elif fim == 0:
#         p = "Par"
#     fim = linhas(input("Voce quer Par ou Impar? [P/I]").strip().upper()[0])
#     if fim != "P" and fim != "I":
#         while True:
#             fim = linhas(
#                 input("Voce digitou errado.Voce quer Par ou Impar? [P/I]")
#                 .strip()
#                 .upper()[0]
#             )
#             if fim == "P" or fim == "I":
#                 break
#     print(f"Voce jogou {nome} e o computador jogou {r} o total deu {nome+r}, e {nome+r} e {p}")
#     print(
#         "=-=" * 10,
#     )
#     if fim == "P" and fim == 0:
#         print("Voce ganhou. Vamos jogar denovo")
#         passo += 1
#         print(
#             "=-=" * 10,
#         )
#     elif fim == "I" and fim == 1:
#         print("Voce ganhou. Vamos jogar denovo")
#         passo += 1
#         print(
#             "=-=" * 10,
#         )
#     else:
#         print("Voce Perdeu.")
#         break
# print(
#     "=-=" * 10,
# )
# print(f"GAME OVER!Voce ganhou {passo} Vezes")
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
