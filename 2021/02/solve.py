dataarray = []
with open("02/input") as f:
    for line in f:
        dataarray.append(line.rstrip())

## Solve for part 1
forward = 0
depth = 0

for entry in dataarray:
  direction,amount = entry.split(' ')
  if direction == 'forward':
    forward += int(amount)
  if direction == 'up':
    depth -= int(amount)
  if direction == 'down':
    depth += int(amount)

print("Part one: ",forward * depth)

## Solve for part 2
forward = 0
depth = 0
aim = 0

for entry in dataarray:
  direction,amount = entry.split(' ')
  if direction == 'forward':
    forward += int(amount)
    depth += (aim * int(amount))
  if direction == 'up':
    aim -= int(amount)
  if direction == 'down':
    aim += int(amount)

print("Part two: ",forward * depth)
