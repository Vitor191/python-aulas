def leiaint(msg):
    global a, b
    while True:
        try:
            a = int(input("Digite um numero inteiro:"))
            break
        except (ValueError, TypeError):
            print("\033[91mERRO!! Você acabou de digitar um número inválido\033[0m")
    while True:
        try:
            b = float(input("Digite um numero real:"))
            break
        except (ValueError, TypeError):
            print("\033[91mERRO!! Você acabou de digitar um número inválido\033[0m")
        # except KeyboardInterrupt:
        #     print("O usuario decidiu encerrar o programa")
    print(f"o valor inteiro digitado foi {a} e o real foi {b}")


a = b = 0
try:
    n = leiaint("Digite um numero inteiro:")
except KeyboardInterrupt:
    print("\033[91m\nO usuario decidiu encerrar o programa\033[0m")
    print(f"O valor inteiro digitado foi {a} e o real foi {b}")
