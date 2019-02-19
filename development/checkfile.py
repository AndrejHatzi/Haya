import sys
file = sys.argv[1]
print(file)
try:
    with open(file, 'r', encoding="utf-8") as f:
        line : str
        for line in f:
            print(line)
except:
    print('the specified file "{}" was not found!'.format(file))
    
