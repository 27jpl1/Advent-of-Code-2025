file = open("Tiles", "r").readlines()

tiles = []
for line in file:
    tiles.append(tuple(map(int, line.strip().split(","))))

largest_area = 0
i = 0
while i < len(tiles):
    j = i + 1
    while j < len(tiles):
        first_x, first_y = tiles[i]
        second_x, second_y = tiles[j]
        area = (abs(first_x - second_x) + 1) * (abs(first_y - second_y) + 1)
        if area > largest_area:
            largest_area = area
        j += 1
    i += 1

print(largest_area)
