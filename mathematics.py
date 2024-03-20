import math

"""
x = 50
a = log(x)
b = sqrt(x)
c = exp(x)
print(a)
"""

angles = [0, 30, 45, 60, 90, -90]
sines = [math.sin(math.radians(angle)) for angle in angles]
# sines = [round(sine, 3) for sine in sines]
print(sines)

angles = [math.degrees(math.asin(sine)) for sine in sines]
print(angles)
