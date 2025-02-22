def calcular():
    print("Bem-vindo à minha calculadora!")
    print("Operações disponíveis: +, -, *, /.")

continuar = True
while continuar:
    try:
        operacao = input("Escolha uma operação: +, -, *, / ou 'Sair' para encerrar: ")
        if operacao.capitalize() == 'Sair':
            continuar = False
            print("Encerrando a calculadora. Até a próxima.")
            break
        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Use apenas os símbolos padrão das operações.")
        x = float(input("Digite um número: "))
        y = float(input("Digite outro número: "))
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
        print(f"Erro Inesperado. {e}")

if __name__ == 'main':
    calcular()