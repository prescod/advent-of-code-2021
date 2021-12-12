from typing import NamedTuple
from collections import defaultdict

class Tunnel(NamedTuple):
    frm: str
    to: str

def find_all_paths_for_maze(maze, allow_double_backs):
    return find_all_paths(maze, ("start",), allow_double_backs)

def is_large(pathname):
    return "A" <= pathname[0] <= "Z"

def find_all_paths(maze, path, allow_double_backs):
    start = path[-1]
    for p in maze[start]:
        longer_path = path + (p,)
        if p == "end":
            yield longer_path
        elif is_large(p) or p not in path:
            yield from find_all_paths(maze, longer_path, allow_double_backs)
        elif allow_double_backs and p!="start":
            yield from find_all_paths(maze, longer_path, False)


def doit(data, allow_double_backs):
    rows =  data.strip().split("\n")
    tunnels = [Tunnel(*row.split("-")) for row in rows]
    maze = defaultdict(list)
    for tunnel in tunnels:
        maze[tunnel.frm].append(tunnel.to)
        maze[tunnel.to].append(tunnel.frm)
    all_paths = list(find_all_paths_for_maze(maze, allow_double_backs))
    print(len(all_paths))

def test():
    doit(testdata, False)
    doit(testdata, True)


testdata = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""



realdata = """
ln-nr
ln-wy
fl-XI
qc-start
qq-wy
qc-ln
ZD-nr
qc-YN
XI-wy
ln-qq
ln-XI
YN-start
qq-XI
nr-XI
start-qq
qq-qc
end-XI
qq-YN
ln-YN
end-wy
qc-nr
end-nr"""

test()
doit(realdata, False)
doit(realdata, True)