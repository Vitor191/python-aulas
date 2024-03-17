v = float(input("Digite fim velocidade do carro:"))

if v > 80:
    m = float(v - 80) * 7
    print(
        f"Voce excedeu o limite de velocidade de 80 km/h e tera que pagar uma multa de {m} reais"
    )
print("Dirija com seguranca")
