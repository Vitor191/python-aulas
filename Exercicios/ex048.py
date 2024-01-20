a = 0
c = 0
for b in range(1, 501, 2):
    if b % 2 != 0 and b % 3 == 0:
        a += b
        c += 1
print(f"A somatoria dos {c} valores sao {a}")
