from datetime import date

# a = int(input("Digite um ano e irei te falar se e um ano bissexto:"))
#
# if a % 100 == 0:
#     if a % 400 == 0:
#         print("ele e um ano bissexto")
#     else:
#         print("ele nao e bissexto")
# if a % 100 != 0:
#     if a % 4 == 0:
#         print("ele e um ano bissexto")
#     else:
#         print("ele nao e um ano bissexto")

ano = int(input("Digite o ano que voce quer verificar se e bissexto:"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} e bissexto")
else:
    print(f"O ano {ano} nao e bissexto")
