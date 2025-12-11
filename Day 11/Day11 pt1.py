from collections import deque

file = open("Devices", "r").readlines()

devices = {}
for line in file:
    line = line.strip().split()
    devices[line[0][:-1]] = line[1:]

total = 0
bfs = deque()
bfs.append("you")
while bfs:
    current_loc = bfs.popleft()
    if current_loc == "out":
        total += 1
    else:
        for connection in devices[current_loc]:
            bfs.append(connection)

print(total)