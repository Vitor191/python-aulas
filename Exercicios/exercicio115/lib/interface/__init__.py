from vitor.utilidadesVitor import linhas


def sistema(a=0):
    linhas.titulo("menu Principal")
    print("\033[92m1\033[0m - \033[94mVer pessoas cadastradas")
    print("\033[92m2\033[0m - \033[94mCadastrar novas pessoas")
    print("\033[92m3\033[0m - \033[94mSair do sistema\033[0m")
    print("-" * 34)
    while True:
        try:
            a = int(input("\033[92mSua opcao:\033[m"))
            if 1 <= a <= 3:
                break
            else:
                print("\033[91mERRo:por favor, digite um numero inteiro valido\033[0m")
        except (ValueError, TypeError):
            print("\033[91mERRo:por favor, digite um numero inteiro valido\033[0m")
    if a == 1:
        vercadastro(1)
    elif a == 2:
        cadastrar(1)
    else:
        linhas.titulo("Saindo do sistema... ate logo")


def vercadastro(a=0):
    linhas.titulo("opcao 1")


def cadastrar(a=0):
    linhas.titulo("opcao 2")
