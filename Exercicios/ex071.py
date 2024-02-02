# cin = vin = dez = um = 0
print("=" * 40)
print("BANCO CEV".center(40, " "))
print("=" * 40)
n = int(input("Qual valor voce deseja sacar? R$:"))
total = n
ced = 50
totced = 0
# while True:
#     if n >= 50:
#         cin = n / 50
#         n = n % 50
#     elif n >= 20:
#         vin = n / 20
#         n = n % 20
#     elif n >= 10:
#         dez = n / 10
#         n = n % 10
#     elif n < 10:
#         um = n
#         break
# print(f"Total de {int(cin)} cedulas de R$50")
# print(f"Total de {int(vin)} cedulas de R$20")
# print(f"Total de {int(dez)} cedulas de R$10")
# print(f"Total de {int(um)} cedulas de R$1")
# print("=" * 40)
# print("Volte sempre ao Banco CEV".center(40, " "))
# print("=" * 40)
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("=" * 40)
print("{:^40}".format("Volte sempre ao banco CEV"))
print("=" * 40)
