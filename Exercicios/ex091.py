from random import randint

dic = {}
jogador = []
ordem = []
print("Valores sorteados")
for c in range(4):
    valor = randint(1, 6)
    dic = {"dado": valor}
    print(f"O jogador{c+1} tirou {valor}")
    jogador.append(dic)
print("=-=" * 10)
for a in jogador:
    ordem.append(a["dado"])
    ordem.sort(reverse=True)
jogador_copia = jogador.copy()
for a, b in enumerate(ordem):
    for c, d in enumerate(jogador_copia):
        if d["dado"] == b:
            print(f"O {a+1} lugar ficou com o jogador{c+1} que tirou {b}")
            d["dado"] = 0
            break
