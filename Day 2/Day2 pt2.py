file = open("Ids", "r")

lines = file.readline().strip().split(",")

def check_same(i, same, str):
    if str == "":
        return True
    elif str[:i] == same:
        return check_same(i, same, str[i:])
    else:
        return False

count = 0
for line in lines:
    ids = line.split("-")
    num = int(ids[0])
    while num < int(ids[1]) + 1:
        str_num = str(num)
        i = 1
        while i <= len(str_num) // 2:
            if check_same(i,str_num[:i], str_num[i:]):
                count += num
                i = 100
            else:
                pass
            i += 1
        num += 1
print(count)


