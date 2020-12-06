dataarray = []
with open("05/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

# Part One

# highestseat = 0

# for entry in dataarray:
#     rowlo = 0
#     rowhi = 127
#     seatlo = 0
#     seathi = 7
#     for part in entry:
#         if part == "B":
#             rowlo = rowlo + ( (rowhi - rowlo) / 2 )
#         if part == "F":
#             rowhi = rowhi - ( (rowhi - rowlo) / 2 )
#         if part == "R":
#             seatlo = seatlo + ( (seathi - seatlo) / 2 )
#         if part == "L":
#             seathi = seathi - ( (seathi - seatlo) / 2 )
    
#     seatid = int(rowhi) * 8 + int(seathi)
    
#     if seatid > highestseat:
#         highestseat = seatid

# print("Part One:", highestseat)

# Part Two

seatids = []

for entry in dataarray:
    rowlo = 0
    rowhi = 127
    seatlo = 0
    seathi = 7
    for part in entry:
        if part == "B":
            rowlo = rowlo + ( (rowhi - rowlo) / 2 )
        if part == "F":
            rowhi = rowhi - ( (rowhi - rowlo) / 2 )
        if part == "R":
            seatlo = seatlo + ( (seathi - seatlo) / 2 )
        if part == "L":
            seathi = seathi - ( (seathi - seatlo) / 2 )
    
    seatid = int(rowhi) * 8 + int(seathi)
    seatids.append(seatid)

seatids.sort()

for x in range(seatids[0], seatids[-1]+1):
    if x not in seatids:
        missingseat = x

print("Part Two:", missingseat)
