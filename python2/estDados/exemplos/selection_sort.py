def selection_sort(list):
    n = len(list)
    for i in range(n):
        idx_menor = i
        for j in range(i + 1, n):
            if list[j] < list[idx_menor]:
                idx_menor = j

        list[i], list[idx_menor] = list[idx_menor], list[i]

    return list

notas = [7, 6, 4, 1, 10, 8, 9]
print(selection_sort(notas))