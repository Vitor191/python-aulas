a = str(input("Digite a frase").lower().replace(" ", ""))
print(a)
b = a[::-1]
if a == b:
    print("Essa frase e um Polindromo")
else:
    print("Essa frase nao e um Polindromo")
