from math import sin, cos, degrees, radians, atan2, floor, ceil

"""
x = 50
a = log(x)
b = sqrt(x)
c = exp(x)
print(a)
"""

# angles = [0, 30, 45, 60, 90, -90]
# sines = [math.sin(math.radians(angle)) for angle in angles]
# sines = [round(sine, 3) for sine in sines]
# print(sines)

# angles = [math.degrees(math.asin(sine)) for sine in sines]


# print(angles)

# Mean Angle

def meanAngle(angles, inDegrees=True):
    sumCos = 0.0
    sumSin = 0.0

    for angle in angles:
        if inDegrees:
            angle = radians(angle)
        sumCos += cos(angle)
        sumSin = sin(angle)

    N = len(angles)
    meanAng = atan2(sumSin / N, sumCos / N)

    if inDegrees:
        meanAng = degrees(meanAng)

    return meanAng


angles2 = [100, 150, 150, 70, 90, 160]
meanAng = meanAngle(angles2)
print(meanAng)

# Rounding
y = floor(5.25)
print(ceil(5.25))
print(type(y))

print(round(9631, -2))

