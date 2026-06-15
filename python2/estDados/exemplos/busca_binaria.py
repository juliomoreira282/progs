def busca_binaria(lista_ordenada: list, item_procurado):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = inicio + fim // 2
        chute = lista_ordenada[meio]
        if chute == item_procurado:
            return f"Achei na posição {meio}!"
        
        if chute > item_procurado:
            fim = meio - 1

        else:
            inicio = meio + 1

    return "Não está na lista."

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(busca_binaria(numeros, 40))