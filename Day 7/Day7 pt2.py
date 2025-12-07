from functools import cache

file = open("Tachyon Manifold", "r").readlines()

grid = []
for i, line in enumerate(file):
    new_line = []
    line = line.strip()
    for j, char in enumerate(line):
        if char == "S":
            r, c = i, j
        new_line.append(char)
    grid.append(new_line)

@cache
def solve(row, col):
    if row >= len(grid):
        return 1
    elif grid[row][col] == "." or grid[row][col] == "S":
        return solve(row + 1, col)
    else:
        return solve(row, col - 1) + solve(row, col + 1)

print(solve(r, c))
