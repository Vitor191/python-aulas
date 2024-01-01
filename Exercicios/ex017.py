import math
num1 = float(input('Fale o cateto oposto:'))
num2 = float(input('Fale o cateto adjacente'))
h = math.hypot(num1,num2)
print(f'A hipotenusa do cateto oposto {num1} e do cateto adjacente {num2} e igual a {h}')
