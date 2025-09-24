def calcular():
    print("Bem-vindo à minha calculadora!")
    print("Operações disponíveis: +, -, *, /")

calculando = True
while calculando:
    try:
        operacao = input("Escolha uma operação: +, -, *, / ou 'sair' para encerrar.")
        if operacao.lower() == 'sair':
            print("Encerrando... Até a próxima.")
            calculando = False
            break
        
        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Use apenas os sinais de operação +, -, *, /")
        
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
        print(f"Resultado: {resultado:.2f}")
    
    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")
    except Exception as e:
        print("Erro inesperado: {e}")