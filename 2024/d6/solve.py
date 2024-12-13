lines = []

with open('d6/input','r') as f:
    for line in f:
        cleanline = list(line.rstrip())
        lines.append(cleanline)

# Find the starting position
start_pos = []
for i, line in enumerate(lines):
    print(line)
    if "^" in line:
        startchar = line.index("^")
        start_pos = [i, startchar]
        print(line,start_pos)

visited_points = set()
visited_points.add(','.join(map(str,start_pos)))

def check_maze(y,x):
    try:
        match lines[y][x]:
            # Going up
            case "^":
                checkLine = lines[y-1][x]
                lines[y][x] = "."
                if checkLine == ".": # Free space, move
                    y = y-1
                    lines[y][x] = "^"
                elif checkLine == "#": # Space is blocked, move "right"
                    x = x+1
                    lines[y][x] = ">"

            # Going right
            case ">":
                checkLine = lines[y][x+1]
                lines[y][x] = "."
                if checkLine == ".": # Free space, move
                    x = x+1
                    lines[y][x] = ">"
                elif checkLine == "#": # Space is blocked, move "right"
                    y = y+1
                    lines[y][x] = "v"

            # Going down
            case "v":
                checkLine = lines[y+1][x]
                lines[y][x] = "."
                if checkLine == ".": # Free space, move
                    y = y+1
                    lines[y][x] = "v"
                elif checkLine == "#": # Space is blocked, move "right"
                    x = x-1
                    lines[y][x] = "<"

            # Going left
            case "<":
                checkLine = lines[y][x-1]
                lines[y][x] = "."
                if checkLine == ".": # Free space, move
                    x = x - 1
                    lines[y][x] = "<"
                elif checkLine == "#": # Space is blocked, move "right"
                    y = y-1
                    lines[y][x] = "^"
    except IndexError:
        # We're off the map
        x = y = -1
    finally:
        return y,x

off_map = False
y, x = start_pos
while not off_map:
    # Check we're not off the map
    if y < 0 or y > len(lines)-1 or x < 0 or x > len(lines[0])-1:
        off_map = True
        print("Went off the edge")
        break

    print(y,x,lines[y][x])
    for line in lines:
        print("".join(line))

    y, x = check_maze(y,x)
    
    visited_points.add(','.join(map(str,[y,x])))
    print("Visited count:", len(visited_points))
    # sleep(0.2)

print(len(visited_points)-1)


# Part two can go away
