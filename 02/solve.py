dataarray = []
with open("02/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

validcount = 0

for entry in dataarray:
    e = entry.split(":", 2)
    txtpass = e[1].split(" ")[1]
    txtchar = e[0].split(" ")[1]
    txtsize = e[0].split(" ")[0].split("-")

    i = 0
    for char in txtpass:
        if char == txtchar:
            i += 1
    
    if int(txtsize[0]) <= i <= int(txtsize[1]):
        validcount += 1

print("Part One:", validcount)

validcount = 0

for entry in dataarray:
    e = entry.split(":", 2)
    txtpass = e[1].split(" ")[1]
    txtchar = e[0].split(" ")[1]
    txtsize = e[0].split(" ")[0].split("-")

    i = 0
    if txtpass[int(txtsize[0])-1] == txtchar:
        i += 1
    if txtpass[int(txtsize[1])-1] == txtchar:
        i += 1
    if i == 1:
        validcount += 1

print("Part Two:", validcount)
