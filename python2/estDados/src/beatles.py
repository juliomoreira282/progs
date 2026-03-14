beatles = []

print("Etapa 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Etapa 2:", beatles)

for i in range(2):
    new_members = input("Insira os novos membros da banda: Stu Sutcliffe e Pete Best: ")
    beatles.append(new_members)

print("Etapa 3:", beatles)

del beatles[4]
del beatles[3]

print("Etapa 4:", beatles)

beatles.insert(0, "Ringo Starr")

print("Etapa 5:", beatles)

print("O fabuloso", len(beatles))