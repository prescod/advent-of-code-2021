from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int


def up(pos, amount):
    return Position(pos.x, pos.y - amount)


def down(pos, amount):
    return Position(pos.x, pos.y + amount)


def forward(pos, amount):
    return Position(pos.x + amount, pos.y)


MOVES = {"up": up, "down": down, "forward": forward}


def split(line):
    direction, value = line.split()

    return MOVES[direction], int(value)


def doit(lines):
    moves_and_amounts = [split(line) for line in lines]
    pos = Position(0, 0)
    for move, amount in moves_and_amounts:
        pos = move(pos, amount)
    return pos.x * pos.y


def test():
    testdata = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    return doit(testdata)


def real():
    with open("2.txt") as f:
        return doit(f)


print(test())
print(real())
