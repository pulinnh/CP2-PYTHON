# Pede ao usuário para digitar o número que será o "segredo" a ser adivinhado
numeroSecreto = int(input("Digite o número secreto: "))

# Contador de tentativas, começa zerado
tentativas = 0

# Loop infinito: só é interrompido quando o número é acertado (break)
while True:
    # Pede um palpite para tentar adivinhar o número secreto
    numero = int(input("Tente adivinhar o número secreto: "))

    # A cada palpite, soma 1 à contagem de tentativas
    tentativas += 1

    if numero == numeroSecreto:
        # Acertou: mostra quantas tentativas foram necessárias e encerra o loop
        print(f"Parabéns! Você acertou em {tentativas} tentativas")
        break
    elif numero < numeroSecreto:
        # Palpite menor que o número secreto: dá a dica de que o número é maior
        print("O número secreto é maior!")
    else:
        # Palpite maior que o número secreto: dá a dica de que o número é menor
        print("O número secreto é menor!")
