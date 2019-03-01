import re;
args : str = "('args', ('num', 1), ('args', ('num', 2), ('args', ('num', 3), ('args', ('num', 4), ('args', ('num', 5), ('num', 6))))))";
print(type(args));

txt : str = "The rain in Spain";
x : list = re.findall("^The.*Spain$", txt);

aa : str = '';
y : list = re.findall("\('num', .*?\)", args);
print(y);
i : int;
for i in range(len(y)):
    v : int = y[i].index(',');
    p : int = y[i].index(')');
    aa += '{} '.format(y[i][v+2 : p]);

print(aa);
print(type(x), x);
