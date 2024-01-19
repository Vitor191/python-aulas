# nome = str(input("Qual e o seu nome?"))
# if nome == "Vitor":
#     print("Que nome lindo voce tem")
# else:
#     print("Seu nome e tao normal")
# print(f"Bom dia {nome}")

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
n = (n1 + n2) / 2
print(f"A sua media foi {n:.1f}")
# if n >= 6.0:
#     print("Nota boa")
# else:
#     print("Nota ruim")
print("Parabens" if n >= 6.0 else "Nota ruim")
