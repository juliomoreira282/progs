import sys
import ply.lex as lex
import ply.yacc as yacc

# --- Tokens ---
reserved = {'print': 'PRINT'}
tokens = [
    'ID', 'NUMBER', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'MODULO', 'POWER', 'EQUALS', 'LPAREN', 'RPAREN', 'SEMICOLON'
] + list(reserved.values)

t_PLUS, t_MINUS, t_TIMES, t_DIVIDE, t_MODULO, t_POWER = r'\+', r'\-', r'\*', r'/', r'%', r'\^'
t_EQUALS, t_LPAREN, t_RPAREN, t_SEMICOLON = r'=', r'\(', r'\)', r';'

def t_FLOAT(t): r'\d+\.\d+'; t.value = float(t.value); return t
def t_NUMBER(t): r'\d+'; t.value = int(t.value); return t
def t_ID(t): r'[a-zA-Z_][a-zA-Z_0-9]*'; t.type = reserved.get(t.value, 'ID'); return t
def t_newline(t): r'\n+'; t.lexer.lineno += len(t.value)
def t_error(t): print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}"); t.lexer.skip(1)

# --- Tabela de Símbolos e Geração de Código ---
symbol_table = {}
intermediate_code = []

# --- Regras de Tipo ---
def promote_type(type1, type2, op):
    if op == '/': return 'float'
    if type1 == 'float' or type2 == 'float': return 'float'
    return 'int'

# --- Gramática ---
precedence = (
    ('left', 'PLUS', 'MINUS')
    ('left', 'TIMES', 'DIVIDE', 'MODULO')
    ('right', 'POWER')
    ('right', 'UMINUS')
)

def p_program(p):
    '''program: statement list'''
    pass

def p_statement_list(p):
    '''statement list: statement
    | statement list statement'''
    pass

