def notas(*n, sit=False):
    """
    →Situacao para adicionar notas para os alunos
    :param n:As notas a serem verificadas
    :param sit:Se voce quiser saber a situacao da media final
    :return:Retorna um dicionario com as informacoes →'total', 'maior', 'menor', 'media' e 'situacao'
    """
    d = {
        "total": len(n),
        "maior": max(n),
        "menor": min(n),
        "media": round((sum(n) / len(n)), 1),
    }
    if sit:
        if d["media"] >= 7:
            d["situacao"] = "BOA"
        elif 6 < d["media"] < 7:
            d["situacao"] = "RAZOAVEL"
        else:
            d["situacao"] = "RUIM"
    lista.append(d.copy())
    d.clear()
    return lista


lista = []
notas(7, 8, 10, 7, sit=True)
print(lista)
