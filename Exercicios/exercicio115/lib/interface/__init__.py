from vitor.utilidadesVitor import linhas
import os


def leiaint(msg):
    while True:
        try:
            a = int(input(f"\033[92m{msg}\033[m").strip())
            if 1 <= a <= 3:
                return a
            else:
                print("\033[91mERRO!! Você acabou de digitar um número inválido\033[0m")
        except (ValueError, TypeError):
            print("\033[91mERRO!! Você acabou de digitar um número inválido\033[0m")


def vercadastro(msg):
    linhas.titulo("pessoas cadastradas")
    with open(msg, "r") as arquivo:
        for linha in arquivo:
            print(linha, end="")
        print("")


def cadastrar(msg):
    linhas.titulo("cadastrar novas pessoas")
    while True:
        a = str(input("Nome:"))
        while True:
            try:
                b = int(input("Idade:"))
            except (ValueError, TypeError):
                print("ERRO:Dados invalidos")
            else:
                with open(msg, "a") as arquivo:
                    arquivo.write(f"{a:<30}{b:>3} anos\n")
                print(f"Dados de {a} coletados com sucesso")
                break
        r = str(input("Deseja adicionar outra pessoa?[S/N]").upper())
        if r in "N":
            break


def menu(lista):
    linhas.titulo("menu principal")
    for a, b in enumerate(lista):
        print(f"\033[92m{a+1}\033[0m-\033[94m{b}\033[0m")
    linhas.linha("-", 42)
    resp = leiaint("Sua Opcao:")
    return resp


def criar(nome):
    arquivo_novo = nome

    if os.path.exists(arquivo_novo):
        print("Arquivo encontrado com sucesso")
    else:
        with open(arquivo_novo, "w") as arquivo:
            arquivo.write("Pessoas cadastradas:\n")
        print("Arquivo.txt criado com sucesso")
