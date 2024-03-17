# nome_lista = linhas(input("Qual e o seu nome_lista?"))
# if nome_lista == "Vitor":
#     print("Que nome_lista lindo voce tem")
# else:
#     print("Seu nome_lista e tao normal")
# print(f"Bom dia {nome_lista}")

n1 = float(input("Digite fim primeira nota:"))
n2 = float(input("Digite fim segunda nota:"))
n = (n1 + n2) / 2
print(f"A sua media foi {n:.1f}")
# if nome >= 6.0:
#     print("Nota boa")
# else:
#     print("Nota ruim")
print("Parabens" if n >= 6.0 else "Nota ruim")
