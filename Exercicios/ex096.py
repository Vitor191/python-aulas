def area(alt, lar):
    a = alt * lar
    print(f"A area de um terreno de {alt}x{lar} e de {a:.1f}m²")


print(f'{"CONTROLE DE TERRENO":^10}')
print("=" * 20)
d = float(input("Digite a altura do seu terreno:"))
b = float(input("Digite a largura do seu terreno:"))
area(d, b)
