a = float(input("Digite o primeiro lado do triangulo:"))
b = float(input("Digite o segundo lado do triangulo:"))
c = float(input("Digite o terceiro lado do triangulo:"))
if a + b > c and a + c > b and c + b > a:
    print("Com essas medidas podem format um triangulo", end="")
    if a == b and a == c and b == c:
        print(" Equilatero")
    elif a != b or a != c or b != c:
        print(" Escaleno")
    else:
        print("Isosceles")
else:
    print("Nao pode ser feito um triangulo")
print("Fim...")
