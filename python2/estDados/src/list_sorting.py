my_list = []
swapped = True
num = int(input("Quantos elementos deseja embaralhar? "))

for i in range(num):
    val = float(input("Entre com a lista de elementos: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)