pedidos = []
pedidos_prontos = []
pedidos_in_line = False

print("\nMenu de Comandos:")
print("Digite 'V' para verificar os pedidos na fila de preparo e espera.")
print("Digite 'P' para preparar um lanche.")
print("Digite 'E' para entregar um lanche.")
print("Digite 'S' para sair.")

while True:
    if not pedidos_in_line:
        acao = input("O que deseja fazer? [I] Inserir | [S] Sair: \n")
        if acao.lower() == 's':
            print("Encerrando...")
            break

        elif acao.lower() == 'i':
            qtd = int(input("Quantos itens deseja adicionar? \n"))

            if qtd > 10:
                print("Desculpe. Não aceitamos pedidos com mais de 10 itens.")
                continue

            for i in range(qtd):
                pedido = input("O que deseja adicionar? \n")
                item = pedido.capitalize()
                pedidos.append(item)
                print(f"{item} foi adicionado à lista.")
                pedidos_in_line = True

    elif pedidos_in_line and len(pedidos) > 0 or len(pedidos_prontos) > 0:
        try:
            comando = input("Escolha um comando para realizar uma ação: [V] [P] [E] [S] \n")
            if comando.lower() == 's':
                print("Encerrando...")
                break

            elif comando.lower() == 'v':
                print(f"Qtde. de lanches esperando para serem preparados: {len(pedidos)} | Lanches em espera: {pedidos}")
                print(f"Qtde. de lanches esperando para serem entregues: {len(pedidos_prontos)} | Lanches em espera: {pedidos_prontos}")
            
            elif comando.lower() == 'p':
                lanche_a_preparar = pedidos.pop()
                pedidos_prontos.append(lanche_a_preparar)
                print(f"{lanche_a_preparar} está pronto.")

            elif comando.lower() == 'e':
                lanche_entregue = pedidos_prontos.pop(0)
                print(f"{lanche_entregue} foi entregue.")

                if len(pedidos) == 0 and len(pedidos_prontos) == 0:
                    print("Todos os itens foram entregues. Encerrando...")
                    break

            else:
                print("O comando não existe. Use um dos comandos mencionados anteriormente.")

        except IndexError:
            print("A lista está vazia.")