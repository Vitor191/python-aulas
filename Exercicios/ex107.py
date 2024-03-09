from exercicio107 import moeda

a = float(input("Digite o preco: R$"))

print(f"A metade de R${a:.2f} e R${moeda.metade(a):.2f}")
print(f"O dobro de R${a:.2f} e R${moeda.dobro(a):.2f}")
print(f"Aumentado em 10%, temos R${moeda.aumentar(a, 10):.2f}")
