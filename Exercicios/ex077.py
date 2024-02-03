palavras = (
    "aula",
    "aprender",
    "cachorro",
    "gato",
    "computador",
    "telefone",
    "teclado",
    "programacao",
    "python",
    "escola",
    "bicicleta",
    "janela",
    "papel",
    "caneta",
    "mesa",
    "cadeira",
    "lampada",
    "porta",
    "livro",
    "musica",
    "carro",
    "cidade",
)
print("As palavras sao:")
print("=" * 30)
# for a in range(len(palavras)):
for a in palavras:
    print(f"\nNa palavra {a.upper()} tem as vogais: ", end="")
    for b in a:
        if b.lower() in "aeiou":
            print(b, end=" ")
print("\n")
print("=" * 30)
print("Fim".center(30, " "))
