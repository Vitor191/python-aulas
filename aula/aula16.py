lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")

for cont in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posicao {cont}")
print("=" * 30)
for comida in lanche:
    print(f"Eu vou comer {comida}")
print("=" * 30)
for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")
print("\nComi pra caramba")
