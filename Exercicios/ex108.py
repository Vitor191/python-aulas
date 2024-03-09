from exercicio108 import moeda

a = float(input("Digite o preco: R$"))

print(f"A metade de {moeda.moeda(a)} e {moeda.moeda(moeda.metade(a))}")
print(f"O dobro de {moeda.moeda(a)} e {moeda.moeda(moeda.dobro(a))}")
print(f"Aumentado em 10%, temos {moeda.moeda(moeda.aumentar(a, 10))}")
