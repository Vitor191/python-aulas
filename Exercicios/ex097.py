def titulo(msg):
    # inicio = len(msg) + 2
    # for _ in range(inicio):
    #     print("~", end="")
    # print()
    # print(f"{msg:^{inicio}}")
    # for _ in range(inicio):
    #     print("~", end="")
    # print()
    tam = len(msg) + 2
    print("~" * tam)
    print(f"{msg:^{tam}}")
    print("~" * tam)


titulo(str(input("Digite o titulo:").strip().upper()))
