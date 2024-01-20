nome = input("Digite o nome_lista de uma cidade:")

nome2 = nome.split()

print(
    'O nome_lista da cidade que foi digitado comeca com "santos"?',
    "santos" in nome2[0].lower(),
)
