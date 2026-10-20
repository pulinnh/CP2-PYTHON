# número que o jogador precisa adivinhar
numeroSecreto = 1
# contador de quantas vezes o jogador tentou
tentativas = 0

# while True cria um loop infinito, que só para quando encontrar um "break"
while True:
    # pede um número ao usuário e converte o texto digitado em inteiro
    numero = int(input("Digite um número de 1 a 10: "))
    # soma 1 a cada tentativa feita
    tentativas += 1
    if numero == numeroSecreto:
        # mensagens exibidas quando o jogador acerta
        print("Parabéns! Você acertou o número secreto!")
        print(f"Você acertou em {tentativas} tentativas.")
        # break interrompe o loop, pois o jogador já acertou
        break
    else:
        # mensagem exibida quando o jogador erra, e o loop continua
        print("Tente novamente! O número secreto é diferen1te.")
