s = input("Digite uma frase: ")

vogais = 0

for letra in s:
    if letra in "aeiouAEIOU":
        vogais += 1

print(f"Quantidade de vogais: {vogais}")