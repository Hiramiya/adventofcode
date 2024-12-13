lines = []

with open('d4/input','r') as f:
    for line in f:
        lines.append([x for x in line.rstrip()])

xmas_found = 0

def check_direction(y,x,direction):
    try:
        match direction:
            case 'forward':
                if lines[y][x+1] == "M" and lines[y][x+2] == "A" and lines[y][x+3] == "S":
                    return True
                
            case 'backward':
                if lines[y][x-1] == "M" and lines[y][x-2] == "A" and lines[y][x-3] == "S":
                    return True

            case 'downward':
                if lines[y+1][x] == "M" and lines[y+2][x] == "A" and lines[y+3][x] == "S":
                    return True

            case 'upward':
                if lines[y-1][x] == "M" and lines[y-2][x] == "A" and lines[y-3][x] == "S":
                    return True

            case 'downright':
                if lines[y+1][x+1] == "M" and lines[y+2][x+2] == "A" and lines[y+3][x+3] == "S":
                    return True
                
            case 'upleft':
                if lines[y-1][x-1] == "M" and lines[y-2][x-2] == "A" and lines[y-3][x-3] == "S":
                    return True

            case 'upright':
                if lines[y-1][x+1] == "M" and lines[y-2][x+2] == "A" and lines[y-3][x+3] == "S":
                    return True

            case 'downleft':
                if lines[y+1][x-1] == "M" and lines[y+2][x-2] == "A" and lines[y+3][x-3] == "S":
                    return True

    except IndexError:
        print("!!!THROW!!!")
        pass

    return False


def count_mas(y,x):

    count = 0

    if lines[y-1][x-1] == "M":
        if lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S" and lines[y+1][x+1] == "S":
            count += 1
        if lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M" and lines[y+1][x+1] == "S":
            count += 1

    if lines[y-1][x-1] == "S":
        if lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M" and lines[y+1][x+1] == "M":
            count += 1
        if lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S" and lines[y+1][x+1] == "M":
            count += 1

    return count
            

for y, line in enumerate(lines):
    print(line)
    for x, letter in enumerate(line):
        if letter != "X":
            continue
    
        # directions = ['forward', 'backward', 'upward', 'downward', 'downright', 'upleft', 'upright', 'downleft']
        directions = []
        
        if x > 2:
            directions.append("backward")
        if x < len(line)-2:
            directions.append("forward")
        if y > 2:
            directions.append("upward")
            if x > 2:
                directions.append("upleft")
            if x < len(line)-3:
                directions.append("upright")
        if y < len(lines)-3:
            directions.append("downward")
            if x > 2:
                directions.append("downleft")
            if x < len(line)-3:
                directions.append("downright")

        for direction in directions:
            # print("nope", y, x)
            if check_direction(y,x,direction):
                print("hit", y, x, direction)
                xmas_found += 1

print("XMAS:", xmas_found)

mas_found = 0
for y, line in enumerate(lines):
    print(line)
    for x, letter in enumerate(line):
        if letter != "A":
            continue

        if x < 1 or x > len(line)-2 or y < 1 or y > len(lines)-2:
            continue

        mas_found += count_mas(y,x)

print("X-MAS:", mas_found)
