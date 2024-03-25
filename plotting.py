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
# pyplot.scatter(valsA, valsB, s=40, marker="*")
# pyplot.show()

# Bar chart
#pyplot.bar(valsA, valsB, color="green")
#pyplot.show()

# Histogram
#pyplot.hist(valsB, bins=20, range=(-2, 2.0))
#pyplot.show()

# Pie chart
sizes = [83, 8, 4, 5]
labels = ["Arthropoda", "Mollusca", "Cordata", "Others"]
colors = ["#B00000", "#D0D000", "#008000", "#4040FF"]
pyplot.pie(sizes, labels=labels, colors=colors)
pyplot.show()