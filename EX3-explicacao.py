# Valor da cédula que será trocada por moedas
cedula = int(input("Digite o valor da cédula: "))
# Valor de cada uma das duas moedas disponíveis para a troca
moeda_a = int(input("Digite o valor de uma moeda: "))
moeda_b = int(input("Digite o valor da outra moeda: "))

# Controla se alguma combinação de moedas que soma o valor da cédula foi encontrada
encontrou = False

# Testa cada quantidade possível de moeda_a, de 0 até o máximo que cabe na cédula
for qtd_a in range(cedula // moeda_a + 1):
    # Quanto ainda falta completar depois de usar "qtd_a" moedas do tipo A
    resto = cedula - (moeda_a * qtd_a)
    # Só é uma combinação válida se o resto for divisível exatamente por moeda_b
    if resto % moeda_b == 0:
        qtd_b = resto // moeda_b
        print(f"Possível: {qtd_a} moeda(s) de {moeda_a} e {qtd_b} moeda(s) de {moeda_b}")
        encontrou = True
        # Para no primeiro resultado válido, não precisa testar as demais quantidades
        break

# Se o loop terminou sem achar nenhuma combinação exata, avisa que não é possível trocar
if not encontrou:
    print("Não é possível fazer a troca")