file = open("Rolls", "r").readlines()

rolls = []

for line in file:
    roll = []
    for char in line.strip():
        roll.append(char)
    rolls.append(roll)

count = 0
old_count = 1
directions = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
while count != old_count:
    old_count = count
    row = 0
    while row < len(rolls):
        col = 0
        while col < len(rolls[0]):
            if rolls[row][col] == "@":
                total = 0
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0 <= col + direction[1] < len(rolls) and 0 <= row + direction[0] < len(rolls[0]):
                        if rolls[new_row][new_col] == "@":
                            total += 1
                if total < 4:
                    if rolls[row][col] == "@":
                        rolls[row][col] = "."
                        count += 1
            col += 1
        row += 1
print(count)