frase = input("Digite uma frase:")
min = frase.lower().count("a")
pri = frase.find("a")
ult = frase.rfind("a")

print(f'A frase que foi digitada tem:{min} letras "a"')
print("O lugar onde aparece a primeira letra e e:", pri)
print('O lugar onde aparece a ultima letra "a" e na posicao:', ult)
