dataarray = []
with open("03/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

width = len(dataarray[0])

# Part One

treecount = 0

# We start at the top-left
posleft = 0
linenum = 0

for entry in dataarray:
    linenum += 1 # We're interested in the value on the next line
    posleft += 3  # Move across 3 spaces
    try:
        spot = dataarray[linenum][posleft % width]
    except:
        print("end of the road")
        break
    print(linenum, posleft, spot)
    if spot == "#":
        treecount += 1

print("Part One:", treecount)

# Part Two

treecount = 0
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

trees = []
for slope in slopes:
    posleft = 0
    linenum = 0
    slopetrees = 0
    for entry in dataarray:
        linenum += slope[1] # Down second value
        posleft += slope[0] # Right first value
        try:
            spot = dataarray[linenum][posleft % width]
        except:
            break
        if spot == "#":
            slopetrees += 1

    trees.append(slopetrees)

treecount = 1 # Multiplication!
for tree in trees:
    treecount = treecount * tree

print("Part Two:", treecount)