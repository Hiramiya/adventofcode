lines = []

with open('d2/input','r') as f:
    for line in f:
        cleanline = line.rstrip().split()

        lines.append([int(x) for x in cleanline])

total_reports  = len(lines)
safe_reports   = 0
unsafe_reports = 0
safe_enough_reports = 0

def process(l):
    is_increment = False
    report_is_unsafe = False

    if l[1] > l[0]:
        is_increment = True

    for i, _ in enumerate(l):
        if i == len(l)-1:
            continue

        dist = l[i] - l[i+1]

        if l[i] > l[i+1] and is_increment:
            report_is_unsafe = True
        elif l[i] < l[i+1] and not is_increment:
            report_is_unsafe = True
        
        if dist < 0:
            dist = dist * -1

        if dist < 1:
            # print("did not differ by at least 1")
            report_is_unsafe = True
        elif dist > 3:
            # print("differed by more than 3")
            report_is_unsafe = True

    return not report_is_unsafe

# part1
for l in lines:
    if process(l):
        safe_reports += 1

print("Safe:", safe_reports)

# part2
for l in lines:
    if process(l):
        safe_enough_reports += 1
        # print(l, "SAFE")
        continue

    for i, _ in enumerate(l):
        nl = l.copy()
        del(nl[i])
        if process(nl):
            safe_enough_reports += 1
            print(l, "safeish", nl)
            break


print("Safe Enough:", safe_enough_reports)
