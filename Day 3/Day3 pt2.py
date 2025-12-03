import sys

file = open("Batteries", "r").readlines()

batteries = []
for line in file:
    batteries.append(line.strip())

def find_best(lst, length):
    if length > len(lst):
        print("this broke")
        sys.exit()
    if length == 0:
        return 0
    else:
        best_num = 0
        index = 0
        i = 0
        while len(lst) - i >= length:
            if int(lst[i]) > best_num:
                best_num = int(lst[i])
                index = i
            i += 1
        return best_num * (10 ** (length - 1)) + find_best(lst[index+1:], length - 1)


total = 0
for battery in batteries:
    add = find_best(battery, 12)
    total += add
print(total)

