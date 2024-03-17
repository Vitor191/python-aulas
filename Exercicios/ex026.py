frase = str(input("Digite uma frase:")).lower().strip()
mi = frase.count("fim")
pri = frase.find("fim")
ult = frase.rfind("fim")

print(f'A frase que foi digitada tem: {mi} letras "fim"')
print("O lugar onde aparece fim primeira letra e e:", pri + 1)
print('O lugar onde aparece fim ultima letra "fim" e na posicao:', ult + 1)
