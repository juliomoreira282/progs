lista_cenario_a = []
lista_cenario_b = []
lista_cooperados = []

def bubble_sort(list: list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

def selection_sort(list: list):
    n = len(list)
    for i in range(n):
        idx_menor = i
        for j in range(i + 1, n):
            if list[j] < list[idx_menor]:
                idx_menor = j

        list[i], list[idx_menor] = list[idx_menor], list[i]

def merge_sort(list: list):
    if len(list) <= 1:
        return list
    
    meio = len(list) // 2
    esq = merge_sort(list[:meio])
    dir = merge_sort(list[meio:])
    return merge(esq, dir)

def merge(esq, dir):
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]: resultado.append(esq[i]); i += 1
        else: resultado.append(dir[j]); j += 1

    return resultado + esq[i:] + dir[j]

def busca_linear(lista: list, item_procurado):
    for idx, elemento in enumerate(lista):
        if elemento == item_procurado:
            return f"Encontrei na posição {idx}"
        
    return "Não encontrei."

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

