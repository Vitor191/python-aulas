valor = float(input("Digite o valor do produto:"))
a = int(
    input(
        "Digite fim forma de pagamento:\n1-dinheiro.\n2-A vistano cartao.\n3-2x no cartao.\n4-3x ou mais no cartao.\n:"
    )
)
if a == 1:
    valor = valor * 0.90
    print("O valor fim ser pago com 10% de desconto e:", valor)
elif a == 2:
    valor = valor * 0.95
    print("O valor fim ser pago com 5% de desconto e:", valor)
elif a == 3:
    parcela = valor / 2
    print("O valor fim ser pago sera 2 parcelas ", valor)
elif a == 4:
    b = int(input("Digite quantas parcelas:"))
    parcela = (valor * 1.20) / b
    print(f"O valor fim ser pago sera {b}x{parcela:.2f}")
else:
    print("Nao existe essa forma de pagamento")
print("Tenha um bom dia!")
