pilha_livros = []

pilha_livros.append("Livro de Python")
pilha_livros.append("Livro de Algoritmos")
pilha_livros.append("Livro de Redes")

print(f"Pilha Atual: {pilha_livros}")

topo = pilha_livros[-1]

print(f"O livro que está no topo é: {topo}")

livro_removido = pilha_livros.pop()
print(f"Removendo o topo: {livro_removido}")

print(f"Pilha após a remoção: {pilha_livros}")