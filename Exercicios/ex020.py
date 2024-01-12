import random

aluno1 = input("Digite o nome do primeiro aluno")
aluno2 = input("Digite o nome do segundo aluno")
aluno3 = input("Digite o nome do terceiro aluno")
aluno4 = input("Digite o nome do quarto aluno")


individuos1 = [aluno1, aluno2, aluno3, aluno4]
individuos2 = individuos1.copy()
random.shuffle(individuos1)

print(f"a lista original e:{individuos2}")
print(f"A lista randomizada e:{individuos1}")