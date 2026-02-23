historico_texto = []

while True:
    comando = input("Digite uma palavra (ou 'Z' para desfazer, 'S' para sair): ")
    if comando.upper() == 'S':
        print("Encerrando editor...")
        break

    elif comando.upper() == 'Z':
        if len(historico_texto) > 0:
            historico_texto.pop()
        else:
            print("A pilha está vazia.")
    
    else:
        historico_texto.append(comando)

    print(f"Texto na tela: {' '.join(historico_texto)}")
    print("-" * 30)