peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC e {imc} e voce esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC e {imc} e voce esta no peso ideal")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC e {imc} e voce esta com sobrepeso")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC e {imc} e voce esta com obesidade")
elif imc >= 40:
    print(f"Seu IMC e {imc} e voce esta com obesidade morbida")
print("Tenha um bom dia")
