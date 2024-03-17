a = float(input("Digite fim sua primeira nota:"))
b = float(input("Digite fim sua segunda nota:"))
m = (a + b) / 2
if m < 5:
    print(f"Sua media e {m} voce esta reprovado")
elif m >= 5 and m < 7:
    print(f"Sua media e {m} voce esta de recuperacao")
elif m >= 7:
    print(f"Sua media e {m} voce esta aprovado")
