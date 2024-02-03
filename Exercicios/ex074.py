from random import randint

lista = tuple(randint(0, 1000) for _ in range(5))
print("Os cinco itens sorteados sao:", lista)
menor = 0
maior = 0
for i in range(0, 5):
    if i == 0 or menor > lista[i]:
        menor = lista[i]
    if i == 0 or maior < lista[i]:
        maior = lista[i]
print(f"O menor numero sorteado e :{menor}")
print(f"O maior numero sorteado e :{maior}")
