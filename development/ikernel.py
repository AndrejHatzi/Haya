'''
<?
a : str = '1';
b : str = '3';
print (a+b);
for i in range(10):
    print(i);
?>
'''
import sys;
def exec_function(user_input):
    try:
        compile(user_input, '<stdin>', 'eval');
    except SyntaxError:
        return exec;
    return eval;

def auto_exec() -> None:
    script_name : str = str(sys.argv[0]);
    embedded_script : str = '';
    with open(script_name, 'r') as f:
        script = f.readlines();
    line : int;
    for line in range(len(script)):
        if script[line] == '<?\n':
            l : int;
            for l in range(line+1, len(script)):
                if (script[l] == '?>\n'):
                    break;
                else:
                    embedded_script += script[l];
    i = exec(embedded_script);
    return i;
