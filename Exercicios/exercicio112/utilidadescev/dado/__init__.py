def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg).replace(",", ".").strip())
        if entrada.isalpha() or entrada.strip() == "":
            print(f"\033[91mERRO:'{entrada}' e um preco invalido\033[0m")
        else:
            valido = True
            return float(entrada)
