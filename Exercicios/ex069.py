i = s = ma = h = mu = c = 0
while True:
    while True:
        i = input("Digite a idade da pessoa:")
        if i.isnumeric():
            i = int(i)
            if i > 18:
                ma += 1
            break
        else:
            print("Você digitou errado. Digite a idade novamente.")
    while True:
        s = str(input("Digite o sexo da pessoa cadastrada {M/F]:").strip().upper()[0])
        if s == "M" or s == "F":
            if s == "M":
                h += 1
            if s == "F" and i < 20:
                mu += 1
            break
        else:
            print("Você digitou errado. Digite o sexo novamente [M/F]:")
    while True:
        c = str(input("Voce deseja continuar?{S/N]").upper())
        if c == "S" or c == "N":
            break

        else:
            print("Você digitou errado. Digite novamente [S/N]:")
    if c == "N":
        break
print(
    f"Nas pessoas cadastradas,{ma} sao maiores de 18 anos,possuem {h} homens cadastrados e {mu} mulheres abaixo de 20 anos"
)
