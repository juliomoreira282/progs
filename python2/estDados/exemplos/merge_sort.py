def merge_sort(list):
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

    return resultado + esq[i:] + dir[j:]

notas = [4, 8, 6, 3, 7, 10, 2]
print(merge_sort(notas)) 