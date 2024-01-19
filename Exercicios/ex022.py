# meu exercicio
# frase = input("Digite o seu nome: ")
# print("Onome todo em maiusculo fica:", frase.upper())
# print("O nome todo em minusculo fica:", frase.lower())
# print("Caracteres sem contar os espacos e:", len(frase.replace(" ", "")))
# dividido = frase.split()
# print("O primeiro nome tem", len(dividido[0]), "letras")

# Correcao do professor

nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
print("Seu nome em maiusculo e {}".format(nome.upper()))
print("Seu nome em minusculas e {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
# print("Seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print(f"Seu primeiro nome e {separa[0]} e ele possui {len(separa[0])} letras")
