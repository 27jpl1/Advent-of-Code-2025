import sys

file = open("Food", "r").readlines()

ranges = []
for line in file:
    line = line.strip()
    if line == "":
        break
    else:
        ranges.append(line.split("-"))

made_change = True
while made_change:
    if len(ranges) == 0:
        sys.exit()
    break_both = False
    i = 0
    while i < len(ranges):
        range_1 = ranges[i]
        j = i + 1
        while j < len(ranges):
            range_2 = ranges[j]
            start_1 = int(range_1[0])
            end_1 = int(range_1[1])
            start_2 = int(range_2[0])
            end_2 = int(range_2[1])
            if end_1 < start_2:
                pass
            elif end_2 < start_1:
                pass
            elif start_1 <= start_2 and end_1 >= end_2:
                ranges.remove(range_2)
                break_both = True
                break
            elif start_1 >= start_2 and end_1 <= end_2:
                ranges.remove(range_1)
                break_both = True
                break
            elif end_1 >= start_2 >= start_1:
                ranges.remove(range_1)
                ranges.remove(range_2)
                ranges.append([range_1[0], range_2[1]])
                break_both = True
                break
            elif end_2 >= start_1 >= start_2:
                ranges.remove(range_1)
                ranges.remove(range_2)
                ranges.append([range_2[0], range_1[1]])
                break_both = True
                break
            else:
                print("this breaks")
                sys.exit()
            j += 1
        if break_both:
            break
        i += 1
    if not break_both:
        made_change = False

total = 0
for range in ranges:
    total += int(range[1]) - int(range[0]) + 1
print(total)
