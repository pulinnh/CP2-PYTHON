numeroSecreto = 1

tentativas = 0

while True:
    numero = int(input("Tente adivinhar um número de 1 a 10: "))
    tentativas += 1
    if numero == numeroSecreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente.2")