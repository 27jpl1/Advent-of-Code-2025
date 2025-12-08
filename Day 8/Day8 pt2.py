import heapq
import math

file = open("Junction Boxes").readlines()

boxes = []
for line in file:
    line = list(map(int,line.strip().split(",")))
    boxes.append(line)

distances = []
i = 0
while i < len(boxes):
    j = i + 1
    while j < len(boxes):
        first_box = boxes[i]
        second_box = boxes[j]
        heapq.heappush(distances, (math.dist(first_box,second_box), first_box, second_box))
        j += 1
    i += 1

connections = []
not_connected = True
while not_connected:
    dist, box_1, box_2 = heapq.heappop(distances)
    box_1_connection = None
    box_2_connection = None
    for connection in connections:
        if box_1 in connection:
            box_1_connection = connection
        if box_2 in connection:
            box_2_connection = connection
    if box_1_connection is not None:
        if box_2_connection is not None:
            if box_1_connection != box_2_connection:
                new_connection = box_1_connection + box_2_connection
                connections.remove(box_1_connection)
                connections.remove(box_2_connection)
                connections.append(new_connection)
        else:
            box_1_connection.append(box_2)
    elif box_2_connection is not None:
        box_2_connection.append(box_1)
    else:
        connections.append([box_1,box_2])

    if len(connections) == 1 and len(connections[0]) == len(boxes):
        not_connected = False

print(box_1[0] * box_2[0])