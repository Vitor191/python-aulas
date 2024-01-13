num = int(input("Digite um numero dentro de 0 a 9999:"))
num = num % 10000
m = num // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
u = num % 10
print(f"unidade:{u}\ndezena:{d}\ncentena:{c}\nmilhar:{m}")
