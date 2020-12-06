dataarray = []
with open("06/input") as f:
    temp = []
    for line in f:
        if line == "\n" or line == "" or len(line) == 0:
            # If there's a blank line, flatten the list from the multiple lines
            blah = ""
            for thing in temp:
                blah = blah + thing + " "
            dataarray.append(blah.rstrip())
            temp = []
        else:
            # Append each line to a temp var
            temp.append(line.rstrip())
    # At the end of the file, do this again. because apparently python can't detect the end of the file.
    # DAY FOUR SAVES THE DAY
    blah = ""
    for thing in temp:
        blah = blah + thing + " "
    dataarray.append(blah.rstrip())
    temp = []

# Part One

sumcount = 0

for entry in dataarray:
    sumcount += len(set(entry.replace(" ","")))

print("Part One:", sumcount)

# Part Two

sumcount = 0

for entry in dataarray:
    answers = entry.replace(" ","")
    personcount = len(entry.split(" "))
    
    for answer in set(answers):
        if answers.count(answer) == personcount:
            sumcount += 1

print("Part Two:", sumcount)