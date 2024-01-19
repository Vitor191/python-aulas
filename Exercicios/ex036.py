print(
    "Para decidirmos se o emprestimo bancario pode ser aprovado o senhor tem que fornecer os seguintes dados:"
)
valor = float(input("Qual o valor da casa?"))
salario = float(input("Quanto voce recebe por mes?"))
anos = int(input("Quantos anos voce vai pagar a casa?"))

pres = anos * 12
v_pres = valor / pres

print(
    f"De acordo com os dados que o senhor informou irar ficar {pres} parcelas de {v_pres:.2f}"
)
if v_pres > salario * 0.30:
    print(
        "nao e possivel fazer o emprestimo pois o valor da parcela e maior que 30% do seu salario"
    )
elif v_pres < salario * 0.30:
    print(
        f"E possivel fazer o emprestimo pois o valor da parcela de {v_pres:.2f} nao ultrapassa 30% do seu salario"
    )
print("Tenha um bom dia!")
