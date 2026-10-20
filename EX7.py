numeroSecreto = int(input("Digite o número secreto: "))

tentativas = 0

while True:
    numero = int(input("Tente adivinhar o número secreto: "))
    tentativas += 1
    if numero == numeroSecreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas")
        break
    elif numero < numeroSecreto:
        print("O número secreto é maior!")
    else:
        print("O número secreto é menor!")