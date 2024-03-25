from matplotlib import pyplot
from random import gauss

valuesA = [x*x for x in range(10)]
valuesB = [100/x for x in range(1, 10)]

# pyplot.plot(valuesA)
# pyplot.plot(valuesB)
# pyplot.show()

xVals = range(21, 30)
yVals = [100.0/x for x in range(1, 10)]


#pyplot.plot(xVals, yVals, color="purple", label="DataName")
#pyplot.legend()
#pyplot.ylim(0, 101)
#pyplot.yticks([0,25,50,75,100])
#pyplot.savefig("C:/Users/ACER/Desktop/holder/Rplot.png", dpi=72)
#pyplot.show()

# Scatter plot

valsA = range(100)
valsB = [gauss(0.0, 1.0) for x in valsA]
pyplot.scatter(valsA, valsB, s=40, marker="*")
pyplot.show()