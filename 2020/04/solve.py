dataarray = []
with open("04/input") as f:
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
    # This wasted so much time :'(
    blah = ""
    for thing in temp:
        blah = blah + thing + " "
    dataarray.append(blah.rstrip())
    temp = []

# Part One

validcount = 0

for entry in dataarray:
    line = entry.split(" ")
    if len(line) == 8:
        # Eight fields means everything is there (including cid)
        validcount += 1
        continue
    if len(line) < 7:
        # If there's less than 7 fields, we're missing two, which is bad!
        continue
    parts = 0
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(x in entry for x in required):
        validcount += 1


print("Part One:", validcount)

# Part Two

import re

validcount = 0

for entry in dataarray:
    line = entry.split(" ")
    if len(line) < 7:
        # If there's less than 7 fields, we're missing two, which is bad!
        continue
    parts = 0
    for thing in line:
        # This is messy but I don't care
        item = thing.split(":")[0]
        value = thing.split(":")[1]
        if item == "byr":
            if 1920 <= int(value) <= 2002:
                parts += 1
        if item == "iyr":
            if 2010 <= int(value) <= 2020:
                parts += 1
        if item == "eyr":
            if 2020 <= int(value) <= 2030:
                parts += 1
        if item == "hgt":
            if "in" in value:
                if 59 <= int(value.replace("in","")) <= 76:
                    parts += 1
            if "cm" in value:
                if 150 <= int(value.replace("cm","")) <= 193:
                    parts += 1
        if item == "hcl":
            if re.search("^#[a-f0-9]{6}$",value):
                parts += 1
        if item == "ecl":
            colours = ["amb", "blu", "brn", "grn", "gry", "hzl", "oth"]
            if any(x in value for x in colours):
                parts += 1
        if item == "pid":
            if len(value) == 9:
                parts += 1
    if parts == 7:
        validcount += 1


print("Part Two:", validcount)
