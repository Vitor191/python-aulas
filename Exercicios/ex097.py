def titulo(msg):
    a = len(msg) + 2
    for _ in range(a):
        print("~", end="")
    print()
    print(f"{msg:^{a}}")
    for _ in range(a):
        print("~", end="")
    print()


m = str(input("Digite o titulo:").strip().upper())
titulo(m)
