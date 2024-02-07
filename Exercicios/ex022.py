# meu exercicio
# frase = input("Digite o seu nome_lista: ")
# print("Onome todo em maiusculo fica:", frase.upper())
# print("O nome_lista todo em minusculo fica:", frase.lower())
# print("Caracteres sem contar os espacos e:", len(frase.replace(" ", "")))
# dividido = frase.split()
# print("O primeiro nome_lista tem", len(dividido[0]), "letras")

# Correcao do professor

nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome...")
print("Seu nome em maiusculo e {}".format(nome.upper()))
print("Seu nome em minusculas e {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome_lista tem {} letras".format(nome.find(" ")))
separa = nome.split()
primeiro_nome = separa[0]
print(f"Seu primeiro nome e {separa[0]} e ele possui {len(separa[0])} letras")
for a in primeiro_nome:
    print(a)
