n = int(input("Quantos produtos serão reajustados? "))

maior_diferenca = 0
maior_percentual = 0

for i in range(n):
    produto = input("Digite o nome do produto: ")
    preco_atual = float(input("Digite o preço do produto atual: "))
    preco_novo = float(input("Digite o valor do preço reajustado: "))
    diferenca = preco_novo - preco_atual
    percentual = (diferenca / preco_atual) * 100

    if diferenca > maior_diferenca:
        maior_diferenca = diferenca
        produto_maior_diferenca = i + 1

    if percentual > maior_percentual:
        maior_percentual = percentual
        produto_maior_percentual = i + 1   

print(f"O produto com maior diferença de preço é o produto {produto_maior_diferenca} com uma diferença de R${maior_diferenca:.2f}.")
print(f"O produto com maior percentual de reajuste é o produto {produto_maior_percentual} com um percentual de {maior_percentual:.2f}%.")
