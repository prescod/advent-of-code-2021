from functools import reduce
from itertools import chain, tee
from typing import NamedTuple


class Board(NamedTuple):
    cells: tuple
    winning_call: int = None

    @property
    def won(self):
        return self.winning_call is not None


class Cell(NamedTuple):
    number: int
    marked: bool


class Boards(NamedTuple):
    winning_boards: list
    unfinished_boards: list


def parse_board(board):
    cells = (
        (Cell(int(cell), False) for cell in row.split(" ") if cell)
        for row in board.split("\n")
    )

    return Board(cells=cells)


def parse(data):
    parts = data.split("\n\n")
    calls, *boards = parts
    calls = (int(call) for call in calls.split(","))
    boards = (parse_board(board) for board in boards)
    return (calls, boards)


def mark_cells(call, board):
    def new_cell(cell):
        matches_call = cell.number == call
        return Cell(cell.number, cell.marked or matches_call)

    return tuple(tuple(new_cell(cell) for cell in row) for row in board)


def bingo(board) -> bool:
    def complete(cells):
        return all(cell.marked for cell in cells)

    def column(colnum, board):
        return (row[colnum] for row in board)

    rows = (row for row in board)

    columns = (column(colnum, board) for colnum in range(5))

    return any(complete(line) for line in chain(rows, columns))


def update_and_check_board(call, board):
    assert not board.won
    cells = mark_cells(call, board.cells)
    won = bingo(cells)
    return Board(cells=cells, winning_call=call if won else None)


def last(iterator):
    return reduce(lambda x, y: y, iterator)


def find_winning_board(calls, boards):
    boards = Boards(winning_boards=(), unfinished_boards=boards)

    # for call in calls:
    boards = reduce(update_boards, calls, boards)

    winning_board = next(boards.winning_boards)
    losing_board = last(boards.winning_boards)
    return winning_board, losing_board


def update_boards(boards, call) -> Boards:
    updated_boards = tuple(
        update_and_check_board(call, board) for board in boards.unfinished_boards
    )

    t1, t2 = tee(updated_boards)
    winning_boards = (board for board in updated_boards if board.won)

    unfinished_boards = (board for board in updated_boards if not board.won)

    return Boards(chain(boards.winning_boards, winning_boards), unfinished_boards)


def cells_in_board(board):
    for row in board:
        for cell in row:
            yield cell


def find_score(board, last_number_called):
    total = sum((cell.number for cell in cells_in_board(board) if not cell.marked))
    return total * last_number_called


def game(data):
    calls, boards = parse(data)
    chicken_dinner, take_the_L = find_winning_board(calls, boards)

    return find_score(*chicken_dinner), find_score(*take_the_L)


def test():
    assert game(testdata) == (4512, 1924)


def real():
    ret = game(open("4.txt").read())
    print(ret)
    assert ret == (21607, 19012)
    return ret


testdata = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

test()
real()
