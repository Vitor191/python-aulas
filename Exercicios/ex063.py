print("=-=" * 10)
print("Sequencia de Fibonati")
print("=-=" * 10)
n = int(input("Digite quantos termos voce quer ver:"))
g = 0
a = 1
b = 0
print(f"Os {n} primeiros termos sao")

while g < n:
    print(b, end="")
    print("." if g == n - 1 else " → ", end="")

    a = a + b
    b = a - b
    g += 1

print("\nTchau")
