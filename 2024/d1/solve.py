list1 = []
list2 = []
total_distance = 0

with open('d1/input','r') as f:
    for line in f:
        v1, v2 = line.rstrip().split()
        list1.append(int(v1))
        list2.append(int(v2))

list1 = sorted(list1)
list2 = sorted(list2)

for i, _ in enumerate(list1):
    distance = list1[i] - list2[i]
    if distance < 0:
        distance = distance * -1
    total_distance += distance

print("Distance:", total_distance)

total_similarity = 0

for v in list1:
    num_of_v = 0
    for vv in list2:
        if vv == v:
            num_of_v += 1
    total_similarity += v * num_of_v

print("Similarity:", total_similarity)
