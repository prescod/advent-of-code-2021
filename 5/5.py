from collections import Counter
from itertools import chain
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


def make_point_list(lines, include_diagonals):
    return tuple(chain(*[line.all_points(include_diagonals) for line in lines]))


def count_duplicated_points(lines, include_diagonals):
    points = make_point_list(lines, include_diagonals)
    counters = Counter(points)
    return len([x for x, count in counters.items() if count >= 2])


def find_hotspots(data, include_diagonals):
    lines = parse(data)
    return count_duplicated_points(lines, include_diagonals)


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
