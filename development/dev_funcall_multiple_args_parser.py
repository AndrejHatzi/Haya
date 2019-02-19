from sly import Lexer
from sly import Parser
class BasicLexer(Lexer):
    tokens = { FUN, NAME, NUMBER, STRING}
    ignore = '\t '
    #function x ():
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', ':' }

    # Define tokens
    FUN = r'function'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')

class BasicParser(Parser):
    debugfile = 'parser.out'
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

    @_('FUN NAME "(" NAME ")" ":" statement')
    def statement(self, p):
        return ('fun_def', p.NAME0, [p.NAME1] ,p.statement)

    @_('NAME "(" NAME ")"')
    def statement(self, p):
        return ('fun_call', p.NAME0, [p.NAME1])

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    #==> Remover na proxima atualizacao
    #@_('NAME "=" expr')
    #def var_assign(self, p):
        #return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    @_('NAME "=" statement')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.statement)

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

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('haya development edition > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
