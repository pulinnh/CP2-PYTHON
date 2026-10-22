
n = int(input("Digite um numero inteiro positivo: "))

passos = 0

# Começa mostraando o numero inicial
print("Sequencia:")

while n != 1:

    print(n, end=" -> ")

    # Se for par, divido por 2
    if n % 2 == 0:
        n = n // 2
    else:
        # Se for impar, multiplico por 3 e soma 1
        n = 3 * n + 1

    # serve para contar cada vez que a regra fot aplicada
    passos += 1

print(n)
print()
print("Quantidade de passos:", passos)
