file = open("Batteries", "r").readlines()

batteries = []
for line in file:
    batteries.append(line.strip())

total = 0
for battery in batteries:
    first_best = 0
    second_best = 0
    first_index = 0
    second_index = 0
    for i, char in enumerate(battery):
        if int(char) > first_best and i < len(battery) - 1:
            first_best = int(char)
            first_index = i
    for i, char in enumerate(battery):
        if i > first_index:
            if int(char) > second_best:
                second_best = int(char)
    total += first_best * 10 + second_best
print(total)

