lines = []

with open('d7/input','r') as f:
    for line in f:
        lines.append(line.rstrip())

def gen_opers(values,opers):
    if len(values) <= 1:
        yield values[0]
        return
    for x in opers:
        for y in gen_opers(values[1:],opers):
            yield values[0] + " " + x + " " + y


p1_total = 0
p2_total = 0
for line in lines:
    target, values = line.split(': ')
    target = int(target)
    values = [i for i in values.split()]
    print(target,values)

    # Part 1
    for x in gen_opers(values,["+", "*"]):
        print(x)
        xlist = x.split()
        result = int(xlist[0])
        # print(xlist[0])
        for i in range(1,len(xlist),2):
            # print(xlist[i], xlist[i+1])
            if xlist[i] == "+":
                result += int(xlist[i+1])
            elif xlist[i] == "*":
                result *= int(xlist[i+1])
        print(result)
        if result == target:
            p1_total += target
            break


    # Part 2
    for x in gen_opers(values,["+", "*", "||"]):
        print(x)
        xlist = x.split()
        result = int(xlist[0])
        # print(xlist[0])

        for i in range(1,len(xlist),2):
            # print(xlist[i], xlist[i+1])
            if xlist[i] == "+":
                result += int(xlist[i+1])
            elif xlist[i] == "*":
                result *= int(xlist[i+1])
            elif xlist[i] == "||":
                result = int(str(result) + xlist[i+1])
        print(result)
        if result == target:
            p2_total += target
            break
        if result > target:
            continue


print("p1:", p1_total, "p2:", p2_total)
