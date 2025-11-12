# interpreter.py
import sys

variables = {}
stack = []

# evaluate_rpn permanece o mesmo, mas agora é uma função "privada"
def _evaluate_rpn(tokens):
    stack.clear() 
    for token in tokens:
        # Se for variável, busca o valor (que já tem tipo)
        if token in variables: stack.append(variables[token])
        # Se for operador, opera
        elif token == '+': val2 = stack.pop(); val1 = stack.pop(); stack.append(val1 + val2)
        elif token == '-': val2 = stack.pop(); val1 = stack.pop(); stack.append(val1 - val2)
        elif token == '*': val2 = stack.pop(); val1 = stack.pop(); stack.append(val1 * val2)
        elif token == '/':
            val2 = stack.pop(); val1 = stack.pop()
            if val2 == 0: print("Erro de Execução: Divisão por zero."); raise SystemExit
            stack.append(val1 / val2)
        elif token == '%':
            val2 = stack.pop(); val1 = stack.pop()
            if val2 == 0: print("Erro de Execução: Divisão por zero (módulo)."); raise SystemExit
            stack.append(val1 % val2)
        elif token == '^': val2 = stack.pop(); val1 = stack.pop(); stack.append(val1 ** val2)
        elif token == '~': val = stack.pop(); stack.append(-val) # Menos unário
        else:
            # Se não for operador nem variável, deve ser um literal numérico
            try: stack.append(int(token))
            except ValueError:
                try: stack.append(float(token))
                except ValueError: print(f"Erro: Token RPN desconhecido: {token}"); raise SystemExit
    return stack.pop()


def reset_interpreter():
    """Limpa o estado global (memória) do interpretador."""
    variables.clear()

def interpret_rpn(rpn_lines_list):
    """
    Executa uma lista de linhas de código RPN.
    Imprime a saída de 'print' e retorna a memória final.
    """
    reset_interpreter()
    
    print("--- INICIANDO INTERPRETADOR RPN ---")
    for line in rpn_lines_list:
        tokens = line.strip().split()
        if not tokens: continue
        
        action = tokens[-1]
        
        if action == '=':
            var_name = tokens[0]
            rpn_expression = tokens[1:-1]
            result = _evaluate_rpn(rpn_expression)
            variables[var_name] = result
            print(f"  Exec: {var_name} = {result} (Tipo: {type(result).__name__})")
            
        elif action == 'print':
            var_name = tokens[0]
            if var_name in variables:
                print(f"  PRINT: {variables[var_name]}")
            else:
                print(f"Erro de Execução: Variável '{var_name}' não definida.")
    
    print("--- EXECUÇÃO CONCLUÍDA ---")
    return dict(variables) # Retorna uma cópia da memória


# Este bloco só executa se o script for chamado diretamente
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python interpreter.py <arquivo_rpn>")
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado.")
            sys.exit(1)
        
        # Chama a nova função refatorada
        final_memory = interpret_rpn(lines)
        print("Memória Final:", final_memory)