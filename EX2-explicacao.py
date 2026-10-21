# Pede quantos produtos serão reajustados, para saber quantas vezes repetir o laço
n = int(input("Quantos produtos serão reajustados? "))

# Guarda a maior diferença de preço (em R$) encontrada até agora
maior_diferenca = 0
# Guarda o maior percentual de reajuste encontrado até agora
maior_percentual = 0

# Repete uma vez para cada produto informado
for i in range(n):
    produto = input("Digite o nome do produto: ")
    preco_atual = float(input("Digite o preço do produto atual: "))
    preco_novo = float(input("Digite o valor do preço reajustado: "))

    # Diferença em reais entre o preço novo e o preço atual
    diferenca = preco_novo - preco_atual

    # Percentual que essa diferença representa em relação ao preço atual
    percentual = (diferenca / preco_atual) * 100

    if diferenca > maior_diferenca:
        # Encontrou uma diferença maior que a registrada até agora: atualiza o recorde
        maior_diferenca = diferenca
        produto_maior_diferenca = i + 1  # +1 porque "i" começa em 0, mas queremos mostrar o nº do produto a partir de 1

    if percentual > maior_percentual:
        # Encontrou um percentual maior que o registrado até agora: atualiza o recorde
        maior_percentual = percentual
        produto_maior_percentual = i + 1

# Ao final do loop, mostra qual produto teve a maior diferença de preço em reais
print(f"O produto com maior diferença de preço é o produto {produto_maior_diferenca} com uma diferença de R${maior_diferenca:.2f}.")

# E qual produto teve o maior percentual de reajuste
print(f"O produto com maior percentual de reajuste é o produto {produto_maior_percentual} com um percentual de {maior_percentual:.2f}%.")
