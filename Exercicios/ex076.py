lista = (
    "Lapis",
    2.00,
    "Bolsa",
    40.00,
    "Caderno",
    15.50,
    "Caneta",
    1.50,
    "Livro",
    25.00,
    "Camiseta",
    20.00,
    "Calca",
    35.00,
    "Sapato",
    50.00,
    "Chinelo",
    10.00,
    "Relogio",
    30.00,
    "Celular",
    300.00,
    "Mouse",
    15.00,
)
print("=" * 40)
print("Listagem de Precos".center(40, " "))
print("=" * 40)
for a in range(0, len(lista), 2):
    print(f"{lista[a]:.<30}R${lista[a+1]: >8.2f}")
print("=" * 40)
print("Fim".center(40, " "))
