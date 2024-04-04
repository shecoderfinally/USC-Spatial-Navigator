#!/usr/local/bin/python3
import numpy as np
from math import cos, sin, pi

TommyX = -118.28553235114964
TommyY = 34.02053733681005
R = 36
r = 9
a = 30
N = 20000
nRevs = 16

f = open("HW4Spiro.txt", 'w')
f.write("[\n")

for t in np.arange(0.0, pi * nRevs, 0.1):
	x = ((R + r) * cos((r / R) * t) - a * cos((1 + r / R) * t)) / N + TommyX
	y = ((R + r) * sin((r / R) * t) - a * sin((1 + r / R) * t)) / N + TommyY

	f.write("{\n")
	f.write("   \"loc\": " + "[" + str(x) + "," + str(y) + "]\n")
	f.write("},\n")

f.write("]\n")
f.close()