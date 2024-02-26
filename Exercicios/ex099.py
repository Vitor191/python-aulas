def maior(*list):
    print("Analisando os valores passados...")
    for a in list:
        print(a, end=" ")
    print(f"Foram informados {len(list)} numeros")
    print(f"O maior valor informado e {max(list)}")
    print()


maior(4, 5, 1, 2, 4, 8)
maior(4, 5, 9, 7, 7)
maior(0)
