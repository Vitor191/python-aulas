jogador = {}
gols = []

jogador["nome"] = str(input("Nome do jogador:"))
a = int(input(f"Quantas partidas {jogador['nome']} jogou:"))
for b in range(a):
    gols.append(int(input(f"Na partida {b+1} o dado {jogador["nome"]} fez quntos gols:")))
jogador['gols'] = gols[:]
jogador['total'] = sum(jogador['gols'])
print('=-='*15)
print(jogador)
print('=-='*15)
for k ,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('=-='*15)
print(f'O dado {jogador["nome"]} jogou {a} patidas')
for b in range(a):
    print(f'→ Na partida {b+1} o dado fez {jogador['gols'][b]} gols')
print(f'Foi um total de {jogador['total']} gols')