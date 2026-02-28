fila = []

fila.append("A")
fila.append("B")
fila.append("C")
fila.append("D")
fila.append("E")
fila.append("F")

print(fila)

clientes_totais = ""

while len(fila) > 0:
    atendido = fila.pop(0)
    clientes_totais += atendido
    print(clientes_totais)
    print(fila)


if len(fila) == 0:
    print("Fila vazia.")

else:
    print("Fila com elementos.")

quantidade = len(fila)
print(quantidade)