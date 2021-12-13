from collections import defaultdict
from typing import NamedTuple

class Pos(NamedTuple):
    x: int
    y: int

def fold_up(data, pos):
    for coord in data.copy():
        distance = coord.y - pos
        if distance>=0:
            data.remove(coord)
            new_pos = Pos(coord.x, pos - distance)
            data.add(new_pos)

def fold_left(data, pos):
    for coord in data.copy():
        distance = coord.x - pos
        if distance>=0:
            data.remove(coord)
            new_pos = Pos(pos - distance, coord.y)
            data.add(new_pos)

DIRECTIONS = {"y": fold_up, "x": fold_left}

def parse_fold_line(line):
    spec = line.split(" ")[-1]
    dir, pos = spec.split("=")
    pos = int(pos)
    dir = DIRECTIONS[dir]
    return lambda data: dir(data, pos)

def make_grid(data):
    lines = data.strip().split("\n")
    coords = [Pos(*map(int, line.split(","))) for line in lines if "," in line]
    fold_lines = [parse_fold_line(line) for line in lines if "fold" in line]
    grid_as_set = set()
    for coord in coords:
        grid_as_set.add(coord)
    return grid_as_set, fold_lines
    
def doit(data):
    grid_as_set, fold_lines = make_grid(data)
    fold_lines[0](grid_as_set)
    print(len(grid_as_set))
    for fold in fold_lines[1:]:
        fold(grid_as_set)
    pprint(grid_as_set)
    

def pprint(grid_as_set):
    width = max(point.x for point in grid_as_set)
    height = max(point.y for point in grid_as_set)
    for y in range(height+2):
        print()
        for x in range(width+2):
            print("#" if Pos(x,y) in grid_as_set else " ", end="")

    print()


testdata = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

doit(testdata)
doit(open("13.txt").read())