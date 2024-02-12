num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print("Nao achei o numero 4")
print(num)
print(f"essa lista tem {len(num)} elementos")

# valores = []
# valores1 = valores[:]
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for _ in range(0, 5):
#     valores.append(int(input("Digite um valor:")))
#
# for c, v in enumerate(valores):
#     print(f"na posicao {c} encontrei o valor {v}!")
# print("Cheguei ao final da lista")
max = max(num)
print(num.index(max))
