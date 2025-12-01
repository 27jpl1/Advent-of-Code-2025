file = open("Dial Turns", "r")
turns = []
for line in file.readlines():
    turns.append(line.strip())

dial = 50
count = 0
for turn in turns:
    direction = turn[0]
    movement = int(turn[1:])
    if direction == "L":
        if movement > 100:
            movement = movement % 100
        dial -= movement
        if dial < 0:
            dial += 100
    else:
        dial += movement
        dial = dial % 100
    if dial == 0:
        count += 1
print(count)
