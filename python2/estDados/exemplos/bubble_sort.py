def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

notas = [5, 8, 4, 7, 10, 9, 2]
print(bubble_sort(notas))