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

f = open("Spiro.kml", 'w')
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
f.write("<Folder>\n")
f.write("<Style id='z1'>\n")
f.write("<IconStyle><Icon><href>http://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png</href></Icon></IconStyle>\n")
f.write("</Style>\n")
f.write("<Placemark>\n")
f.write("<name>Tommy Trojan</name>")
f.write("<styleUrl>#z1</styleUrl><Point><coordinates>-118.28553235114964,34.02053733681005</coordinates></Point>\n")
f.write("</Placemark>\n")
f.write("<Placemark>\n")
f.write("<LineString>\n")
f.write("<visibility>1</visibility>\n")
f.write("<extrude>1</extrude>\n")
f.write("<tessellate>1</tessellate>\n")
f.write("<coordinates>")

for t in np.arange(0.0, pi * nRevs, 0.02):
	x = ((R + r) * cos((r / R) * t) - a * cos((1 + r / R) * t)) / N + TommyX
	y = ((R + r) * sin((r / R) * t) - a * sin((1 + r / R) * t)) / N + TommyY

	f.write(str(x) + "," + str(y) + ",0.0" + "\n")

f.write("</coordinates>\n")
f.write("</LineString>\n")
f.write("<Style>\n")
f.write("<LineStyle>\n")
f.write("<color>80fe4d28</color>")
f.write("<width>4</width>")
f.write("</LineStyle>")
f.write("</Style>")
f.write("</Placemark>\n")
f.write("</Folder>\n")
f.write("</kml>\n")