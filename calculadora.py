def calcular():
    print("Bem-vindo à minha calculadora!")
    print("Operações disponíveis: +, -, *, /.")
while True:
    try:
        operacao = input("Escolha uma operação: (+, -, *, /) ou 'Sair' para encerrar. \n").strip()
        if operacao.capitalize() == 'sair':
            print("Saindo da calculadora... Até a próxima. \n")
            break
        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida. Use apenas +, -, *, /.")
        x = float(input("Digite um número: \n"))
        y = float(input("Digite outro número: \n"))
        match(operacao):
            case '+':
                resultado = x + y
            case '-':
                resultado = x - y
            case '*':
                resultado = x * y
            case '/':
                if y == 0:
                    raise ZeroDivisionError("Não é permitido divisão por zero.")
                resultado = x / y
        print(f"Resultado: {resultado}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")
    except Exception as e:
        print(f"Erro inesperado: {e}")