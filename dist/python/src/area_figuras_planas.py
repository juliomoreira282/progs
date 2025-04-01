calcular = True
while calcular:
    figura_plana = input("Qual o tipo da figura plana? Use 'Sair' para encerrar. \n")
    if figura_plana.capitalize() == 'Sair':
        print("Até a próxima!")
        calcular = False
        break
    match(figura_plana.capitalize()):
        case "Paralelogramo":
            base = float(input("Qual o valor da base? \n"))
            altura = float(input("Qual o valor da altura? \n"))
            area = base * altura
        case "Triângulo":
            base = float(input("Qual o valor da base? \n"))
            altura = float(input("Qual o valor da altura? \n"))
            area = base * altura / 2
        case "Losango":
            diagonal_maior = float(input("Qual o valor da diagonal maior? \n"))
            diagonal_menor = float(input("Qual o valor da diagonal menor? \n"))
            area = diagonal_maior * diagonal_menor / 2
        case "Círculo":
            raio = float(input("Qual o valor do raio? \n"))
            area = 3.14 * (raio * raio)
        case _:
            print("Figura plana inválida.")
    print(f"A área do {figura_plana} é {area:.2f}")