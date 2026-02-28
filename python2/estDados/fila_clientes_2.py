fila = []

fila.append("Cliente 1")
fila.append("Cliente 2")
fila.append("Cliente 3")

print("Próximo:", fila[0])

atendido = fila.pop(0)

print("Atendido:", atendido)

print("Fila atual:", fila)

if "Cliente 2" in fila:
    print("Está na fila.")

else:
    print("Não está na fila.")

fila.clear()

print("Fila atual:", fila)