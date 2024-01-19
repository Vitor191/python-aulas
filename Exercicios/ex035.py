a = float(input("Digite o primeiro lado do triangulo:"))
b = float(input("Digite o segundo lado do triangulo:"))
c = float(input("\033[;31mDigite o terceiro lado do triangulo:"))

if a + b > c and a + c > b and c + b > a:
    print("Pode ser feito um triangulo")
else:
    print("Nao pode ser feito um triangulo")
print("Fim...")
