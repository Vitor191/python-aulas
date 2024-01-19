nome = str(input("Qual o seu nome?"))

if nome == "gustavo":
    print("Que nome bonito")
elif nome == "paulo" or "maria":
    print("Seu nome e bem popular")
elif nome == "ana":
    print("que nome feminino")
else:
    print("Seu nome e bem normal")
print(f"Tenha um bom dia {nome}")
