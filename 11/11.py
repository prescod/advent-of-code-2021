def neighbours(data, row, column, width, height):
    return [(y,x, data[y][x]) 
        for x in (column-1, column, column+1) 
        for y in (row-1, row, row+1)
        if x>=0 and y>=0 and x<width and y<height and (x,y)!=(column, row)]

def flash(data, row, column, width, height):
    data[row][column] = None
    for row, column, datum in neighbours(data, row, column, width, height):
        if datum!=None:
            data[row][column] += 1
    return data

def iterate(width, height):
    for row in range(height):
        for column in range(width):
            yield row, column

def substep(data, width, height):
    flashes = 0
    for row, column in iterate(width, height):
        if data[row][column] and data[row][column] >= 10:
            flash(data, row, column, width, height)
            flashes += 1
    return flashes

def pprint(data):
    print()
    for row in data:
        print("".join(str(cell) for cell in row))

def step(data, width, height):
    flashes = 0
    new_flashes = True
    for row, column in iterate(width, height):
        data[row][column] += 1
    while new_flashes:
        new_flashes = substep(data, width, height)
        flashes += new_flashes
    for row, column in iterate(width, height):
        if data[row][column] is None:
            data[row][column] = 0

    return flashes

def parse(data):
    return [[int(cell) for cell in row] for row in data.strip().split("\n")]

def doit(data):
    grid = parse(data)
    flashes = 0
    for i in range(0, 10000):
        width = len(grid[0])
        height = len(grid)
        flashes += step(grid, width, height)
        pprint(grid)
        if not any(grid[row][column] for row,column in iterate(width, height)):
            print(i+1)
            break
    pprint(grid)

def test():
    doit(testdata)

testdata = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

def real():
    doit(realdata)

realdata = """2238518614
4552388553
2562121143
2666685337
7575518784
3572534871
8411718283
7742668385
1235133231
2546165345"""

# pprint(flash(parse(testdata), 1,1, 10, 10))
test()
real()
