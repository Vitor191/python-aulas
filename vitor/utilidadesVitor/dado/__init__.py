from vitor.utilidadesVitor import linhas


def leiadinheiro(msg):
    """

    :param msg: Le uma str e verifica se e um valor valido para dinheiro
    :return: retorna dado float de um valor valido para dinheiro
    """
    valido = False
    while not valido:
        entrada = str(input(msg).replace(",", ".").strip())
        if entrada.isalpha() or entrada.strip() == "":
            linhas.titulo(f'ERRO: "{entrada}" e um preco invalido', 1)
        else:
            valido = True
            return float(entrada)
