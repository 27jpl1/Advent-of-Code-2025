file = open("Ids", "r")

lines = file.readline().strip().split(",")

count = 0
for line in lines:
    ids = line.split("-")
    num = int(ids[0])
    while num < int(ids[1]) + 1:
        str_num = str(num)
        mid = len(str_num) // 2
        if str_num[0:mid] == str_num[mid:]:
            count += num
        num += 1
print(count)


