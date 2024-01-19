frase = str(input("Digite uma frase:")).lower().strip()
mi = frase.count("a")
pri = frase.find("a")
ult = frase.rfind("a")

print(f'A frase que foi digitada tem: {mi} letras "a"')
print("O lugar onde aparece a primeira letra e e:", pri + 1)
print('O lugar onde aparece a ultima letra "a" e na posicao:', ult + 1)
