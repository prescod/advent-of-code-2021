from functools import reduce
from typing import NamedTuple


class Coord(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    frm: Coord
    to: Coord

    def all_points(self, include_diagonals):
        if self.frm.x == self.to.x:
            small = min([self.frm.y, self.to.y])
            big = max([self.frm.y, self.to.y])
            return [Coord(self.frm.x, y) for y in range(small, big + 1)]
        elif self.frm.y == self.to.y:
            small = min([self.frm.x, self.to.x])
            big = max([self.frm.x, self.to.x])
            return [Coord(x, self.frm.y) for x in range(small, big + 1)]
        elif include_diagonals:
            frm, to = sorted([self.frm, self.to])
            if frm.y > to.y:
                ys = range(frm.y, to.y - 1, -1)
            else:
                assert frm.y != to.y
                ys = range(frm.y, to.y + 1, 1)
            return [Coord(x, y) for x, y in zip(range(frm.x, to.x + 1), ys)]
        else:
            return []


class Map(NamedTuple):
    cells: list

    def display(self):
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    cell = "."
                print(cell, end="")
            print()


def parse(data):
    data = data.strip()

    def as_lines(s: str):
        a, b = s.split("->")
        a, b = a.strip(), b.strip()
        frm, to = a.split(","), b.split(",")
        frm, to = Coord(*[int(x) for x in frm]), Coord(*[int(x) for x in to])
        return Line(frm, to)

    lines = (as_lines(line) for line in data.split("\n"))
    return tuple(lines)


def make_map(line_specs, include_diagonals):
    mapwidth = max(max(line.frm.x, line.to.x) for line in line_specs) + 1
    mapheight = max(max(line.frm.y, line.to.y) for line in line_specs) + 1
    map = [[0 for cell in range(mapwidth)] for row in range(mapheight)]
    add_lines(map, line_specs, include_diagonals)
    return Map(map)


def add_lines(map, lines, include_diagonals):
    return reduce(lambda map, line: add_line(map, line, include_diagonals), lines, map)


def add_line(map, line, include_diagonals):
    for coord in line.all_points(include_diagonals):
        # this assignment could be replaced with a persistent hashmap
        # in a functional language, but Python would need a library
        # for that, so I'm faking it
        map[coord.y][coord.x] += 1
    return map


def count_hotspots(map):
    return sum([sum(1 for cell in row if cell >= 2) for row in map.cells])


def find_hotspots(data, include_diagonals):
    return count_hotspots(make_map(parse(data), include_diagonals))


def test():
    return find_hotspots(testdata, include_diagonals=False), find_hotspots(
        testdata, include_diagonals=True
    )


def real():
    return find_hotspots(open("5.txt").read(), include_diagonals=False), find_hotspots(
        open("5.txt").read(), include_diagonals=True
    )


testdata = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
print(test())
print(real())
