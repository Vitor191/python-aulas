numero = int(input("Digite o numero que sera convertido:"))
a = int(input("Digite:\n1-Binario.\n2-Octal.\n3-Hexa.\n"))

if a == 1:
    print(f"o numero {(numero)} em Binario fica {bin(numero)[2:]}")
elif a == 2:
    print(f"o numero {numero} em Octal fica {oct(numero)[2:]}")
elif a == 3:
    print(f"o numero {numero} em Hexadecimal fica {hex(numero)[2:]}")
elif a != 1 and a != 2 and a != 3:
    print("Essa opcao nao existe")
print("Tenha um bom dia")
