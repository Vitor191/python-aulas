nome_produ = preco_produ = preco_total = produ_bara = a = nome_bara = b = 0
while True:
    nome_produ = str(input("Nome do pruduto:"))
    preco_produ = int(input("Preco:"))
    preco_total += preco_produ
    if produ_bara == 0 or produ_bara > preco_produ:
        produ_bara = preco_produ
        nome_bara = nome_produ
    elif preco_produ > 1000:
        a += 1
    while True:
        b = str(input("Deseja continuar[S/N]?").upper())
        if b == "S" or b == "N":
            break
    if b == "N":
        break
print("FIM DO PROGRAMA".center(21, "-"))
print(f"Foram gastos um total de {preco_total} reais.")
print(f"Um total de {a} itens custam mais que 1000 reias")
print(f"O nome do produto mais barato e :{nome_bara} custando R${produ_bara}")
