lista = []

def mostrar_lista(list: list):
    print(f"Lista: {list}")

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

print("Lista de Comandos:")
print("Digite 'A' para adicionar um item ao último índice da lista.")
print("Digite 'V' para adicionar múltiplos itens à lista.")
print("Digite 'I' para inserir um item em qualquer índice da lista.")
print("Digite 'P' para remover o último item da lista.")
print("Digite 'F' para remover o primeiro índice da lista.")
print("Digite 'R' para remover um item específico da lista.")
print("Digite 'O' para organizar os itens da lista.")
print("Digite 'M' para mostrar os itens")
print("Digite 'S' para sair.")

while True:
    try:    
        comando = input("Digite um comando: ").strip()
        if comando.lower() == 's':
            print("Encerrando...")
            break

        elif comando.lower() == 'a':
            numero = int(input("Digite um número para adicionar a lista: "))
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
            numero = int(input("Digite um número para adicionar a lista: "))
            indice = int(input("Digite o índice em que deseja adicionar o item: "))
            lista.insert(indice, numero)
            mostrar_lista(lista)

        elif comando.lower() == 'p':
            lista.pop()
            mostrar_lista(lista)

        elif comando.lower() == 'f':
            lista.pop(0)
            mostrar_lista(lista)

        elif comando.lower() == 'r':
            mostrar_lista(lista)
            numero_remover = int(input("Qual número deseja remover? \n"))
            if numero_remover not in lista:
                raise ValueError("O número não está na lista.")
            
            else:
                lista.remove(numero_remover)
                mostrar_lista(lista)

        elif comando.lower() == 'o':
            lista_ordenada = merge_sort(lista)
            mostrar_lista(lista_ordenada)

        elif comando.lower() == 'm':
            mostrar_lista(lista)

        else:
            print("O comando não existe. Tente novamente.")

    except ValueError as ve:
        print(f"Erro. {ve}")

    except IndexError:
        print("A lista está vazia.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")