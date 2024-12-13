from math import floor
rules = []
updates = []

with open('d5/input','r') as f:
    for line in f:
        cleanline = line.rstrip()

        if "|" in line:
            rules.append(cleanline)
        if "," in line:
            updates.append([x for x in cleanline.split(",")])

def passes_rules(pages):
    for rule in rules:
        a, b = rule.split("|")
        if a in pages and b in pages: # Both pages from this rule are included
            # print("both pages found for rule", rule)
            if pages.index(a) > pages.index(b):
                return False
    return True

bad_updates = []
mid_total = 0
for pages in updates:
    if passes_rules(pages):
        midnum = int(pages[floor(len(pages)/2)])
        print("picking", midnum)
        mid_total += midnum
    else:
        bad_updates.append(pages)

print("mid sum:", mid_total)

def sort_pages(pages):
    for rule in rules:
        a, b = rule.split("|")
        if a in pages and b in pages: # Both pages from this rule are included
            idx_a = pages.index(a)
            idx_b = pages.index(b)
            if idx_a > idx_b:
                pages.remove(a)
                pages.insert(idx_b,a)
    
    return pages

updated_mid_sum = 0

for updates in bad_updates:
    while not passes_rules(updates):
        sort_pages(updates)

    midnum = int(updates[floor(len(updates)/2)])
    updated_mid_sum += midnum

print("updated midsum:",updated_mid_sum)
