from datetime import datetime

atual = datetime.now()
ano = int(input("informe o ano que voce nasceu:"))
idade = atual.year - ano
if idade > 18:
    a = idade - 18
    print(f"Ja passou {a} anos do seu alistamento")
elif idade < 18:
    a = 18 - idade
    print(f"Ainda falta {a} anos da data de alistamento")
elif idade == 18:
    print("Voce esta no ano de alistamento")
print("Boa tarde")
