
texto = input("Digite uma palavra ou frase: ")

# ele vai armazenar um texto vazio
invertido = ""

# O for vai percorrer o texto todo de tras pra frente
for i in range(len(texto) - 1, -1, -1):
    invertido += texto[i]
print()
# Mostra o texto/String já invertida
print("O texto invertido é:", invertido)
