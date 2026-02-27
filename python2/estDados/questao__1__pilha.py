pilha_livros: list[str] = ["Dom Casmurro", "A Hora da Estrela"]

pilha_livros.append("O Alquimista")

livro_saiu = pilha_livros.pop()

print(f"Livro que deveria ter saído por último: {livro_saiu}")
print(f"Pilha restante: {pilha_livros}")