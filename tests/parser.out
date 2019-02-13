Grammar:

Rule 0     S' -> statement
Rule 1     statement -> expr
Rule 2     statement -> var_assign
Rule 3     statement -> NAME ( )
Rule 4     statement -> FUN NAME ( ) : statement
Rule 5     statement -> <empty>
Rule 6     var_assign -> NAME = statement
Rule 7     var_assign -> NAME = STRING
Rule 8     expr -> NUMBER
Rule 9     expr -> NAME
Rule 10    expr -> - expr  [precedence=right, level=3]
Rule 11    expr -> expr / expr  [precedence=left, level=2]
Rule 12    expr -> expr * expr  [precedence=left, level=2]
Rule 13    expr -> expr - expr  [precedence=left, level=1]
Rule 14    expr -> expr + expr  [precedence=left, level=1]

Terminals, with rules where they appear:

(                    : 3 4
)                    : 3 4
*                    : 12
+                    : 14
-                    : 10 13
/                    : 11
:                    : 4
=                    : 6 7
FUN                  : 4
NAME                 : 3 4 6 7 9
NUMBER               : 8
STRING               : 7
error                : 

Nonterminals, with rules where they appear:

expr                 : 1 10 11 11 12 12 13 13 14 14
statement            : 4 6 0
var_assign           : 2


state 0

    (0) S' -> . statement
    (1) statement -> . expr
    (2) statement -> . var_assign
    (3) statement -> . NAME ( )
    (4) statement -> . FUN NAME ( ) : statement
    (5) statement -> .
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    (6) var_assign -> . NAME = statement
    (7) var_assign -> . NAME = STRING
    NAME            shift and go to state 4
    FUN             shift and go to state 5
    $end            reduce using rule 5 (statement -> .)
    NUMBER          shift and go to state 6
    -               shift and go to state 7

    statement                      shift and go to state 1
    expr                           shift and go to state 2
    var_assign                     shift and go to state 3

state 1

    (0) S' -> statement .


state 2

    (1) statement -> expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    $end            reduce using rule 1 (statement -> expr .)
    /               shift and go to state 8
    *               shift and go to state 9
    -               shift and go to state 10
    +               shift and go to state 11


state 3

    (2) statement -> var_assign .
    $end            reduce using rule 2 (statement -> var_assign .)


state 4

    (3) statement -> NAME . ( )
    (9) expr -> NAME .
    (6) var_assign -> NAME . = statement
    (7) var_assign -> NAME . = STRING
    (               shift and go to state 12
    /               reduce using rule 9 (expr -> NAME .)
    *               reduce using rule 9 (expr -> NAME .)
    -               reduce using rule 9 (expr -> NAME .)
    +               reduce using rule 9 (expr -> NAME .)
    $end            reduce using rule 9 (expr -> NAME .)
    =               shift and go to state 13


state 5

    (4) statement -> FUN . NAME ( ) : statement
    NAME            shift and go to state 14


state 6

    (8) expr -> NUMBER .
    /               reduce using rule 8 (expr -> NUMBER .)
    *               reduce using rule 8 (expr -> NUMBER .)
    -               reduce using rule 8 (expr -> NUMBER .)
    +               reduce using rule 8 (expr -> NUMBER .)
    $end            reduce using rule 8 (expr -> NUMBER .)


state 7

    (10) expr -> - . expr
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    NUMBER          shift and go to state 6
    NAME            shift and go to state 16
    -               shift and go to state 7

    expr                           shift and go to state 15

state 8

    (11) expr -> expr / . expr
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    NUMBER          shift and go to state 6
    NAME            shift and go to state 16
    -               shift and go to state 7

    expr                           shift and go to state 17

state 9

    (12) expr -> expr * . expr
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    NUMBER          shift and go to state 6
    NAME            shift and go to state 16
    -               shift and go to state 7

    expr                           shift and go to state 18

state 10

    (13) expr -> expr - . expr
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    NUMBER          shift and go to state 6
    NAME            shift and go to state 16
    -               shift and go to state 7

    expr                           shift and go to state 19

state 11

    (14) expr -> expr + . expr
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    NUMBER          shift and go to state 6
    NAME            shift and go to state 16
    -               shift and go to state 7

    expr                           shift and go to state 20

state 12

    (3) statement -> NAME ( . )
    )               shift and go to state 21


