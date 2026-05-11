produtos = {
    "001": { "nome": "Camiseta", "preco": 29.90, "estoque": 100 },
    "002": { "nome": "Calça Jeans",  "preco": 99.90, "estoque": 50 },
    "003": { "nome": "Tênis", "preco": 199.90, "estoque": 30 },
    "004": { "nome": "Jaqueta", "preco": 149.90, "estoque": 20 },
    "005": { "nome": "Boné", "preco": 19.90, "estoque": 150 },
    "006": { "nome": "Mochila", "preco": 89.90, "estoque": 40 },
    "007": { "nome": "Relógio", "preco": 249.90, "estoque": 10 },
    "008": { "nome": "Óculos de Sol", "preco": 79.90, "estoque": 25 },
    "009": { "nome": "Cinto", "preco": 39.90, "estoque": 50 },
    "010": { "nome": "Carteira", "preco": 49.90, "estoque": 80 }
}

lista_id_produtos = [chave for chave in produtos.keys()]

print("\nLista de Comandos:")
print("Digite 'A' para mostrar a lista de ID de produtos.")
print("Digite 'R' para ler as informações do dicionário principal.")
print("Digite 'D' para deletar um item do dicionário.")
print("Digite 'L' para ler as informações de um item em específico.")
print("Digite 'N' para adicionar um novo item ao dicionário.")
print("Digite 'U' para substituir os valores de um item no dicionário.")
print("Digite 'S' para sair.")

while True:
    comando = input("Comando: ").strip()

    if comando.upper() == 'S':
        print("Encerrando...")
        break

    elif comando.upper() == 'A':
        print(f"Lista de IDs: {lista_id_produtos}")

    elif comando.upper() == 'R':
        print("\nDicionário Completo de Produtos:")
        for pid, info in produtos.items():
            print(f"ID: {pid} | Nome: {info['nome']} | Preço: R$ {info['preco']:.2f} | Estoque: {info['estoque']} un.")

    elif comando.upper() == 'L':
        id_produto = input("Qual o produto que deseja visualizar? \n")
        resultado = produtos.get(id_produto, "Produto não encontrado.")
        print(f"ID: {id_produto} | Nome: {resultado['nome']} | Preço: R$ {resultado['preco']:.2f} | Estoque: {resultado['estoque']} un.")

    elif comando.upper() == 'D':
        id_produto = input("Qual produto deseja remover? \n")
        if id_produto in lista_id_produtos:
            del produtos[id_produto]
            lista_id_produtos.remove(id_produto)
            print(f"Produto de ID {id_produto} removido com sucesso.")

        else:
            print(f"Produto de ID {id_produto} não encontrado para ser removido.")

    elif comando.upper() == 'U':
        id_produto = input("Qual produto deseja atualizar? \n")
        if id_produto in lista_id_produtos:
            comando = int(input("Deseja mudar o nome do produto? (0: Não | 1: Sim)"))
            
            if comando == 0:
                preco = float(input("Qual o novo preço do produto? \n"))
                estoque = int(input("Qual o novo estoque desse produto? \n"))
                produtos[id_produto]["preco"] = preco
                produtos[id_produto]["estoque"] = estoque
                resultado = produtos.get(id_produto)
                print(f"Valores do produto de ID {id_produto} atualizado com sucesso.")
                print(f"ID: {id_produto} | Nome: {resultado['nome']} | Preço: R$ {resultado['preco']:.2f} | Estoque: {resultado['estoque']} un.")

            elif comando == 1:
                nome = input("Qual o nome do produto? \n")
                preco = float(input("Qual o preço do produto? \n"))
                estoque = int(input("Qual o estoque do produto? \n"))
                produtos[id_produto]["nome"] = nome
                produtos[id_produto]["preco"] = preco
                produtos[id_produto]["estoque"] = estoque
                resultado = produtos.get(id_produto)
                print(f"Produto de ID {id_produto} alterado com sucesso.")
                print(f"ID: {id_produto} | Nome: {resultado['nome']} | Preço: R$ {resultado['preco']:.2f} | Estoque: {resultado['estoque']} un.")

            else:
                print("Comando inválido. Tente novamente.")

        else:
            print("Produto não encontrado para a substituição de valores.")

    elif comando.upper() == 'N':
        id_produto_novo = input("Digite a ID do produto novo: \n")
        nome = input("Digite o nome do produto: \n")
        preco = float(input("Digite o preço do produto: \n"))
        estoque = int(input("Digite o estoque do produto: \n"))
        produtos.update({id_produto_novo: {"nome": nome.capitalize(), "preco": preco, "estoque": estoque}})
        lista_id_produtos.append(id_produto_novo)
        print(f"Produto de ID {id_produto_novo} adicionado com sucesso.")

    else:
        print("Comando inválido. Tente novamente.")