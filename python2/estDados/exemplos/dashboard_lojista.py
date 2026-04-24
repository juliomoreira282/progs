estoque_vendido = ["M", "P", "G", "M", "GG", "M", "P"]

copia_estoque_vendido = estoque_vendido.copy()
copia_estoque_vendido.sort(reverse=True)

print(f"Estoque organizado: {copia_estoque_vendido}")

if "G" in copia_estoque_vendido:
    print("Nós vendemos G.")

else:
    print("Nós não vendemos G.")

quantidade_M = copia_estoque_vendido.count('M')
print(f"Quantidade de camisas 'M' vendidas: {quantidade_M}")

posicao_gg = copia_estoque_vendido.index("GG")
print(f"A primeira GG está no índice {posicao_gg + 1}.")