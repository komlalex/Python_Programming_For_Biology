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

name1 = sys.argv[0]
print("The name: ", name1)

