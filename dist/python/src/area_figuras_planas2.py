continuar = True
while continuar:
    figura_plana = input("Digite o tipo da figura plana ou use 'Sair' para cancelar. \n")
    if figura_plana.capitalize() == 'Sair':
        print("Saindo...")
        continuar = False
        break
    elif figura_plana.capitalize() == 'Quadrado':
        lado = float(input("Qual o valor do quadrado? "))
        area = lado ** 2
    elif figura_plana.capitalize() in ['Paralelogramo', 'Retângulo']:
        base = float(input("Qual o valor da base? "))
        altura = float(input("Qual o valor da altura? "))
        area = base * altura
    else:
        match(figura_plana.capitalize()):
            case 'Triângulo':
                base = float(input("Qual o valor da base? "))
                altura = float(input("Qual o valor da altura? "))
                area = base * altura / 2
            case 'Losango':
                diagonalMaior = float(input("Qual o valor da diagonal maior? "))
                diagonalMenor = float(input("Qual o valor da diagonal menor? "))
                area = diagonalMaior * diagonalMenor / 2
            case 'Trapézio':
                baseMaior = float(input("Qual o valor da base maior? "))
                baseMenor = float(input("Qual o valor da base menor? "))
                altura = float(input("Qual o valor da altura? "))
                area = (baseMaior * baseMenor) * altura / 2
            case 'Círculo':
                raio = float(input("Qual o valor do raio? "))
                area = 3.14 * (raio ** 2)
            case _:
                print("Opção inválida. Tente novamente.")
    print(f"A área do {figura_plana} é {area:.2f}.")