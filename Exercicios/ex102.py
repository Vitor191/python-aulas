def fatorial(n, show=False):
    """
    →Calcula a fatorial de n
    :param n:O valor a ser calculado
    :param show:Para mostrar a operacao
    :return: Retorna o resultado final
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f"{c}", end="")
            print(" x " if c > 1 else " = ", end="")
    return f


print(fatorial(5, True))
