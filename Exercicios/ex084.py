pessoa = []
pessoa_pesada = []
pessoa_leve = []
dado = []
mai = men = b = 0
while True:
    dado.append(str(input("Nome:")))
    while True:
        peso = input("Peso")
        if peso.isdigit():
            peso = int(peso)
            dado.append(peso)
            if peso < men or b == 0:
                men = peso
            if peso > mai or b == 0:
                mai = peso
                b = 1
            break
    pessoa.append(dado[:])
    dado.clear()
    a = str(input("Deseja continuar?[S/N]"))
    if a in "Nn":
        break
for a in pessoa:
    if a[1] == mai:
        pessoa_pesada.append(a[0])
    elif a[1] == men:
        pessoa_leve.append(a[0])
print("=-=" * 20)
print(f"Foram cadastradas {len(pessoa)} pessoas")
print(f"As pessoas mais pesadas pesando {mai}Kg sao {pessoa_pesada}")
print(f"As pessoas mais leves pesando {men}Kg sao {pessoa_leve}")
