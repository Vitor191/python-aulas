peso = float(input("Digite o seu peso:"))
altura = float(input("Digite fim sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC e {imc} e voce esta abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"Seu IMC e {imc} e voce esta no peso ideal")
elif 25 <= imc < 30:
    print(f"Seu IMC e {imc} e voce esta com sobrepeso")
elif 30 <= imc < 40:
    print(f"Seu IMC e {imc} e voce esta com obesidade")
elif imc >= 40:
    print(f"Seu IMC e {imc} e voce esta com obesidade morbida")
print("Tenha um bom dia")
