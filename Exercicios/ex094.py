dado = {}
pessoa = []
mulheres = []
maiores = []
a = cont = soma = 0

while True:
    dado["nome"] = str(input("Nome:"))
    while True:
        a = str(input("Sexo: [M/F]")).strip().upper()[0]
        if a in "MF":
            dado["sexo"] = a
            break
        print("ERRO!! Dijite apenas M ou F")
    while True:
        a = input("Idade:")
        if a.isdigit():
            a = int(a)
            soma += a
            dado["idade"] = a
            break
    pessoa.append(dado.copy())
    a = str(input("QUER CONTINUAR:[S/N]")).strip().upper()[0]
    if a in "N":
        break
    elif a not in "SN":
        print("ERRO!! Dijite apenas S ou N")
print("=-=" * 20)
med = int(soma / len(pessoa))
print(f"Foram cadastrados {len(pessoa)} pessoas")
print(f"A media da idade do grupo e {med}")
for a in pessoa:
    if a["sexo"] in "F":
        mulheres.append(a["nome"])
    if a["idade"] > med:
        maiores.append(a["nome"])
print(f"A lista de mulheres cadastradas: {mulheres}")
print(f"A lista com as pessoas com a idade acima da media e: {maiores}")
print("=-=" * 20)
