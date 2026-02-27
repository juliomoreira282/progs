fila = []

# Enfileirar (enqueue)
fila.append("Cliente 1")
fila.append("Cliente 2")
fila.append("Cliente 3")

# Desenfileirar (dequeue)
atendido = fila.pop(0)

print("Atendido:", atendido)
print("Fila Atual:", fila)