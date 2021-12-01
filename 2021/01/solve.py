dataarray = []
with open("01/input") as f:
    for line in f:
        dataarray.append(int(line.rstrip()))

## Solve for part 1
# count = 0
# previous = 0
# for entry in dataarray:
#   if entry > previous:
#     count += 1
#   previous = entry
# print(count - 1)

## Solve for part 2
count = 0
previous = 0
previousone = 0
previoustwo = 0
for entry in dataarray:
  value = entry + previousone + previoustwo
  if value > previous and previoustwo > 1:
    count += 1
  previous = value
  previoustwo = previousone
  previousone = entry
print(count - 1)
