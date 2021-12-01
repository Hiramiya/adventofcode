
dataarray = []
with open("01/input") as f:
    for line in f:
        dataarray.append(int(line.rstrip()))

## Solve for Part 1 (2 values)
for entry in dataarray:
    val = 2020 - entry
    if val in dataarray:
        print(entry * val)

## Solve for Part 2 (3 values)
for entry in dataarray:
    for entryy in dataarray:
        val = 2020 - entry - entryy
        if val in dataarray:
            print(entry * entryy * val)
