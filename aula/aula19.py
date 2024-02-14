# pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
# print(pessoas.items())
# del pessoas["sexo"]
# pessoas["nome"] = "Leandro"
# pessoas["peso"] = 98.5
# for k, v in pessoas.items():
#     print(f"{k} = {v}")
# brasil = []
# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "Sao Paulo", "sigla": "SP"}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[1]["sigla"])
estado = {}
brasil = []
for c in range(3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=" ")
    print()