state 13

    (6) var_assign -> NAME = . statement
    (7) var_assign -> NAME = . STRING
    (1) statement -> . expr
    (2) statement -> . var_assign
    (3) statement -> . NAME ( )
    (4) statement -> . FUN NAME ( ) : statement
    (5) statement -> .
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    (6) var_assign -> . NAME = statement
    (7) var_assign -> . NAME = STRING
    STRING          shift and go to state 23
    NAME            shift and go to state 4
    FUN             shift and go to state 5
    $end            reduce using rule 5 (statement -> .)
    NUMBER          shift and go to state 6
    -               shift and go to state 7

    statement                      shift and go to state 22
    expr                           shift and go to state 2
    var_assign                     shift and go to state 3

state 14

    (4) statement -> FUN NAME . ( ) : statement
    (               shift and go to state 24


state 15

    (10) expr -> - expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    /               reduce using rule 10 (expr -> - expr .)
    *               reduce using rule 10 (expr -> - expr .)
    -               reduce using rule 10 (expr -> - expr .)
    +               reduce using rule 10 (expr -> - expr .)
    $end            reduce using rule 10 (expr -> - expr .)


state 16

    (9) expr -> NAME .
    /               reduce using rule 9 (expr -> NAME .)
    *               reduce using rule 9 (expr -> NAME .)
    -               reduce using rule 9 (expr -> NAME .)
    +               reduce using rule 9 (expr -> NAME .)
    $end            reduce using rule 9 (expr -> NAME .)


state 17

    (11) expr -> expr / expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    /               reduce using rule 11 (expr -> expr / expr .)
    *               reduce using rule 11 (expr -> expr / expr .)
    -               reduce using rule 11 (expr -> expr / expr .)
    +               reduce using rule 11 (expr -> expr / expr .)
    $end            reduce using rule 11 (expr -> expr / expr .)


state 18

    (12) expr -> expr * expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    /               reduce using rule 12 (expr -> expr * expr .)
    *               reduce using rule 12 (expr -> expr * expr .)
    -               reduce using rule 12 (expr -> expr * expr .)
    +               reduce using rule 12 (expr -> expr * expr .)
    $end            reduce using rule 12 (expr -> expr * expr .)


state 19

    (13) expr -> expr - expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    -               reduce using rule 13 (expr -> expr - expr .)
    +               reduce using rule 13 (expr -> expr - expr .)
    $end            reduce using rule 13 (expr -> expr - expr .)
    /               shift and go to state 8
    *               shift and go to state 9


state 20

    (14) expr -> expr + expr .
    (11) expr -> expr . / expr
    (12) expr -> expr . * expr
    (13) expr -> expr . - expr
    (14) expr -> expr . + expr
    -               reduce using rule 14 (expr -> expr + expr .)
    +               reduce using rule 14 (expr -> expr + expr .)
    $end            reduce using rule 14 (expr -> expr + expr .)
    /               shift and go to state 8
    *               shift and go to state 9


state 21

    (3) statement -> NAME ( ) .
    $end            reduce using rule 3 (statement -> NAME ( ) .)


state 22

    (6) var_assign -> NAME = statement .
    $end            reduce using rule 6 (var_assign -> NAME = statement .)


state 23

    (7) var_assign -> NAME = STRING .
    $end            reduce using rule 7 (var_assign -> NAME = STRING .)


state 24

    (4) statement -> FUN NAME ( . ) : statement
    )               shift and go to state 25


state 25

    (4) statement -> FUN NAME ( ) . : statement
    :               shift and go to state 26


state 26

    (4) statement -> FUN NAME ( ) : . statement
    (1) statement -> . expr
    (2) statement -> . var_assign
    (3) statement -> . NAME ( )
    (4) statement -> . FUN NAME ( ) : statement
    (5) statement -> .
    (8) expr -> . NUMBER
    (9) expr -> . NAME
    (10) expr -> . - expr
    (11) expr -> . expr / expr
    (12) expr -> . expr * expr
    (13) expr -> . expr - expr
    (14) expr -> . expr + expr
    (6) var_assign -> . NAME = statement
    (7) var_assign -> . NAME = STRING
    NAME            shift and go to state 4
    FUN             shift and go to state 5
    $end            reduce using rule 5 (statement -> .)
    NUMBER          shift and go to state 6
    -               shift and go to state 7

    statement                      shift and go to state 27
    expr                           shift and go to state 2
    var_assign                     shift and go to state 3

state 27

    (4) statement -> FUN NAME ( ) : statement .
    $end            reduce using rule 4 (statement -> FUN NAME ( ) : statement .)
