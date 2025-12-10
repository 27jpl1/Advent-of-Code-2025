from z3 import *

file = open("Lights","r").readlines()

lights = []

for line in file:
    line = line.strip().split()
    line.pop(0)
    lights.append(line)

total = 0
for light in lights:
    final = list(map(int,light[-1][1:-1].split(",")))
    old_buttons = light[:-1]
    buttons = []
    for i, button in enumerate(old_buttons):
       buttons.append(list(map(int,light[i][1:-1].split(","))))

    num_buttons = len(buttons)
    num_lights = len(final)

    button_ints = []
    for i in range(num_buttons):
        button_ints.append(Int(f"button_{i}"))

    solver = Optimize()

    for button_int in button_ints:
        solver.add(button_int >= 0)

    for j in range(num_lights):
        affecting_buttons = []
        for i, button in enumerate(buttons):
            if j in button:
                affecting_buttons.append(i)

        solver.add(sum(button_ints[i] for i in affecting_buttons) == final[j])

    solver.minimize(sum(button_ints))

    if solver.check() != sat:
        print("No solution!")
        continue

    model = solver.model()
    for button_int in button_ints:
        total += model[button_int].as_long()

print(total)