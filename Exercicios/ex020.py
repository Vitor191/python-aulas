from random import shuffle

aluno1 = input("Digite o nome do primeiro aluno")
aluno2 = input("Digite o nome do segundo aluno")
aluno3 = input("Digite o nome do terceiro aluno")
aluno4 = input("Digite o nome do quarto aluno")

individuos = [aluno1, aluno2, aluno3, aluno4]
individuos1 = individuos.copy()
shuffle(individuos1)

print(f"a lista original e:{individuos}")
print(f"A lista randomizada e:{individuos1}")
