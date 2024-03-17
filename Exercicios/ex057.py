# nome = ""
# while nome != "M" and nome != "F":
#     nome = linhas(input("Voce e Homem ou Mulher Digite [M/F]'\nome:")).upper()
#     if nome != "M" and nome != "F":
#         print("Voce digitou algo diferente de [M/F], Digite denovo.")
# print("fim")
sexo = str(input("Por favor informe seu sexo :[M/F]")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados incorretos.Por favor informe seu sexo:")).strip().upper()[0]
print(f"Seu sexo {sexo} foi cadastrado com sucesso!")
