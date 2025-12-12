file = open("Presents", "r").readlines()

total = 0
box_areas = [7, 7, 6, 7, 7, 5]
for line in file:
    total_needed_area = 0
    line = line.strip().split()
    box = line[0][:-1].split("x")
    area = int(box[0]) * int(box[1])
    total_boxes = 0
    for i,box in enumerate(line[1:]):
        total_needed_area += box_areas[i] * int(box)
    print(total_needed_area, area)
    if total_needed_area <= area:
        total += 1
print(total)