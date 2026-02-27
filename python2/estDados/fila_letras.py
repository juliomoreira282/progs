fila = []

fila.append("C")
fila.append("B")
fila.append("A")

print(fila)

atendido = fila.pop(0)

print(atendido)
print(fila)

primeiro = fila[0]
print(primeiro)

ultimo = fila[-1]

print(ultimo)

if len(fila) == 0:
    print("Fila vazia.")

else:
    print("Fila com elementos.")

quantidade = len(fila)
print(quantidade)