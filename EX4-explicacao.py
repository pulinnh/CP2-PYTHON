# Pede ao usuário para digitar uma frase, que será analisada
s = input("Digite uma frase: ")

# Contador de vogais, começa zerado
vogais = 0

# Percorre a frase caractere por caractere
for letra in s:
    # Verifica se a letra atual é uma vogal (maiúscula ou minúscula)
    if letra in "aeiouAEIOU":
        # Encontrou uma vogal: soma 1 ao contador
        vogais += 1

# Ao final do loop, mostra o total de vogais encontradas na frase
print(f"Quantidade de vogais: {vogais}")
