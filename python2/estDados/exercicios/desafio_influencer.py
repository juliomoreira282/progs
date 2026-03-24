# Listas das diferentes coisas que serão utilizadas no código
uploads = []
historico = []
seguidores = ["@java_master", "@assembly_wizkid", "@front_end_ninja"]

# Menu de comandos
print("\nMenu de Comandos:")
print("Digite 'U' para adicionar algo à fila de uploads.")
print("Digite 'H' para adicionar algo à pilha do histórico.")
print("Digite 'P' para postar algo que esteja na fila de uploads.")
print("Digite 'D' para desfazer algo da pilha do histórico.")
print("Digite 'A' para adicionar um usuário à lista de seguidores da forma normal.")
print("Digite 'V' para adicionar um usuário VIP à lista.")
print("Digite 'B' para banir um usuário.")
print("Digite 'C' para verificar o estado de cada uma das listas.") 
print("Digite 'S' para sair.")

# O código reside no loop abaixo
while True:
    try:   
        comando = input("Digite um comando: ").strip() # Comando que o usuário deve colocar
        if comando.lower() == 's': # Encerra o programa
            print("Encerrando...")
            break

        elif comando.lower() == 'u': # Comando para adicionar um arquivo à fila de uploads
            arquivo = input("Qual arquivo deseja adicionar? \n")
            uploads.append(arquivo.capitalize())
            print(f"{arquivo} foi adicionado à fila.")
            print(f"Qtde. de itens na fila de uploads: {len(uploads)} | Fila de Uploads: {uploads}")

        elif comando.lower() == 'p': # Comando para postar um arquivo na fila de espera de uploads
            arquivo_postado = uploads.pop(0)
            print(f"{arquivo_postado} foi postado.")
            print(f"Qtde. de arquivos restantes: {len(uploads)} | Arquivos restantes: {uploads}")

        elif comando.lower() == 'h': # Comando que adiciona alguma ação à pilha do histórico
            add_historico = input("O que deseja adicionar ao histórico? \n")
            historico.append(add_historico.capitalize())
            print(f"{add_historico} foi adicionado ao histórico.")
            print(f"Qtde. de itens no histórico: {len(historico)} | Itens no histórico: {historico}")

        elif comando.lower() == 'd': # Açaõ que desfaz a última ação do histórico
            historico_undo = historico.pop()
            print(f"Usuário apertou desfazer... Item removido: {historico_undo}")
            print(f"Qtde. de itens no histórico: {len(historico)} | Itens no histórico: {historico}")

        elif comando.lower() == 'a': # Comando para adicionar um seguidor colocando-o no final da lista
            add_usuario = input("Qual o nome de usuário a ser adicionado à lista de seguidores? Use o '@' antes de seu nome de usuário. \n")
            seguidores.append(add_usuario)
            print(f"Qtde. de seguidores: {len(seguidores)} | Seguidores: {seguidores}")

        elif comando.lower() == 'v': # Comando para adicionar um usuário VIP, colocando-o no índice 0 da lista
            add_usuario_vip = input("Qual seu nome de usuário, senhor usuário VIP? Não se esqueça de usar o '@'. \n")
            seguidores.insert(0, add_usuario_vip)
            print(f"Seja muito bem-vindo! {add_usuario_vip}!")
            print(f"Qtde. de seguidores: {len(seguidores)} | Seguidores: {seguidores}")

        elif comando.lower() == 'b': # Comando para banir o usuário se ele estiver na lista
            banir_usuario = input("Qual usuário deseja banir? \n")
            if banir_usuario not in seguidores: # Caso o usuário não exista, levanta um ValueError
                raise ValueError(f"{banir_usuario} não está na lista, tente novamente.")

            else:
                seguidores.remove(banir_usuario)
                print(f"{banir_usuario} foi banido... Bye-Bye loser!")
                print(f"Qtde. de seguidores: {len(seguidores)} | Seguidores: {seguidores}")

        elif comando.lower() == 'c': # Comando para verificar todas as listas simultaneamente
            print(f"Qtde. de itens na fila de uploads: {len(uploads)} | Fila de Uploads: {uploads}")
            print(f"Qtde. de itens no histórico: {len(historico)} | Itens no histórico: {historico}")
            print(f"Qtde. de seguidores: {len(seguidores)} | Seguidores: {seguidores}")

        else: # Mensagem mostrada caso o usuário coloque um comando que não existe.
            print("O comando não existe. Tente novamente.")

    # Exceção caso o nome de usuário não exista na lista de seguidores 
    except ValueError as ve:
        print(f"Erro. {ve}")

    # Exceção usada caso o usuário tente remover algo de uma lista vazia
    except IndexError:
        print("A lista está vazia. Adicione algo à lista.")

    # Exceção usada caso algum erro inesperado ocorra
    except Exception as e:
        print(f"Erro inesperado. {e}")