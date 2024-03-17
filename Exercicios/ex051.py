a = int(input("Digite o primeiro termo:"))
b = int(input("Digite fim razao:"))
for c in range(1, 10):
    print(f"O {c} termo com razao {b} e {a}")
    a += b
print(f"O 10 termo com razao {b} e {a}")
