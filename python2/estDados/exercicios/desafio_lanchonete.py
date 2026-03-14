pedidos = []
pedidos_prontos = []
pedidos_in_line = False # Flag que verifica se há algum pedido esperando para ser entregue

# Menu de Comandos para as diferentes ações do bloco de baixo.
print("\nMenu de Comandos:")
print("Digite 'V' para verificar os pedidos na fila de preparo e espera.")
print("Digite 'P' para preparar um lanche.")
print("Digite 'E' para entregar um lanche.")
print("Digite 'S' para sair.")

while True:
    if not pedidos_in_line: # Se não houver pedidos esperando para ser entregue, esse bloco será executado.
        acao = input("O que deseja fazer: Inserir lanches ou sair? [I] Inserir | [S] Sair \n") # Pergunta ao usuário se ele quer inserir itens ou encerrar o programa.
        if acao.upper() == 'S': # Encerra o programa sem executar o outro bloco.
            print("Encerrando...")
            break

        elif acao.upper() == 'I': # Pede os itens a serem adicionados de acordo com a quantidade fornecida.
            qtd = int(input("Quantos itens deseja adicionar? \n"))
            
            if qtd > 10: # Ignora o pedido se a quantidade for maior que 10
                print("Desculpe. Não aceitamos pedidos com mais de 10 itens.")
            
            for i in range(qtd): # Adiciona os itens um a um de acordo com a quantidade fornecida.
                pedido = input("O que deseja adicionar? \n")
                item = pedido.capitalize()
                pedidos.append(item)
                print(f"{item} foi adicionado à lista.")
                pedidos_in_line = True # O valor da flag é alterado para executar o outro bloco de código
            
    elif pedidos_in_line and len(pedidos) > 0 or len(pedidos_prontos) > 0: # Se o valor da flag pedidos_in_line = True e se houver pedidos em alguma das listas.
        try:  # Tenta pegar algum possível erro  
            comando = input("Escolha um comando para realizar uma ação: [V] [P] [E] [S] \n") # Pede para o usuário realizar um comando de acordo com as teclas.
            if comando.upper() == 'S': # Encerra o programa caso haja um item em alguma das listas.
                print("Encerrando...")
                break
            
            elif comando.upper() == 'V': # Verifica a quantidade de lanches esperando o preparo ou a entrega.
                print(f"Qtde. de lanches esperando para serem prontos: {len(pedidos)} | Lanches em espera: {pedidos}")
                print(f"Quantidade de lanches esperando para serem entregues: {len(pedidos_prontos)} | Lanches em espera: {pedidos_prontos}")

            elif comando.upper() == 'P': # Remove o item da lista de espera de preparo e adiciona-o à lista de espera de entrega (Pilha).
                lanche_a_preparar = pedidos.pop()
                pedidos_prontos.append(lanche_a_preparar)
                print(f"{lanche_a_preparar} está pronto.")

            elif comando.upper() == 'E': # Remove o item da lista de espera de entrega e o entrega (Fila).
                lanche_entregue = pedidos_prontos.pop(0)
                print(f"{lanche_entregue} foi entregue.")

                if len(pedidos_prontos) == 0: # Caso todos os itens tenham sido entregues, altera a flag pedidos_in_line para False. 
                    pedidos_in_line = False

        except IndexError: # Exibe uma mensagem de erro caso o usuário tente preparar ou entregar algo com a lista vazia.
            print("A lista está vazia.")