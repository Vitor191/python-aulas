s = int(input("Digite o seu salario:"))

if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print(f"O seu salario com o almento ficaria {s:0.2f} reais")
