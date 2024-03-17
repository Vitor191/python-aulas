def voto(nasc=0):
    from datetime import date

    global a, b
    atual = date.today().year
    a = atual - nasc

    if a < 16:
        b = "NAO VOTA"
    elif 16 >= a < 18 or a >= 65:
        b = "VOTO OPCIONAL"

    else:
        b = "VOTO OBIGATORIO"


a = b = 0
voto(int(input("Em que ano voce nasceu:")))
print(f"Com {a} anos : {b}")
