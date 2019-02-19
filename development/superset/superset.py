def helloworld():
    with open('main.cpp', 'a', encoding='utf-8') as f:
        f.write('#include <iostream>\n');
        f.write('using namespace std;\n');
        f.write('\n');
        f.write('main(){\n');
        f.write('cout << "Hello World" << endl;\n');
        f.write('return 0;\n');
        f.write('}\n');
def forloop():
    with open('forloop.cpp', 'a', encoding='utf-8') as f:
        f.write('#include <iostream>\n');
        f.write('using namespace std;\n');
        f.write('\n');
        f.write('main(){\n');
        f.write('for (int a = 10; a < 20; a++){\n');
        f.write('cout << "value of a: " << a << endl;\n')
        f.write('}')
        f.write('return 0;\n');
        f.write('}\n');

forloop()

'''
for( int a = 10; a < 20; a = a + 1 ) {
      cout << "value of a: " << a << endl;
   }
'''
#vars
#for loops
#functions
#ifs
