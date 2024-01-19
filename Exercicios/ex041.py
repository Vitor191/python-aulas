from datetime import datetime

atual = datetime.now()
ano = int(input("informe o ano que voce nasceu:"))
idade = atual.year - ano
if idade < 9:
    print(f"Voce tem {idade} e voce e da categoria Mirim")
elif idade < 14:
    print(f"Voce tem {idade} e voce e da categoria Infantil")
elif idade < 19:
    print(f"Voce tem {idade} e voce e da categoria Junior")
elif idade < 20:
    print(f"Voce tem {idade} e voce e da categoria Senior")
elif idade > 20:
    print(f"Voce tem {idade} e voce e da categoria Master")
print("Boa tarde")
