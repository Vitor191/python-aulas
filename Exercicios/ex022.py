# meu exercicio
# frase = input("Digite o seu nome_lista: ")
# print("Onome todo em maiusculo fica:", frase.upper())
# print("O nome_lista todo em minusculo fica:", frase.lower())
# print("Caracteres sem contar os espacos e:", len(frase.replace(" ", "")))
# dividido = frase.split()
# print("O primeiro nome_lista tem", len(dividido[0]), "letras")

# Correcao do professor

nome = str(input("Digite seu nome_lista completo: "))
print("Analisando seu nome_lista...")
print("Seu nome_lista em maiusculo e {}".format(nome.upper()))
print("Seu nome_lista em minusculas e {}".format(nome.lower()))
print("Seu nome_lista tem {} letras".format(len(nome) - nome.count(" ")))
# print("Seu primeiro nome_lista tem {} letras".format(nome_lista.find(" ")))
separa = nome.split()
print(f"Seu primeiro nome_lista e {separa[0]} e ele possui {len(separa[0])} letras")
