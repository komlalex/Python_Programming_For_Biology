import numpy

x = numpy.ones((2,3), dtype=int)
print(x)
print(x.shape)

y = numpy.zeros((3,2))
print(y)

z = numpy.identity(3)
print(z)

x = numpy.array(((1,1), (1,0)))
y = numpy.array(((0,1), (1,1)))
z = numpy.dot(x, y)
print(z)


keys = [1,2,3]
values = ["Apple", "Banana", "Orange"]
dictData = zip(keys, values)
print(dictData)