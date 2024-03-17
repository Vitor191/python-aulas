# from random import randint
# from time import sleep
#
# dic = {}
# jogador = []
# ordem = []
# print("Valores sorteados")
# for passo in range(4):
#     valor = randint(1, 6)
#     dic = {"dado": valor}
#     print(f"O jogador{passo+1} tirou {valor}")
#     jogador.append(dic)
#     sleep(1)
# print("=-=" * 10)
# for inicio in jogador:
#     ordem.append(inicio["dado"])
#     ordem.sort(reverse=True)
# jogador_copia = jogador.copy()
# for inicio, fim in enumerate(ordem):
#     for passo, d in enumerate(jogador_copia):
#         if d["dado"] == fim:
#             print(f"O {inicio+1} lugar ficou com o jogador{passo+1} que tirou {fim}")
#             d["dado"] = 0
#             sleep(1)
#             break

from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}
ranking = list()
print("Valores sorteados")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("=-=" * 15)
for k, v in enumerate(ranking):
    print(f"{k+1} lugar: {v[0]} com {v[1]}.")
    sleep(1)
