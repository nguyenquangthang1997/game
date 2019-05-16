file = open("map.txt", "r")
map = []

for line in file:
    strTemp = line.split(" ")
    map.append(strTemp[0:12])

# 3 1 2 3 2 0 3 2 2 0 0 0
# 2 3 0 2 0 0 0 1 0 0 1 3
# 1 0 2 3 3 1 0 2 2 1 2 3
# 0 2 0 3 3 2 2 0 0 3 2 0
# 2 0 0 2 2 2 1 0 0 3 3 2
# 3 0 3 1 1 3 3 3 0 0 3 2
# 2 0 2 2 1 0 0 2 1 2 1 2
# 2 2 2 2 2 3 2 2 3 1 2 1
# 2 3 2 1 2 0 3 1 3 1 3 0
# 2 0 0 3 3 1 0 1 3 0 3 0
# 2 0 1 0 2 2 0 3 2 3 2 0
# 1 1 2 0 0 0 3 2 0 1 1 1


# 2 3 0 3 2 1 1 0 3 0 1 1
# 3 0 1 2 1 0 2 2 2 2 2 3
# 2 0 1 3 3 0 1 0 1 0 0 2
# 3 2 3 0 1 1 2 0 3 1 3 1
# 2 0 0 0 0 3 0 2 3 1 1 2
# 3 0 1 1 1 3 2 3 1 0 0 2
# 3 0 1 2 3 1 0 1 0 3 1 2
# 1 3 0 0 1 2 1 3 0 3 0 1
# 1 1 3 1 0 0 0 0 3 2 3 0
# 3 2 2 0 3 2 0 3 1 2 3 1
# 2 1 0 0 3 3 2 0 2 2 2 3
# 2 2 3 0 1 2 2 2 1 2 1 1

# i la y, j la x
for i in range(0, 12, 1):
    for j in range(0, 12, 1):
        map[i][j] = int(map[i][j])
        # for j in range(1, 3):
    #     print(map[i][j])


def burn(i, j):
    # if (i & j == 0 or i == 11 or j == 11):
    #     return 1
    #
    print (str(i)+"aaaaaa"+str(j))

    for i in range(0, 12, 1):
        print map[i]


    map[i][j] = 0
    for k in range(i - 1, -1, -1):
        if map[k][j] != 0:
            map[k][j] = map[k][j] + 1
            if map[k][j] == 4:
                burn(k, j)
            break
    for k in range(i + 1, 12, 1):
        if map[k][j] != 0:
            map[k][j] = map[k][j] + 1
            if map[k][j] == 4:
                burn(k, j)
            break
    for k in range(j - 1, -1, -1):
        if map[i][k] != 0:
            map[i][k] = map[i][k] + 1
            if map[i][k] == 4:
                burn(i, k)
            break
    for k in range(j + 1, 12, 1):
        if map[i][k] != 0:
            map[i][k] = map[i][k] + 1
            if map[i][k] == 4:
                burn(i, k)
            break


def click(i, j):
    if map[i][j] == 0:
        return
    elif map[i][j] >= 3:
        burn(i, j)
    else:
        map[i][j] = map[i][j] + 1

def tong(map):
    tong = 0
    for i in range(0, 12, 1):
        for j in range(0, 12, 1):
            tong = map[i][j] + tong
    return tong == 0

# print(tong())
burn(0,10)
# print (tong())
# click(9,9)
# click(9,9)
# burn(1,1)
# burn(11,1)


for i in range(0, 12, 1):
    print map[i]
