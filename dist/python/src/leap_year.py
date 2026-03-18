ano = int(input("Digite um ano: "))

if ano < 1582:
    print("Não dentro do calendário gregoriano.")

else:
    if ano % 4 != 0:
        print("Ano comum")

    elif ano % 100 != 0:
        print("Ano bissexto")

    elif ano % 400 != 0:
        print("Ano comum")

    else:
        print("Ano bissexto")

