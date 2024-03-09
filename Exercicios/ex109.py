from exercicio109 import moeda

a = float(input("Digite o preco: R$"))

print(f"A metade de {moeda.moeda(a)} e {moeda.metade(a, True)}")
print(f"O dobro de {moeda.moeda(a)} e {moeda.dobro(a, True)}")
print(f"Aumentado em 10%, temos {moeda.aumentar(a, 10, True)}")
print(f"Reduzindo em 13%, temos {moeda.diminuir(a, 13, True)}")
