def ficha(nome, gols):
    if nome == "":
        nome = "<desconhecido>"
    if gols == "" or gols.isnumeric() is False:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato")


a = str(input("Nome do Jogador:"))
b = input("Numero de gols:")
ficha(a, b)
