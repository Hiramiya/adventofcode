dataarray = []
with open("04/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

total_p1 = 0
total_p2 = 0

# Part One

for card in dataarray:
    cardmeta, carddata = card.split(':')
    cardnum = cardmeta.split()[1]

    winning, having = carddata.split('|')
    winnums = winning.split()
    havenums = having.split()

    matches = len(set(winnums) & set(havenums))

    if matches == 0:
        continue

    if matches != 1:
        matches = 1*(2**(matches-1))

    total_p1 += matches

print(total_p1)

# Part Two

def process_card(card):
    global total_p2
    total_p2 += 1
    cardmeta, carddata = card.split(':')
    cardnum = int(cardmeta.split()[1])

    winning, having = carddata.split('|')
    winnums = winning.split()
    havenums = having.split()
    
    matches = len(set(winnums) & set(havenums))

    if matches == 0:
        return

    for i in range(0, matches):
        process_card(dataarray[cardnum+i])

for card in dataarray:
    process_card(card)

print(total_p2)
