dataarray = []
with open("01/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

total_sum_p1 = 0
total_sum_p2 = 0

# Part One
for item in dataarray:
    # Make a new string of just the numbers
    item_nums = ''.join(filter(lambda x: x.isdigit(), item))
    number = f'{item_nums[0]}{item_nums[-1]}'
    total_sum_p1 += int(number)
print(total_sum_p1)

# Part Two

for item in dataarray:
    # Add the number in but don't clobber the word, prevent breaking
    # things like fiveightwone
    item = item.replace('one', 'one1one')
    item = item.replace('two', 'two2two')
    item = item.replace('three', 'three3three')
    item = item.replace('four', 'four4four')
    item = item.replace('five', 'five5five')
    item = item.replace('six', 'six6six')
    item = item.replace('seven', 'seven7seven')
    item = item.replace('eight', 'eight8eight')
    item = item.replace('nine', 'nine9nine')
    # Then do the same as part one since we have real digits
    item_nums = ''.join(filter(lambda x: x.isdigit(), item))
    number = f'{item_nums[0]}{item_nums[-1]}'
    total_sum_p2 += int(number)

print(total_sum_p2)
