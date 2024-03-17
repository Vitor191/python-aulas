lista = []
m = 0
while True:
    nome = str(input("Nome:"))
    nota1 = int(input("Primeira nota"))
    nota2 = int(input("Segunda nota:"))
    lista.append([nome, [nota1, nota2]])
    n = str(input("Voce deseja adicionar outro nome?[S/N]"))
    if n in "Nn":
        break
print(f'=-='*15)
print(f'{'nº': <5}{'Nome':<15}{'Media': >10}')
for a, i in enumerate(lista):
    m = (sum(lista[a][1])) / 2
    print(f"{a+1: <5}{i[0]: <15}{m:>10.2f}")
while True:
    while True:
        print(f'=-='*15)
        a = input('Qual aluno voce deseja saber fim media?(999 interrompe):')
        if a.isdigit():
            a = int(a)
            if 0 < a <= len(lista) or a == 999:
                break
            else:
                print('Esse aluno nao existe')
    if a == 999:
        break
    a -= 1
    print(f'Notas de {lista[a][0]} sao {lista[a][1]}')
print('Tchau')
