from functools import cache

file = open("Devices", "r").readlines()

devices = {}
for line in file:
    line = line.strip().split()
    devices[line[0][:-1]] = line[1:]

@cache
def find_path(point, fft, dac):
    if point == "out":
        if fft and dac:
            return 1
        else:
            return 0
    else:
        if point == "fft":
            fft = True
        if point == "dac":
           dac = True
        total = 0
        for next_point in devices[point]:
            total += find_path(next_point, fft, dac)

        return total

print(find_path("svr", False, False))