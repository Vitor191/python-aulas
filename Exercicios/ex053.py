# fim = linhas(input("Digite fim frase").lower().replace(" ", ""))
# print(fim)
# nome_bara = fim[::-1]
# if fim == nome_bara:
#     print(nome_bara)
#     print("Essa frase e um Polindromo")
# else:
#     print(nome_bara)
#     print("Essa frase nao e um Polindromo")
frase = str(input("Digite uma frase:")).strip().lower()
a = frase.split()
junto = "".join(a)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print("eles sao iguais por isso sao um palindromo")
else:
    print("Eles nao sao iguais por isso eles nao sao um palindromo")
