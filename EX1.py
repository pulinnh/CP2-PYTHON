
n = int(input("Digite a quantidade de numeros: "))

anterior = int(input("Digite o primeiro numero: "))
segmentos = 1

for i in range(n - 1):
    numero = int(input("Digite o proximo numero: "))

    if numero != anterior:
        segmentos += 1

    anterior = numero

print("O resultado é:", segmentos)
