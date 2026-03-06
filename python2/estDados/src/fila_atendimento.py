fila = []
entrada = False

print("Instruções: ")
print("Digite um nome para adicionar ou [A] Atender | [V] Verificar | [S] Sair")

while True:
    if entrada and len(fila) == 0:
        print("\nTodos os clientes foram atendidos. Encerrando...")
        break

    comando = input("\nComando ou Nome: ").strip()

    if comando.upper() == 'S':
        print("Encerrando...")
        break
    
    elif comando.upper() == 'V':
        print(f"Fila atual: ({len(fila)} pessoas): {fila}")

    elif comando.upper() == 'A':
        if not fila:
            print("Fila vazia.")
        
        else:
            pessoa_atendida = fila.pop(0)
            print(f"Pessoa atendida: {pessoa_atendida}")

    else:
        nome = comando.capitalize()
        fila.append(nome)
        entrada = True
        print(f"{nome} entrou na fila.")