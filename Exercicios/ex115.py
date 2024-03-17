from exercicio115.lib import interface

arq = "arquivo.txt"
interface.criar(arq)


while True:
    resp = interface.menu(
        ["Ver pessoa cadastrada", "Cadastrar nova Pessoas", "Sair do sistema"]
    )
    if resp == 1:
        interface.vercadastro(arq)
    elif resp == 2:
        interface.cadastrar(arq)
    elif resp == 3:
        break


print("tchau")
