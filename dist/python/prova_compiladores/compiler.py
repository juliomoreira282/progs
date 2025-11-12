import sys
import ply.lex as lex
import ply.yacc as yacc

# --- Tokens  ---
reserved = {'print': 'PRINT'}
tokens = [
    'ID', 'NUMBER', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'MODULO', 'POWER', 'EQUALS', 'LPAREN', 'RPAREN', 'SEMICOLON'
] + list(reserved.values())
t_PLUS, t_MINUS, t_TIMES, t_DIVIDE, t_MODULO, t_POWER = r'\+', r'-', r'\*', r'/', r'%', r'\^'
t_EQUALS, t_LPAREN, t_RPAREN, t_SEMICOLON = r'=', r'\(', r'\)', r';'
t_ignore = ' \t'

def t_FLOAT(t): r'\d+\.\d+'; t.value = float(t.value); return t
def t_NUMBER(t): r'\d+'; t.value = int(t.value); return t
def t_ID(t): r'[a-zA-Z_][a-zA-Z_0-9]*'; t.type = reserved.get(t.value, 'ID'); return t
def t_newline(t): r'\n+'; t.lexer.lineno += len(t.value)
def t_error(t): print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}"); t.lexer.skip(1)

# --- Tabela de Símbolos e Geração de Código ---
symbol_table = {}
intermediate_code = []

# --- Regras de Tipo  ---
def promote_type(type1, type2, op):
    if op == '/': return 'float'
    if type1 == 'float' or type2 == 'float': return 'float'
    return 'int'

# --- Gramática  ---
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
    ('right', 'POWER'),
    ('right', 'UMINUS'),
)

def p_program(p): 
    '''program : statement_list'''
    pass

def p_statement_list(p): 
    '''statement_list : statement 
    | statement_list statement'''
    pass

def p_statement_assignment(p):
    '''statement : ID EQUALS expression SEMICOLON'''
    expr_type, expr_rpn = p[3]
    symbol_table[p[1]] = expr_type
    rpn_line = f"{p[1]} {expr_rpn} ="
    intermediate_code.append(rpn_line)

def p_statement_print(p):
    '''statement : PRINT LPAREN ID RPAREN SEMICOLON'''
    if p[3] not in symbol_table:
        print(f"Erro Semântico: Variável '{p[3]}' usada em print() não foi declarada. Linha {p.lineno(3)}"); raise SystemExit
    intermediate_code.append(f"{p[3]} print")

def p_expression_binop(p):
    '''expression : expression PLUS expression 
                   | expression MINUS expression 
                   | expression TIMES expression 
                   | expression DIVIDE expression 
                   | expression MODULO expression 
                   | expression POWER expression'''
    type1, rpn1 = p[1] 
    type2, rpn2 = p[3] 
    op = p[2]
    result_type = promote_type(type1, type2, op)
    if op in ['/', '%'] and rpn2 == '0':
        print(f"Erro Semântico: Tentativa de divisão por zero literal. Linha {p.lineno(2)}"); 
        raise SystemExit
    p[0] = (result_type, f"{rpn1} {rpn2} {op}")

def p_expression_uminus(p): 
    '''expression : MINUS expression %prec UMINUS''' 
    expr_type, expr_rpn = p[2] 
    p[0] = (expr_type, f"{expr_rpn} ~")

def p_expression_group(p): 
    '''expression : LPAREN expression RPAREN''' 
    p[0] = p[2]

def p_expression_number(p): 
    '''expression : NUMBER''' 
    p[0] = ('int', str(p[1]))

def p_expression_float(p): 
    '''expression : FLOAT''' 
    p[0] = ('float', str(p[1]))

def p_expression_id(p):
    '''expression : ID'''
    if p[1] not in symbol_table:
        print(f"Erro Semântico: Variável '{p[1]}' não declarada. Linha {p.lineno(1)}"); raise SystemExit
    p[0] = (symbol_table[p[1]], p[1])

def p_error(p):
    if p: print(f"Erro Sintático: Token inesperado '{p.value}' (tipo {p.type}) na linha {p.lineno}")
    else: print("Erro Sintático: Fim de arquivo inesperado (EOF)")

# --- Construção dos Analisadores ---
lexer = lex.lex()
parser = yacc.yacc()

# Reiniciar Compilador

def reset_compiler():
    """Limpa o estado global do compilador para uma nova execução."""
    global symbol_table, intermediate_code
    symbol_table.clear()
    intermediate_code = []
    # Reinicia o lexer
    lexer.lineno = 1

def get_tokens(code_string):
    """Executa apenas o analisador léxico e retorna uma lista de tokens."""
    reset_compiler()
    lexer.input(code_string)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list

def compile_code(code_string):
    """
    Executa o compilador completo (lex, yacc, semântico) no código.
    Retorna (lista_rpn, tabela_simbolos) em caso de sucesso.
    Lança SystemExit em caso de erro.
    """
    reset_compiler()
    parser.parse(code_string, lexer=lexer)
    # Retorna uma cópia dos resultados
    return list(intermediate_code), dict(symbol_table) 

# Este bloco só executa se o script for chamado diretamente
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compiler.py <arquivo_de_codigo>")
    else:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                code = f.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado.")
            sys.exit(1)
        
        print("--- ETAPA 1: ANÁLISE LÉXICA (Tokens) ---")
        tokens_list = get_tokens(code)
        for tok in tokens_list:
            print(f"  {tok.type:10} | {str(tok.value):10} | Linha {tok.lineno}")
        print("-" * 40)

        print("\n--- ETAPAS 2, 3 E 4 (Parse, Semântica e Geração de Código) ---")
        try:
            # Re-compila para obter o RPN e a tabela de símbolos
            rpn, sym_table = compile_code(code) 
            print("Análise concluída com sucesso.")
            
            print("\n--- ETAPA 3: TABELA DE SÍMBOLOS (Final) ---")
            print("  Variáveis declaradas (Nome: Tipo):")
            for symbol, type_val in sym_table.items():
                print(f" - {symbol}: {type_val}")
            print("-" * 40)

            print("\n--- ETAPA 4: CÓDIGO INTERMEDIÁRIO (RPN) ---")
            for line in rpn:
                print(f"  {line}")
            print("-" * 40)
            
        except SystemExit:
            print("Compilação interrompida devido a erro.")