catalogo = {}

while True:
    tipo = input("Digite o tipo de item (ou 'sair' para encerrar): ")
    if tipo == 'sair': break
    
    preco = input(f"Digite o preço para {tipo}: ")
    estoque = input(f"Digite a quantidade em estoque para {tipo}: ")
    
    # Adicionando o dicionário aninhado
    catalogo[tipo] = {
        "preco": preco,
        "estoque": estoque
    }

print("\nCatálogo Final:")
print(catalogo)
