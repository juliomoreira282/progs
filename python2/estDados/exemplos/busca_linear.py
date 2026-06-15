def busca_linear(lista: list, item_procurado):
    for idx, elemento in enumerate(lista):
        if elemento == item_procurado:
            return f"Achei na posição {idx}!"
    
    return "Não encontrei."

mochila = ["caderno", "estojo", "caneta", "lanche"]
print(busca_linear(mochila, "caneta"))
print(busca_linear(mochila, "marca texto"))