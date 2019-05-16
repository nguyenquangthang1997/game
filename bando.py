# map = []
import random

file = open("map.txt", "w+")


def creatMap():
    for i in range(0, 12, 1):
        strTemp = ''
        for j in range(0, 12, 1):
            temp = random.randint(0, 3)
            strTemp = strTemp + str(temp) + " "
        file.writelines(strTemp + "\n")


creatMap()
