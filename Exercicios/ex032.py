from datetime import date

# fim = int(input("Digite um ano e irei te falar se e um ano bissexto:"))
#
# if fim % 100 == 0:
#     if fim % 400 == 0:
#         print("ele e um ano bissexto")
#     else:
#         print("ele nao e bissexto")
# if fim % 100 != 0:
#     if fim % 4 == 0:
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
