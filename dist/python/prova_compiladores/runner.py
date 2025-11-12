# run.py
import sys
import argparse
# Importa as *funções* específicas que refatoramos
try:
    from compiler import compile_code, get_tokens
    from interpreter import interpret_rpn
except ImportError:
    print("Erro: Verifique se 'compiler.py' e 'interpreter.py' estão no mesmo diretório.")
    sys.exit(1)

def main():
    # 1. Configura o argparse para uma CLI amigável
    parser = argparse.ArgumentParser(
        description="Compilador e Interpretador para uma linguagem aritmética simples.",
        epilog="Exemplo de uso: py run.py meu_codigo.txt"
    )
    
    # Argumento principal: o arquivo de código-fonte
    parser.add_argument(
        'source_file',
        type=str,
        help="O arquivo de código-fonte a ser processado."
    )
    
    # Grupo de opções para controlar o que fazer
    action_group = parser.add_mutually_exclusive_group()
    
    action_group.add_argument(
        '--tokens',
        action='store_true',
        help="Executa apenas o analisador léxico (scanner) e exibe os tokens."
    )
    
    action_group.add_argument(
        '--compile-only',
        action='store_true',
        help="Compila o código para RPN, mas não o executa."
    )
    
    # Analisa os argumentos da linha de comando
    args = parser.parse_args()

    # 2. Lê o arquivo de código-fonte
    try:
        with open(args.source_file, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{args.source_file}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        sys.exit(1)

    # 3. Executa a ação solicitada
    try:
        # Ação: --tokens
        if args.tokens:
            print(f"--- Tokens de '{args.source_file}' ---")
            tokens_list = get_tokens(code)
            for tok in tokens_list:
                print(f"  {tok.type:10} | {str(tok.value):10} | Linha {tok.lineno}")
        
        # Ação: --compile-only
        elif args.compile_only:
            print(f"--- Compilando '{args.source_file}' ---")
            rpn, sym_table = compile_code(code)
            print("Compilação concluída com sucesso.")
            
            print("\n--- Tabela de Símbolos ---")
            for symbol, type_val in sym_table.items():
                print(f"  - {symbol}: {type_val}")
                
            print("\n--- Código Intermediário (RPN) ---")
            for line in rpn:
                print(f"  {line}")

        # Ação Padrão: Compilar E Executar
        else:
            print(f"--- Compilando e Executando '{args.source_file}' ---")
            # 3a. Compila
            rpn, sym_table = compile_code(code)
            print("Compilação concluída com sucesso.\n")
            
            # 3b. Interpreta o resultado da compilação
            final_memory = interpret_rpn(rpn)
            print("\nMemória Final:", final_memory)

    except SystemExit:
        # Captura os erros sintáticos/semânticos lançados pelo compilador
        print("\nProcesso interrompido devido a erros no código-fonte.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()