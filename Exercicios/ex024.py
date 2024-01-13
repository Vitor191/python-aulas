nome = input("Digite o nome de uma cidade:")

nome2 = nome.split()

print(
    'O nome da cidade que foi digitado comeca com "santos"?',
    "santos" in nome2[0].lower(),
)
