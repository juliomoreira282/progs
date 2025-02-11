def calcular():
    print("Bem vindo à minha calculadora!")
    print("Operações disponíveis: +, -, *, /.")

while True:
    try:
        operacao = input("Digite a operação a ser realizada: (+, -, *, /) ou 'Sair' para encerrar: ")
        if operacao.capitalize() == 'Sair':
            print("Encerrando a calculadora. Até a próxima.")
            break
        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")
        x = float(input("Digite um número: "))
        y = float(input("Digite um outro número: "))
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

if __name__ == 'main':
    calcular()