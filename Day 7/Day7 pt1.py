file = open("Tachyon Manifold", "r").readlines()

grid = []
for i, line in enumerate(file):
    new_line = []
    line = line.strip()
    for j, char in enumerate(line):
        if char == "S":
            beams = {(i, j)}
        new_line.append(char)
    grid.append(new_line)

splits = 0
for i in range(len(grid) - 1):
    new_beams = set()
    for beam in beams:
        if grid[beam[0] + 1][beam[1]] == "^":
            splits += 1
            new_beams.add((beam[0] + 1, beam[1] + 1))
            new_beams.add((beam[0] + 1, beam[1] - 1))
        else:
            new_beams.add((beam[0] + 1, beam[1]))
    beams = new_beams

print(splits)