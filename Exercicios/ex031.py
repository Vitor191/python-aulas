d = float(input("Digite a distancia do seu trajeto:"))
#
if d <= 200:
    print("Como a viagem e de ate 200km voce irar pagar {:0.2f} reais".format(d * 0.50))
else:
    print("Como a viagem foi maior que 200km voce irar pagar {:.2f}".format(d * 0.45))
