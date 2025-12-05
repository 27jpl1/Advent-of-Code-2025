file = open("Food", "r").readlines()

ranges = []
ids = []
in_ranges = True
for line in file:
    line = line.strip()
    if line == "":
        in_ranges = False
    elif in_ranges:
        ranges.append(line.split("-"))
    else:
        ids.append(int(line))

total = 0
for id in ids:
    for range in ranges:
        if int(range[0]) <= id <= int(range[1]):
            total += 1
            break

print(total)