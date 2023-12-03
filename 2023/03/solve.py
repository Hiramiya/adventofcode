dataarray = []
with open("03/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

SYMBOLS = ['#', '$', '@', '%', '/', '*', '&', '=', '-', '+']
MAX_X = len(dataarray[0])-1
MAX_Y = len(dataarray)-1

# Part One

total_p1 = 0
symbol_positions = []

for i, value in enumerate(dataarray):
    for j, character in enumerate(value):
        if character in SYMBOLS:
            symbol_positions.append([i, j])

# y = line, x = character
for symy, symx in symbol_positions:
    check_spaces = [
        [max(0, symx-1), max(0, symy-1)],     [symx, max(0, symy-1)],     [min(MAX_X, symx+1), max(0, symy-1)],
        [max(0, symx-1), symy],                                           [min(MAX_X, symx+1), symy],
        [max(0, symx-1), min(MAX_Y, symy+1)], [symx, min(MAX_Y, symy+1)], [min(MAX_X, symx+1), min(MAX_Y, symy+1)]
    ]
    # strongly assuming the same number doesn't show up twice by a symbol
    nums_around_this_symbol = set()
    for x,y in check_spaces:
        if dataarray[y][x].isdigit():
            # Find the start of the number
            i = 0
            while dataarray[y][x-i].isdigit():
                first_x_pos = x-i
                i += 1
            # Find the rest of the number
            i = 0
            numstr = ''
            while first_x_pos+i <= MAX_X and dataarray[y][first_x_pos+i].isdigit():
                numstr += dataarray[y][first_x_pos+i]
                i +=1
            # Add it to our optimistic set
            nums_around_this_symbol.add(int(numstr))

    for val in nums_around_this_symbol:
        total_p1 += val

print(total_p1)

# Part Two

total_p2 = 0
symbol_positions = []

for i, value in enumerate(dataarray):
    for j, character in enumerate(value):
        if character in '*':
            symbol_positions.append([i, j])

# y = line, x = character
for symy, symx in symbol_positions:
    check_spaces = [
        [max(0, symx-1), max(0, symy-1)],     [symx, max(0, symy-1)],     [min(MAX_X, symx+1), max(0, symy-1)],
        [max(0, symx-1), symy],                                           [min(MAX_X, symx+1), symy],
        [max(0, symx-1), min(MAX_Y, symy+1)], [symx, min(MAX_Y, symy+1)], [min(MAX_X, symx+1), min(MAX_Y, symy+1)]
    ]
    # strongly assuming the same number doesn't show up twice by a symbol
    nums_around_this_symbol = set()
    for x,y in check_spaces:
        if dataarray[y][x].isdigit():
            # Find the start of the number
            i = 0
            while dataarray[y][x-i].isdigit():
                first_x_pos = x-i
                i += 1
            # Find the rest of the number
            i = 0
            numstr = ''
            while first_x_pos+i <= MAX_X and dataarray[y][first_x_pos+i].isdigit():
                numstr += dataarray[y][first_x_pos+i]
                i +=1
            # Add it to our optimistic set
            nums_around_this_symbol.add(int(numstr))

    if len(nums_around_this_symbol) == 2:
        # Can't sub a set, but can sub a list
        nums = list(nums_around_this_symbol)
        res = nums[0] * nums[1]
        total_p2 += res

print(total_p2)
