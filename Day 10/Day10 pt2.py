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


#
# total = 0
# for light in lights:
#     print("total = " ,len(lights), "current = ", lights.index(light))
#     presses = 0
#     final_light = list(map(int,light.pop()[1:-1].split(",")))
#     light_len = len(final_light)
#     curr_light = [0] * len(final_light)
#     updated_lights = [(curr_light, 0)]
#     while True:
#         print(presses, len(updated_lights))
#         curr_light, presses = updated_lights.pop(0)
#         if curr_light == final_light:
#             break
#         for move in light:
#             new_light = curr_light.copy()
#             move = list(map(int,move[1:-1].split(",")))
#             for num in move:
#                 new_light[num] = new_light[num] + 1
#             if (new_light, presses + 1) in updated_lights:
#                 pass
#             else:
#                 updated_lights.append((new_light, presses + 1))
#     print("presses", presses)
#     print("list length = ", len(updated_lights))
#     total += presses
#
# print(total, "total")

