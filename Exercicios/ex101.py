from datetime import datetime


def voto(nasc=0):
    if a < 16:
        return "NEGADO"
    elif 16 >= a < 18 or a >= 65:
        return "OPCIONAL"
    else:
        return "OBIGATORIO"


b = int(input("Em que ano voce nasceu:"))
atual = datetime
data = atual.today().year
a = data - b
print(f"Com {a} anos: VOTO {voto(a)} ")
