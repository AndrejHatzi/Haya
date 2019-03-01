from sly import Lexer
from sly import Parser
#http://www.sqlitetutorial.net/sqlite-python/delete/
#https://www.tomordonez.com/sqlite3-cheatsheet-python.html

#THIS VERSION HAS OPTIONAL ()
#
#

'''
@_('item')
def opt_item(self, p):
      return p.item

@_('')
def opt_item(self, p):
     return None
'''

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, ELSE, PRINT, EQEQ}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', ':', '?'}

    # Define tokens
    IF = r'if'
    ELSE = r'else'
    PRINT = r'print'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

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
    tokens = BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS', ','),
        )

    def __init__(self):
        self.env = { }

    @_('')
    def statement(self, p):
        pass

    @_('IF condition ":" statement ELSE statement')
    def statement(self, p):
        return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('PRINT "(" expr ")"')
    #@_('PRINT ARGS')
    def statement(self, p):
        return ('print_stmt_args', p.expr)

    @_('PRINT "(" STRING ")"')
    #@_('PRINT ARGS')
    def statement(self, p):
        return ('print_stmt', p.STRING)

    @_('NAME "(" ")" ":" statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)

    @_('NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.NAME)

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" expr')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.expr)

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    #BasicLexer = lexer(statement)
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

    @_('expr "," expr')
    def expr(self, p):
        return ('args', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
    def expr(self, p):
        return p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('NAME')
    def expr(self, p):
        return ('var', p.NAME)

    @_('NUMBER')
    def expr(self, p):
        return ('num', p.NUMBER)



class BasicExecute:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
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
            else:
                return self.walkTree(node[2][2])

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
        elif node[0] == 'virgulae':
            #return (self.walkTree(node[1]), self.walkTree(node[2]))
            return (self.walkTree(node[1]), self.walkTree(node[2]))

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            return node[1]

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("Undefined variable '"+node[1]+"' found!")
                return 0

        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

        #print print(self.walktree[i]) => qlqr coisa assim!
        #ver docs => do que foi feito anteriormente em relacao ao print
        #=> magrs => tem mesmo de levar um return type x => e checkar se o type e o type para nao colocar o programa em erros!
        if node[0] == 'print_stmt_args':
            #print(node)
            #print(node[1])
            res = self.walkTree(node[1]);
            print(res, len(node[1]));
            print(node[1]);
            #print(node.count(args));
            ln : str = str(node[1]);
            ln : str = str(ln.replace("'args'", '').replace('(', '').replace(')', '').replace('num', '').replace("''", '').replace(' , ,', ''));
            print('ln',ln);
	    #res = self.walkTree(node[1])
	    #print(res)
            #if (node[1][0]) == 'args':
            #   print(len(node[1]))
                #i : int;
                #for i in range(len(node[1])):
                #    print(node[1][i][1])
            #print(node)
            #print(node[0])
            #print(node[1])
            #print(node[1][0])
            #print(node[1][1])
            #print(node[1][1][1])
            #print(node[1][2][1][1])

            '''
            i : int;
            strg : str = '';
            for i in range(len(node[1])):
                try:
                    strg += ('{} '.format(self.env[node[1][i][1]]))
                except LookupError:
                    print("Undefined variable '"+node[1][i][1]+"' found!")
                    return 0
            print(strg)
            '''


            #print(node[1], len(node[1]))
            #print(node[1][1][1])

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    while True:
        try:
            text = input('mini haya > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)
            #parsetree = parser.parse(lexer.tokenize(text))
            #print(parsetree)
