file = open("Dial Turns", "r")
turns = []
for line in file.readlines():
    turns.append(line.strip())

dial = 50
count = 0
for turn in turns:
    direction = turn[0]
    movement = int(turn[1:])
    while movement > 0:
        if direction == "L":
            if dial == 0:
                dial = 99
            else:
                dial -= 1
            movement -= 1
        elif direction == "R":
            if dial == 99:
                dial = 0
            else:
                dial += 1
            movement -= 1
        if dial == 0:
            count += 1
print(count)
