file = open("Lights","r").readlines()

lights = []

for line in file:
    line = line.strip().split()
    line.pop()
    lights.append(line)

total = 0
for light in lights:
    presses = 0
    final_light = light.pop(0)
    light_len = len(final_light)
    curr_light = "[" + "." * (light_len - 2) + "]"
    updated_lights = [(curr_light, 0)]
    while True:
        curr_light, presses = updated_lights.pop(0)
        if curr_light == final_light:
            break
        for move in light:
            new_light = curr_light
            move = list(map(int,move[1:-1].split(",")))
            for num in move:
                if new_light[num + 1] == ".":
                    new_light = new_light[:num + 1] + "#" + new_light[num + 2:]
                else:
                    new_light = new_light[:num + 1] + "." + new_light[num + 2:]
            if (new_light, presses + 1) in updated_lights:
                pass
            else:
                updated_lights.append((new_light, presses + 1))
    total += presses

print(total)

