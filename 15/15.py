import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra_path


def neighbours(data, row, column):
    neighbours = []
    if row > 0:
        neighbours.append((row-1, column))
    if row < len(data)-1:
        neighbours.append((row+1, column))
    if column > 0:
        neighbours.append((row, column-1))
    if column < len(data[0])-1:
        neighbours.append((row, column+1))
    return neighbours


def find_lowest_path(rows):
    G = nx.DiGraph()
    width = len(rows[0])
    height = len(rows)
    for rownum, row in enumerate(rows):
        for cellnum, cell in enumerate(row):
            G.add_node((rownum, cellnum))
            for targetrow, targetcol in neighbours(rows, rownum, cellnum):
                G.add_edge((rownum, cellnum), (targetrow, targetcol),
                           weight=rows[targetrow][targetcol])
    print(G)

    path = dijkstra_path(G, (0, 0), (width-1, height-1), weight="weight")
    return sum(rows[row][column] for row, column in path) - rows[0][0]


def parse(data):
    return [[int(cell) for cell in row]for row in data.strip().split("\n")]


def part1(data):
    rows = parse(data)
    return find_lowest_path(rows)


def tile(rows):
    width = len(rows[0])
    height = len(rows)
    full_width = width * 5
    full_height = height * 5
    table = [[None]*full_width for i in range(full_height)]
    for bigrow in range(5):
        for bigcolumn in range(5):
            increment = bigrow + bigcolumn
            for rownum, row in enumerate(rows):
                for columnnum, cell in enumerate(row):
                    new_value = ((cell+increment-1) % 9)+1
                    rowpos = rownum+(bigrow*height)
                    colpos = columnnum+(bigcolumn*width)
                    assert table[rowpos][colpos] is None
                    table[rowpos][colpos] = new_value
    return table



def part2(data):
    rows = parse(data)
    rows = tile(rows)
    return find_lowest_path(rows)


testdata = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

assert part1(testdata) == 40
assert part2(testdata) == 315
realdata = open("15.txt").read()
print(part1(realdata))
print(part2(realdata))
