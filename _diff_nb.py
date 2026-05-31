import json, sys

def dump(path):
    nb = json.load(open(path))
    out = []
    for i, c in enumerate(nb['cells']):
        out.append(f"---CELL {i} [{c['cell_type']}]---")
        out.append(''.join(c['source']))
    return '\n'.join(out)

for p in sys.argv[1:]:
    print(f"\n==== {p} ====")
    print(dump(p))
