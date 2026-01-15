import sys

day_source = '''
from helpers import load_input


input = load_input()
lines = input.split('\\n')
'''[1:]


def create_files():
    global day_source
    args = sys.argv
    if len(args) < 2:
        return

    name = args[1]
    open(name + ' input.txt', 'a').close()
    try:
        with (open(name + '.py', 'x')) as file:
            file.write(day_source)
    except:
        pass

create_files()
