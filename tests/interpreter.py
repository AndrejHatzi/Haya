from sly import Lexer
from sly import Parser
import sys
#--------------------------
# While Loop
# Del Var
# Print stmt
# EQEQ, LEQ
#--------------------------
class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, FOR, PRINT, CREATEFILE, WRITE, EQEQ, TO}
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', ':', '.'}

    # Define tokens
    IF = r'if'
    #FUN = r'function'
    FOR = r'for'
    TO = r','
    PRINT = r'print'
    CREATEFILE = r'createfile'
    WRITE = 'write'
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

    #fzr update de syntax
    @_('NAME "(" ")" ":" statement')
    def statement(self, p):
        return ('fun_def', p.NAME, p.statement)

    @_('FOR "(" var_assign TO expr ")" ":" statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_assign, p.expr), p.statement)

    @_('IF "(" condition ")" ":" statement')
    def statement(self, p):
        return ('if_stmt', p.condition, p.statement)

    @_('NAME "(" ")"')
    def statement(self, p):
        return ('fun_call', p.NAME)

    @_('var_assign')
    def statement(self, p):
        return p.var_assign

    @_('NAME "=" STRING')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.STRING)

    @_('NAME "=" statement')
    def var_assign(self, p):
        return ('var_assign', p.NAME, p.statement)

    @_('PRINT "(" statement ")"')
    def statement(self, p):
        return ('print_stmt', p.statement)

    @_('PRINT "(" STRING ")"')
    def statement(self, p):
        return ('print_stmt_string' , p.STRING)

    @_('CREATEFILE "(" STRING ")"')
    def statement(self, p):
        return ('createfile_stmt', p.STRING)

    @_('STRING "." WRITE "(" STRING ")"')
    def statement(self, p):
        return ('add_to_file_stmt', p.STRING0 ,p.STRING1)

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

    @_('expr EQEQ expr')
    def condition(self, p):
        return ('condition_eqeq', p.expr0, p.expr1)

    @_('"-" expr %prec UMINUS')
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
        #print(env)
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
                return self.walkTree(node[1][1])

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

        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

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

                #searches for the var in the env and gets it's value
                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count+1, loop_limit+1):
                    res = self.walkTree(node[2])
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]

        if node[0] == 'for_loop_setup':
            return (self.walkTree(node[1]), self.walkTree(node[2]))

        if node[0] == 'print_stmt':
            res = self.walkTree(node[1])
            print(res)

        if node[0] == 'print_stmt_string':
            res = self.walkTree(node[1][1:-1])
            print(res)

        if node[0] == 'createfile_stmt':
            file : str = self.walkTree(node[1][1:-1])
            with open(file, 'a') as f:
                pass

        #node 1 2
        if node[0] == 'write_to_file_stmt':
            print(node[2])
            try:
                file : str = self.walkTree(node[1][1:-1])
                with open(file, 'w') as f:
                    f.write(self.walkTree(node[2][1:-1]))
            except LookupError:
                print("file or dir '"+node[1][1:-1]+"' not found!")
                return 0

if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    env = {}
    try:
        file : str  = sys.argv[1]
        try:
            with open(file, 'r', encoding="utf-8") as f:
                line : str
                for line in f:
                    try:
                        text = line
                    except EOFError:
                        break
                    if text:
                        tree = parser.parse(lexer.tokenize(text))
                        BasicExecute(tree, env)
        except:
            print('the specified file "{}" was not found!'.format(file))
    except:

        while True:
            try:
                text = input('haya development edition > ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                BasicExecute(tree, env)
                #parsetree = parser.parse(lexer.tokenize(text))
                #print(parsetree)
