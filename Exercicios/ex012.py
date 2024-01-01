n = int(input("Qaul o preco do produto:"))
n1 = int(input("Qual o valor de desconto do produto:"))
n2 = 1 - (n1 * 10**-2)
nf = n * n2
print(f"O produto de valor {n} com desconto de {n1}% custara {nf:.3f}")
