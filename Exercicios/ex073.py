brasileirao = (
    "Palmeiras",
    "Gremio",
    "Atletico-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "Sao Paulo",
    "Cuiaba",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goias",
    "Coritiba",
    "America-MG",
)
print("=" * 20)
print("Os primeiros  colocados da tabela brasileira de 2023 sao:", brasileirao[0:5])
print("=" * 20)
print("Os ultimos 4 colocados da tabela brasileira de 2023 sao:", brasileirao[16:])
b = sorted(brasileirao)
print("=" * 20)
print("A tabela do brasileirao de 2023 na ordem alfabetica e:")

for a in range(0, len(brasileirao)):
    print(b[a])
print("=" * 20)
print("O Fluminense esta na {} posicao:".format(brasileirao.index("Fluminense") + 1))
