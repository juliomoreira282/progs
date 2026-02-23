nome = input("Digite um nome para inverter: ")
pilha_letras = []

for letra in nome:
    pilha_letras.append(letra)

nome_invertido = ""

while len(pilha_letras) > 0:
    letra_retirada = pilha_letras.pop()
    nome_invertido += letra_retirada

print(f"Nome Original: {nome}")
print(f"Nome Invertido: {nome_invertido.capitalize()}")