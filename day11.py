from helpers import load_input

input = '''
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
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



ways_to_destination = dict[(str, str), int]()
def get_ways_to_out(in_device: str, out_device: str = 'out'):
    if in_device == 'out':
        return 0
    
    global ways_to_destination, outputs_by_device 

    key = (in_device, out_device) 
    if key in ways_to_destination:
        return ways_to_destination[key] 

    ways_count = 0
    device_outs = outputs_by_device[in_device]
    for output in device_outs:
        if output == out_device:
            ways_count += 1
        else: 
            ways_count += get_ways_to_out(output, out_device)
    
    ways_to_destination[key] = ways_count
    return ways_count

ways_from_you = get_ways_to_out('svr', 'fft')
print(ways_from_you)

svr_to_fft = get_ways_to_out('svr', 'fft')
fft_to_dac = get_ways_to_out('fft', 'dac')
dac_to_out = get_ways_to_out('dac', 'out')
svr_to_fft_to_dac_to_out = svr_to_fft * fft_to_dac * dac_to_out

svr_to_dac = get_ways_to_out('svr', 'dac')
dac_to_fft = get_ways_to_out('dac', 'fft')
fft_to_out= get_ways_to_out('fft', 'out')
svr_to_dac_to_fft_to_out = svr_to_dac * dac_to_fft * fft_to_out
print ("fft first:", svr_to_fft_to_dac_to_out)
print ("dac first:", svr_to_dac_to_fft_to_out)

total = svr_to_dac_to_fft_to_out + svr_to_fft_to_dac_to_out 
print(total)