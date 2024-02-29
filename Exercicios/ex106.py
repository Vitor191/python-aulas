from time import sleep

c = (
    "\033[0m",  # 0 sem cor
    "\033[91m",  # 1 cor vermelha
    "\033[92m",  # 2 cor verde
    "\033[93m",  # 3 cor amarela
    "\033[94m",  # 4 cor azul
    "\033[95m",  # 5 cor roxa
    "\033[96m",  # 6 cor ciano
)


def ajuda(com):
    titulo(f"Acessando o manual de comando '{com}'", 3)
    help(com)
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("=" * tam)
    print(f"  {msg}")
    print("=" * tam)
    print(c[0], end="")
    sleep(1)


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Funcao ou Biblioteca >"))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATE LOGO", 1)
