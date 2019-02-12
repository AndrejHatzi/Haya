
from sly import Lexer
from sly import Parser

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, FLOAT, STRING, IF, THEN, ELSE, FOR, WHILE, PRINT, FUN, TO, ARROW, EQEQ, LEQ, RPAREN, LPAREN}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'if'
    THEN = r':'
    ELSE = r'else'
    FOR = r'for'
    WHILE = r'while'
    FUN = r'FUN'
    TO = r','
    ARROW = r'->'
    PRINT = r'print'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    RPAREN = r'[(]'
    LPAREN = r'[)]'


    EQEQ = r'=='
    LEQ = r'<='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    #match floats
    #Not working!!
    @_(r'^[+-]?[0-9]*\.[0-9]+$"')
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

    @_('PRINT RPAREN condition LPAREN')
    def statement(self, p):
        return ('print_stmt_condition', p.condition)

    #for (x=5, 10): x
    @_('FOR RPAREN var_assign TO expr LPAREN THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

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
    @_('FUN NAME "(" ")" ARROW statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)
    #Deprecated
    @_('NAME "(" ")"')
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

class BasicExecute:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        print(env)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):

        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] == None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree(node[2][1])
            return self.walkTree(node[2][2])

        if node[0] == 'if_else_stmt':
            result = self.walkTree(node[1])
            if result:
                return self.walkTree[2][1]

        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

        if node[0] == 'condition_leq':
            return self.walkTree(node[1]) <= self.walkTree(node[2])

        if node[0] == 'fun_def':
            self.env[node[1]] = node[2]

        if node[0] == 'fun_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("Undefined function '%s'" % node[1])
                return 0

        if node[0] == 'add':
            return self.walkTree(node[1]) + self.walkTree(node[2])
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return self.walkTree(node[1]) / self.walkTree(node[2])

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0

        if node[0] == 'for_loop':
            if node[1][0] == 'for_loop_setup':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count+1, loop_limit+1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        print(res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == 'for_loop_setup':
            return (self.walkTree(node[1]), self.walkTree(node[2]))

        if node[0] == 'while_loop':
            stmt = self.walkTree(node[1][1])
            print(stmt)
            while stmt:
                res = self.walkTree(node[2])
                if res:
                    return self.walkTree(node[2][1])





            #if node[1][0] == 'while_loop_setup':
                #loop_setup = self.walkTree(node[1])
                #print(loop_setup)

        #It lacks var ref printing!
        if node[0] == 'print_stmt_string':
            print(node[1][1:-1])

        if node[0] == 'print_stmt_var':
            try:
                print (self.env[node[1]])
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0

        if node[0] == 'print_stmt_expr':
            res = self.walkTree(node[1])
            print(res)

        if node[0] == 'print_stmt_condition':
            return self.walkTree(node[1])





if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('haya console > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)
