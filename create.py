import sys

def create_files():
    args = sys.argv
    if len(args) < 2:
        return

    name = args[1]
    open(name + ' input.txt', 'a').close()
    try:
        with (open(name + '.py', 'x')) as file:
            file.write('from helpers import load_input\n\n\ninput = load_input()')
    except:
        pass

create_files()
