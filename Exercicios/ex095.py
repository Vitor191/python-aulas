dado = {}
jogador = []
gols = []
while True:
    dado["nome"] = str(input("Nome do dado:"))
    a = int(input(f"Quantas partidas {dado['nome']} jogou:"))
    for b in range(a):
        gols.append(int(input(f"Na partida {b+1} o {dado["nome"]} fez quntos gols:")))
    dado['gols'] = gols[:]
    dado['total'] = sum(dado['gols'])
    jogador.append(dado.copy())
    gols.clear()
    a = str(input('Quer continuar?[S/N]'))
    if a in 'Nn':
        break
print('=-='*18)
print('COD ', end='')
for i in dado.keys():
    print(f'{i:<15}', end='')
# print(f'{'Nº': <5}{'Nome': <10}{'Gols':>10}{'Total': >15}')
print()
print('=-='*18)
b = 1
# for a in jogador:
#     gols_str = ', '.join(map(str, a['gols']))
#     print(f"{b: <5}{a['nome']: <15}{gols_str: <10}{a['total']: >10}")
#     b += 1
for k, v in enumerate(jogador):
    print(f'{k+1:>2}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    while True:
        a = input('Mostra dados de qual jogador? ')
        if a.isdigit():
            a = int(a)
            break
    if 0 < a <= len(jogador):
        a -= 1
        b = 0
        print('--'*18)
        print(f'Levantando dados do jogador {jogador[a]['nome']}')
        for b in range(len(jogador[a]['gols'])):
            print(f'  →No jogo {b+1} ele fez {jogador[a]['gols'][b]} ')
    else:
        print('Esse jogador nao existe')
    print('--'*20)
    b = str(input('Deseja continuar?[S/N]'))
    if b in 'Nn':
        break
print('Fim')
