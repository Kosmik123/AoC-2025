from helpers import load_input

input = '''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''[1:-1]


input = load_input()
lines = input.split('\n')

outputs_by_device = dict[str, list[str]]()
for line in lines:
    device, outputs = line.split(':')
    outputs_by_device[device] = []
    for output in outputs.strip().split(' '):
        outputs_by_device[device].append(output.strip())

def ptree(start, tree, indent_width=4):
    def _ptree(start, parent, tree, grandpa=None, indent=""):
        if parent != start:
            if grandpa is None:  # Ask grandpa kids!
                print(parent, end="")
            else:
                print(parent)
        if parent not in tree:
            return
        for child in tree[parent][:-1]:
            print(indent + "├" + "─" * indent_width, end="")
            _ptree(start, child, tree, parent, indent + "│" + " " * 4)
        child = tree[parent][-1]
        print(indent + "└" + "─" * indent_width, end="")
        _ptree(start, child, tree, parent, indent + " " * 5)  # 4 -> 5

    parent = start
    print(start)
    _ptree(start, parent, tree)

ptree('you', outputs_by_device)



ways_to_out_by_device = dict[str, int]()
def get_ways_to_out(device: str):
    global ways_to_out_by_device, outputs_by_device 
    if device in ways_to_out_by_device:
        return ways_to_out_by_device[device] 

    ways_count = 0
    device_outs = outputs_by_device[device]
    for output in device_outs:
        if output == 'out':
            ways_count += 1
        else: 
            ways_count += get_ways_to_out(output)
    
    ways_to_out_by_device[device] = ways_count
    return ways_count

ways_from_you = get_ways_to_out('you')
print(ways_from_you)

