lista = []
continuar = True

def mostrar_lista(list: list):
    print(f"Lista: {list}")

def bubble_sort(list: list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

print("Menu de Comandos:")
print("Digite 'A' para adicionar um item ao último ìndice da lista.")
print("Digite 'V' para adicionar múltiplos itens à lista.")
print("Digite 'I' para adicionar um item em qualquer índice da lista.")
print("Digite 'P' para remover o último item da lista.")
print("Digite 'F' para remover o primeiro item da lista.")
print("Digite 'R' para remover um item específico da lista.")
print("Digite 'O' para organizar os itens da lista.")
print("Digite 'M' para mostrar os itens da lista.")
print("Digite 'S' para sair.")

while continuar:
    try:
        comando = input("Digite um comando: ").strip()
        if comando.lower() == 's':
            print("Encerrando...")
            continuar = False

        elif comando.lower() == 'a':
            numero = int(input("Digite um número para adicionar à lista: "))
            lista.append(numero)
            mostrar_lista(lista)

        elif comando.lower() == 'v':
            quantidade = int(input("Quantos itens deseja adicionar? \n"))
            if quantidade <= 0:
                print("A quantidade não pode ser menor ou igual a zero.")

            for i in range(quantidade):
                numero = int(input("Digite um número: "))
                lista.append(numero)

            mostrar_lista(lista)

        elif comando.lower() == 'i':
            numero = int(input("Digite um número para adicioná-lo à lista: "))
            indice = int(input("Digite o índice em que o índice deve ser inserido: "))
            lista.insert(indice, numero)
            mostrar_lista(lista)

        elif comando.lower() == 'p':
            item_removido = lista.pop()
            print(f"Item removido: {item_removido}")
            mostrar_lista(lista)

        elif comando.lower() == 'f':
            item_removido = lista.pop(0)
            print(f"Item removido: {item_removido}")
            mostrar_lista(lista)

        elif comando.lower() == 'r':
            mostrar_lista(lista)
            numero_remover = int(input("Qual número deseja remover? \n"))
            if numero_remover not in lista:
                raise ValueError("O número não está na lista.")
            
            item_removido = lista.remove(numero_remover)
            print(f"Item removido: {item_removido}")
            mostrar_lista(lista)
        
        elif comando.lower() == 'o':
            bubble_sort(lista)
            mostrar_lista(lista)

        elif comando.lower() == 'm':
            mostrar_lista(lista)

        else:
            print("O comando não existe. Tente novamente.")

    except ValueError as ve:
        print(f"Erro. {ve}")

    except IndexError:
        print("A lista está vazia.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado. {e}")