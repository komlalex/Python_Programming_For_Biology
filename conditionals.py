
from math import factorial, inf
import sys
import os
z = 0 and 1
z = 1 and 2
z = 5 and 0
print(z)

x = "Hello"
text = x and "Yes" or "No"
text = "Yes" if x else "No"
print(text)

values = [13, 23, 14, 4, 3, 4, 265, 4, 6, 4, 6]
for v in values:
    print(v)

value = 1
while value < 32:
    print(f"{value} is less than 32")
    value *= 2

values = [5,-5,-3,7,8]
total = 0
for v in values:
    if v < 0:
        continue
    total = total + v

print(total)

vec1 = (4, 7, 0)
vec2 = (1, 3, 5)
s = 0
for i in range(len(vec1)):
    s += vec1[i] * vec2[i]


s = 0
for i, x in enumerate(vec1):
    s += x * vec2[i]
print(s)

squares = []
for n in range(1,8):
    squares.append(n*n)


# List comprehension
squares2 = [x*x for x in range(1,8)]
print(squares2)

values = [1,2,3,4,5,6,7,8,9]

for val in list(values):
    if val < 5:
        values.remove(val)

container = []

for val in values:
    if val >= 5:
        container.append(val)

values = container



values = [val for val in range(len(values)) if val >= 5]

nums = [1,2,3,4,5,6,7,8,9]
result = [factorial(x) for x in nums if factorial(x) >= 700]

print(result)

yearDict = {"Jan": 31, "Feb": 28, "Mar": 31}
total = 0
for month in yearDict:
    total += yearDict[month]

print(total)

x = 1
y = 0
try:
    z = x + y
    w = x * y
    t = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program did not stop")

try:
    t = x / y
except ZeroDivisionError as errorObj:
    print("New eror: ", errorObj)

try:
    t = x / y
except Exception as errorObj:
    print("General Exception: ", errorObj)
finally:
    print("We are done here!!")
print("We moove!!")

try:
    sys.exit()
except SystemExit:
    print("Exit stopped")

os._exit(0)

print("Not reached")