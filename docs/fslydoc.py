# calclex.py

#Multiline <= neste script
#
#

from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, LPAREN, RPAREN }

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    # Regular expression rules for tokens
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'

    #para contar as linhas
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
        print(self.lineno, t.value)

if __name__ == '__main__':
    #data = 'x = 3 + 42 * (s - t)'
    #data = '''x = 3 + 42
    #            * (s    # This is a comment
    #                - t)'''
    with open('test.ts', 'r') as f:
        data=f.read()
    print(data)
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
