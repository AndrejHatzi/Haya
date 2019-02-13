from sly import Lexer
from sly import Parser

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, FLOAT, STRING, IF, THEN, ELSE, FOR, FASTERLOOP, WHILE, CREATE, LEQ, PRINT, FUN,TO, ARROW, EQEQ, RPAREN, LPAREN}
    #{ NAME, NUMBER, FLOAT, STRING, IF, THEN, ELSE, FOR, FASTERLOOP, WHILE,FUN,CREATE,TO, ARROW,PRINT,EQEQ, RPAREN, LPAREN}
    ignore = '\t '
    # ADDED '.' TRY FOR FLOATS
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' , '.'}

    # Define tokens
    IF = r'if'
    THEN = r':'
    ELSE = r'else'
    FOR = r'for'
    FASTERLOOP = r'fasterfor'
    WHILE = r'while'
    FUN = r'FUN'
    CREATE = r'createfile'
    TO = r','
    ARROW = r'->'
    PRINT = r'print'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    RPAREN = r'[(]'
    LPAREN = r'[)]'
    '''
    @_('expr PLUS term',
   'expr MINUS term')
def expr(self, p):
    return (p[1], p.expr, p.term)
    '''

    '''
    @_('LPAREN expr RPAREN')
def expr(self, p):
    return ('group-expression',p.expr])
    '''


    EQEQ = r'=='
    LEQ = r'<='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    #match floats
    #Not working!! #=> implementar build 0
    @_(r'[+-]((\d+(\.\d*)?)|\.\d+)([eE][+-]?[0-9]+)?')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

class BasicParser(Parser):
    tokens = BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )

    def __init__(self):
        self.env = { }

    @_('')
    def statement(self, p):
        pass

    @_('PRINT RPAREN NAME LPAREN')
    def statement(self, p):
        return ('print_stmt_var', p.NAME)

    @_('PRINT RPAREN expr LPAREN')
    def statement(self, p):
        return ('print_stmt_expr', p.expr)

    @_('PRINT RPAREN STRING LPAREN')
    def statement(self, p):
        return ('print_stmt_string', p.STRING)

    @_('CREATE STRING')
    def statement(self, p):
        return ('create_stmt_string', p.STRING)

    @_('CREATE RPAREN NAME LPAREN')
    def statement(self, p):
        return ('create_stmt_var', p.NAME)


    #for (x=5, 10): x
    @_('FOR RPAREN var_assign TO expr LPAREN THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('FASTERLOOP RPAREN var_assign TO expr LPAREN THEN statement')
    def statement(self, p):
        return ('faster_for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('WHILE RPAREN condition LPAREN THEN statement')
    def statement(self, p):
        return ('while_loop', ('while_loop_setup', p.condition), p.statement)
    #if x==5: x
    @_('IF condition THEN statement')
    def statement(self, p):
        return ('if_stmt', p.condition, ('branch', p.statement))

    #if x==5: x else y
    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return ('if_else_stmt', p.condition, ('branch', p.statement0, p.statement1))

    #Deprecated
    @_('FUN NAME RPAREN LPAREN ARROW statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)
    #Deprecated
    @_('NAME RPAREN LPAREN')
    def statement(self, p):
        return ('fun_call', p.NAME)

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('expr LEQ expr')
    def condition(self, p):
        return ('condition_leq', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    @_('expr')
    def statement(self, p):
        return (p.expr)

    @_('expr "+" expr')
    def expr(self, p):
        return ('add', p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ('sub', p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ('mul', p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ('div', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)

    @_('FLOAT')
    def expr(self, p):
        return ('float', p.FLOAT)

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('haya console >')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
