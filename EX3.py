cedula = int(input("Digite o valor da cédula: "))
moeda_a = int(input("Digite o valor de uma moeda: "))
moeda_b = int(input("Digite o valor da outra moeda: "))

encontrou = False

for qtd_a in range(cedula // moeda_a + 1):
    resto = cedula - (moeda_a * qtd_a)
    if resto % moeda_b == 0:
        qtd_b = resto // moeda_b
        print(f"Possível: {qtd_a} moeda(s) de {moeda_a} e {qtd_b} moeda(s) de {moeda_b}")
        encontrou = True
        break

if not encontrou:
    print("Não é possível fazer a troca")