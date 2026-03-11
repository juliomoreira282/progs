inventario = ["Oxigênio", "Ração", "Antena", "Combustível", "Trajes Espaciais"]

print(inventario[2])

print(f"Houve um problema com o item {inventario[-1]}!")

item_removido = inventario.pop()

print(f"O item {item_removido} foi descartado.")

print("A integridade estrutural está comprometida. Adicione um kit de reparo na primeira posição com urgência.")

# Console

item = input("Digite para adicionar um item: ")

inventario.insert(0, item)

print(f"O item {item} foi adicionado.")

for item in inventario:
    if "Combustível" not in inventario:
        print("Falha crítica do motor. Sem combustível.")
    
    if item == "Combustível":
        print(f"{item} encontrado na posição {inventario.index(item)}!")

while True:
    for i, item in enumerate(inventario):
        print(f"{i}. {item}")

    comando = input("Digite para adicionar um outro item: Digite (S) para Substituir | Digite (X) para encerrar: ")
    if comando.upper() == 'X':
        print("Encerrando...")
        break
    
    elif comando.upper() == 'S':    
        sub_item = input("Digite o item para colocar no lugar de algum outro: ")
        indice = int(input("Digite o índice o item a ser substituído: "))
        inventario[indice] = sub_item.capitalize()

    else:    
        novo_item = comando.capitalize()
        inventario.append(novo_item)