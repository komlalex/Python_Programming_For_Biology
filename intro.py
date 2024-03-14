numbers = [2,4,6,8,10]
numbers.reverse()
print(numbers)

mass = 12.785
volume = 4.253
density = mass/volume
print(density)

x = 1
y = 2
print(x.__add__(y))

z = 4.5e10

print(type(z))

print(1e-2)
print(0.2+0.1)

print("Hello, wanna see me move to a new line? \nThere you go.")

hungry = True
chocolate = False

happiness = (not hungry) or (hungry and chocolate)
print(happiness)

days = [1, 2, 3, 4, 5]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][0])

days.append(10)
# days.reverse()
days.pop()
print(days)
matrix[0].reverse()
print(matrix)

tup1 = (3, 6, 9, 12, 15)
print(tup1[0])

font1 = ("helvetica", 10)

weekdays = {"Monday", "Tuesday", "Wednesday", "Monday"}
weekdays.add("Thursday")
weekdays.clear()
print(weekdays)

ageDict = {"alex": 23, "james": 22, "simon": 47, False: True, 33: 100}

print(ageDict["alex"])

text = "+2445.45"
floatNum = float(text)
intNum = int(floatNum)
print(intNum)

total = 0
numbers = [1, 2, 3, 4, 5, 6, 7]
for x in numbers:
    total = total + (x * x)

print(total)

def convertToFahrenheit(celcius):
    fahrenheit = 1.8 * celcius + 32.0
    return fahrenheit

print(convertToFahrenheit(10))

class unitConverter:
    def __init__(self, name):
        self.name = name
    def metresToFeet(self, m):
        f = m / 0.3048
        return f
    def feetToMetres(self, f):
        m = f * 0.3048
        return m

converter = unitConverter("Alex")

print(converter.metresToFeet(10))
print(converter.name)

print(11//5)
print(2**3)

print(pow(10,2))

text = 'Hello World'

print(text[2:])

print("war" in text)
print("Wor" in text)

print(text.find("lor"))
text.rfind("hell")
# text.rindex("old")

line = " hey there "
strip1 = line.strip()
strip2 = line.lstrip()
strip3 = line.rstrip()

name = "alex king"
names = name.split()
print(names)

joiner = "->"
fruits = ["apple", "pear", "papaya", "orange", "peaches"]
jfruits = joiner.join(fruits)
print(jfruits)

seq = ["A", "G", "T", "C"]
print("".join(seq))
print(seq[0]+seq[1]+seq[2]+seq[3])
print(f"{seq[0]}{seq[1]}{seq[2]}{seq[3]}")

x = 5
sell = "I have " + str(x) + " oranges"
print(sell)

sell2 = "I have %d apples and %d mangoes" % (x, x + 5)
print(sell2)

name = "Angela"
age = 33
weight = 130.0
text = "Hello, I am %s. I am %d years old. I weigh %f kg" % (name, age, weight)
print(text)

hours = 12
minutes = 5
seconds = 43
t = "%02d:%02d:%02d" % (hours, minutes, hours)

print(t)

# tuples
x = ()
y = (2,)
z = (7, 6, 5, 4)

w = {1, 2, 3, 1, 2, 3, 1, 2, 34}
print(type(w))

# u = {[1, 2, 3], {1, 2, 3}}

# dic = {[name]: "Hello"}

froset = frozenset({"a", "b", "c"})
print(type(froset))

original = [12, 24, 36]
copy = original[:]
print(12 in original)

ori = [1, 1, 1, 1, 3, 4, 45, 5, 3, 5, 5, 3]
print(ori.count(1))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b)
print(a)

v = a.pop(2)

a.remove(2)
print(a)

c = [12,4,24,-34,5]
c.sort()

e = [23,54,-5,745]
d = sorted(e)
print(e)

s = {123, 54, 92}
t = tuple(s)
u = list(s)

print(123 not in s)
s.add(7888)

p = {1,2,3,4,5}
q = {2,3,4,5,6}

print(p & q)
print(p | q)

d = {"Ala": 71.05, "Arg": 156.18}

# x = d.get("Gly", 100)

x = d.setdefault("Gly", 57.05)
print(d)

print(d.keys())
print(d.values())
print(d.items())

