# Reading files
import sys

path = "C:/Users/ACER/Desktop/Practice_R/sdata.txt"

try:
    fh = open(path, "r")
    every = fh.read()
    line = fh.readline()
    # print(every)
    fh.close()
except IOError as err:
    print(err)
finally:
    print("Moving on!!!")

"""
fileObj = open(path, "r")
for line in fileObj:
    print(line)
"""

"""
fh2 = open(path, "r")
lines = fh2.readlines()
for line in lines:
    print("Line: ", line)

fh2.close()

"""

"""
fileObj2 = open(path, "r")
lines = [line for line in fileObj2]
print(lines)
"""

'''
with open(path, "r") as obj:
    for line in obj:
        print("My Line: ", line)

'''

fh = open("./mydata/chromoData.tsv")

values = []
allRows = []
positions = []
header = fh.readline()

for line in fh:
    data = line.split()
    chromosome, position, value = data
    position = int(position)
    value = float(value)

    positions.append(position)
    values.append(value)
    eachRow = [chromosome, position, value]
    allRows.append(eachRow)

print(values)
print(positions)
print(allRows)

# Means
valueMean = sum(values) / len(values)
positionMean = sum(positions) / len(positions)

# Maximum
maxValue = max(values)
maxPosition = max(positions)

print(f"Mean values: {valueMean}")
print(f"Mean of positions: {positionMean}")
print(f"Maximum value: {maxValue}")
print(f"Maximum position: {maxPosition}")

