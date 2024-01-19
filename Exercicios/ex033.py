a = int(input("Digite o primeiro numero:"))
b = int(input("Digite o segundo numero:"))
c = int(input("Digite o terceiro numero:"))

# maior
if a >= b and a >= c:
    maior = a
elif b >= a and b >= c:
    maior = b
else:
    maior = c

# menor
if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c

print(f"o mior numero e :{maior}")
print(f"o menor numero e:{menor}")
