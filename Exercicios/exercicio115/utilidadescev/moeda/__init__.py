def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * (taxa / 100))
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco, format=False):
    res = preco / 2
    return res if not format else moeda(res)


def moeda(preco=0, moe="R$"):
    return f"{moe}{preco:.2f}".replace(".", ",")


def resumo(preco=0, taxa=10, taxar=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"PRECO ANALISADO: \t{moeda(preco)}")
    print(f"Dobro do Preco: \t{dobro(preco, True)}")
    print(f"Metade do preco: \t{metade(preco, True)}")
    print(f"{taxa}% de aumento: \t{aumentar(preco, taxa, True)}")
    print(f"{taxar}% de reducao: \t{diminuir(preco, taxar, True)}")
    print("-" * 30)
